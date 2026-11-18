{
  description = "iridescent: RDST lifecycle skills and workspace artifact rules";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    { self, nixpkgs }:
    let
      inherit (nixpkgs) lib;

      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      forAllSystems = lib.genAttrs systems;

      skillsRoot = ./skills;
      artifactsScript = ./scripts/iridescent-artifacts;

      skillNames = builtins.attrNames (
        lib.filterAttrs (_: type: type == "directory") (builtins.readDir skillsRoot)
      );

      mkIridescentArtifacts =
        pkgs:
        let
          artifactsApp = pkgs.writeShellApplication {
            name = "iridescent-artifacts";
            runtimeInputs = [ pkgs.python3 ];
            text = ''
              exec python3 ${artifactsScript} "$@"
            '';
          };
        in
        pkgs.symlinkJoin {
          name = "iridescent-artifacts";
          paths = [ artifactsApp ];
          postBuild = ''
            ln -s $out/bin/iridescent-artifacts $out/bin/artifacts
            ln -s $out/bin/iridescent-artifacts $out/bin/artifacts.sh
          '';
        };

      mkSkillDir =
        pkgs:
        { prefix }:
        name:
        let
          dir = skillsRoot + "/${name}";
          files = lib.filesystem.listFilesRecursive dir;
          helper = mkIridescentArtifacts pkgs;
        in
        pkgs.runCommandLocal "${prefix}-iridescent-${name}" { } ''
          mkdir -p "$out"
          ${lib.concatMapStringsSep "\n" (
            file:
            let
              rel = lib.removePrefix (toString dir + "/") (toString file);
              mode = if lib.hasPrefix "scripts/" rel then "0755" else "0644";
            in
            ''
              install -D -m${mode} ${file} "$out/${rel}"
            ''
          ) files}
          install -D -m0755 ${helper}/bin/iridescent-artifacts "$out/scripts/iridescent-artifacts"
        '';

      mkSkillDirs =
        pkgs:
        { prefix }:
        lib.genAttrs skillNames (mkSkillDir pkgs { inherit prefix; });

      mkSkillFileAttrs =
        {
          baseDir,
          pkgs ? null,
        }:
        builtins.listToAttrs (
          builtins.concatLists (
            map (
              name:
              let
                dir = skillsRoot + "/${name}";
                files = lib.filesystem.listFilesRecursive dir;
                renderedFiles = map (
                  file:
                  let
                    rel = lib.removePrefix (toString dir + "/") (toString file);
                  in
                  {
                    name = "${baseDir}/${name}/${rel}";
                    value = {
                      source = file;
                      executable = lib.hasPrefix "scripts/" rel;
                    };
                  }
                ) files;
                helperEntry = {
                  name = "${baseDir}/${name}/scripts/iridescent-artifacts";
                  value =
                    if pkgs != null then
                      { source = "${mkIridescentArtifacts pkgs}/bin/iridescent-artifacts"; }
                    else
                      {
                        source = artifactsScript;
                        executable = true;
                      };
                };
              in
              [ helperEntry ] ++ renderedFiles
            ) skillNames
          )
        );

      hmModule =
        {
          config,
          lib,
          options,
          pkgs,
          ...
        }:
        let
          cfg = config.programs.iridescent;
          hasOpt = name: options.programs ? ${name};
          enabled = name: hasOpt name && (config.programs.${name}.enable or false);
        in
        {
          options.programs.iridescent.enable = lib.mkOption {
            type = lib.types.bool;
            default = true;
            description = "Install iridescent skills and iridescent-artifacts into enabled AI harnesses.";
          };

          config = lib.mkIf cfg.enable (
            lib.mkMerge [
              {
                home.packages = [ (mkIridescentArtifacts pkgs) ];
              }

              (lib.optionalAttrs (hasOpt "claude-code") {
                programs.claude-code = lib.mkIf (enabled "claude-code") {
                  skills = mkSkillDirs pkgs { prefix = "claude-code"; };
                };
              })

              (lib.optionalAttrs (hasOpt "opencode") {
                programs.opencode = lib.mkIf (enabled "opencode") {
                  skills = mkSkillDirs pkgs { prefix = "opencode"; };
                };
              })

              (lib.optionalAttrs (hasOpt "codex") {
                programs.codex = lib.mkIf (enabled "codex") {
                  skills = mkSkillDirs pkgs { prefix = "codex"; };
                };
              })

              (lib.optionalAttrs (hasOpt "crush") {
                programs.crush = lib.mkIf (enabled "crush") {
                  skills = mkSkillDirs pkgs { prefix = "crush"; };
                };
              })

              (lib.optionalAttrs (hasOpt "github-copilot-cli") {
                programs.github-copilot-cli = lib.mkIf (enabled "github-copilot-cli") {
                  skills = mkSkillDirs pkgs { prefix = "copilot"; };
                };
              })

              (lib.optionalAttrs (hasOpt "antigravity-cli") {
                programs.antigravity-cli = lib.mkIf (enabled "antigravity-cli") {
                  skills = mkSkillDirs pkgs { prefix = "antigravity"; };
                };
              })

              (lib.optionalAttrs (hasOpt "kiro-cli") {
                home.file = lib.mkIf (enabled "kiro-cli") (
                  mkSkillFileAttrs {
                    baseDir = ".kiro/skills";
                    inherit pkgs;
                  }
                );
              })

              (lib.optionalAttrs (hasOpt "pi-coding-agent") {
                home.file = lib.mkIf (enabled "pi-coding-agent") (
                  mkSkillFileAttrs {
                    baseDir = "${config.programs.pi-coding-agent.configDir}/skills";
                    inherit pkgs;
                  }
                );
              })
            ]
          );
        };
    in
    {
      lib = {
        inherit
          skillNames
          artifactsScript
          mkIridescentArtifacts
          mkSkillDir
          mkSkillDirs
          mkSkillFileAttrs
          ;
      };

      overlays.default = final: _prev: {
        iridescent-artifacts = mkIridescentArtifacts final;
      };

      packages = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          helper = mkIridescentArtifacts pkgs;
        in
        {
          iridescent-artifacts = helper;
          default = helper;
        }
      );

      homeManagerModules = {
        default = hmModule;
        iridescent = hmModule;
      };
    };
}
