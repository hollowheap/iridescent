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
      rulesFile = ./rules/artifacts.md;
      artifactsScript = ./scripts/artifacts.sh;

      skillNames = builtins.attrNames (
        lib.filterAttrs (_: type: type == "directory") (builtins.readDir skillsRoot)
      );

      mkIridescentArtifacts =
        pkgs:
        let
          artifactsApp = pkgs.writeShellApplication {
            name = "artifacts.sh";
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
            ln -s $out/bin/artifacts.sh $out/bin/iridescent-artifacts
            ln -s $out/bin/artifacts.sh $out/bin/artifacts
          '';
        };

      renderSkill =
        invocation: content:
        lib.foldl' (
          text: name:
          builtins.replaceStrings [ "{{skill:${name}}}" ] [ (invocation name) ] text
        ) content skillNames;

      mkSkillDir =
        pkgs:
        {
          prefix,
          invocation ? (name: name),
        }:
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
              srcFile =
                if lib.hasSuffix ".md" (toString file) then
                  pkgs.writeText "${name}-${builtins.replaceStrings [ "/" ] [ "-" ] rel}" (
                    renderSkill invocation (builtins.readFile file)
                  )
                else
                  file;
            in
            ''
              install -D -m${mode} ${srcFile} "$out/${rel}"
            ''
          ) files}
          install -D -m0755 ${helper}/bin/artifacts.sh "$out/scripts/artifacts.sh"
        '';

      mkSkillDirs =
        pkgs:
        {
          prefix,
          invocation ? (name: name),
        }:
        lib.genAttrs skillNames (mkSkillDir pkgs { inherit prefix invocation; });

      mkSkillFileAttrs =
        {
          baseDir,
          invocation ? (name: name),
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
                    value =
                      if lib.hasSuffix ".md" (toString file) then
                        { text = renderSkill invocation (builtins.readFile file); }
                      else
                        {
                          source = file;
                          executable = lib.hasPrefix "scripts/" rel;
                        };
                  }
                ) files;
                helperEntry = {
                  name = "${baseDir}/${name}/scripts/artifacts.sh";
                  value =
                    if pkgs != null then
                      { source = "${mkIridescentArtifacts pkgs}/bin/artifacts.sh"; }
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
          ruleText = builtins.readFile rulesFile;
          hasOpt = name: options.programs ? ${name};
          enabled = name: hasOpt name && (config.programs.${name}.enable or false);
        in
        {
          options.programs.iridescent.enable = lib.mkOption {
            type = lib.types.bool;
            default = true;
            description = "Install iridescent skills, iridescent-artifacts, and workspace artifact rules into enabled AI harnesses.";
          };

          config = lib.mkIf cfg.enable (
            lib.mkMerge [
              {
                home.packages = [ (mkIridescentArtifacts pkgs) ];
              }

              (lib.optionalAttrs (hasOpt "claude-code") {
                programs.claude-code = lib.mkIf (enabled "claude-code") {
                  skills = mkSkillDirs pkgs { prefix = "claude-code"; };
                  rules.artifacts = rulesFile;
                };
              })

              (lib.optionalAttrs (hasOpt "opencode") {
                programs.opencode = lib.mkIf (enabled "opencode") {
                  skills = mkSkillDirs pkgs {
                    prefix = "opencode";
                    invocation = name: "@${name}";
                  };
                  context = lib.mkAfter ruleText;
                };
              })

              (lib.optionalAttrs (hasOpt "codex") {
                programs.codex = lib.mkIf (enabled "codex") {
                  skills = mkSkillDirs pkgs {
                    prefix = "codex";
                    invocation = name: "$" + name;
                  };
                  context = lib.mkAfter ruleText;
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
                  context = lib.mkAfter ruleText;
                };
              })

              (lib.optionalAttrs (hasOpt "antigravity-cli") {
                programs.antigravity-cli = lib.mkIf (enabled "antigravity-cli") {
                  skills = mkSkillDirs pkgs {
                    prefix = "antigravity";
                    invocation = name: "/${name}";
                  };
                  context = lib.mkAfter ruleText;
                };
              })

              (lib.optionalAttrs (hasOpt "kiro-cli") {
                home.file = lib.mkIf (enabled "kiro-cli") (
                  (mkSkillFileAttrs {
                    baseDir = ".kiro/skills";
                    inherit pkgs;
                  })
                  // {
                    ".kiro/steering/artifacts.md".source = rulesFile;
                  }
                );
              })

              (lib.optionalAttrs (hasOpt "pi-coding-agent") {
                home.file = lib.mkIf (enabled "pi-coding-agent") (
                  mkSkillFileAttrs {
                    baseDir = "${config.programs.pi-coding-agent.configDir}/skills";
                    invocation = name: "/skill:${name}";
                    inherit pkgs;
                  }
                );
                programs.pi-coding-agent.context = lib.mkIf (enabled "pi-coding-agent") (
                  lib.mkAfter ruleText
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
          rulesFile
          artifactsScript
          mkIridescentArtifacts
          renderSkill
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
