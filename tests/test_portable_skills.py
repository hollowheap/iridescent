"""Cases: C0701"""

from pathlib import Path
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent
AFFECTED_SKILLS = ("design", "specify", "doctor-iridescent")
SCRIPTED_SKILLS = (
    "design",
    "doctor-iridescent",
    "draw",
    "how-to-iridescent",
    "implement",
    "plan",
    "review",
    "specify",
    "update",
)
FORBIDDEN = ("rules/artifacts.md", "rules/slicing.md")


class PortableSkillsTests(unittest.TestCase):
    def test_local_reference_copies(self):
        for skill in AFFECTED_SKILLS:
            references = REPO_ROOT / "skills" / skill / "references"
            for name in ("artifacts.md", "slicing.md"):
                self.assertTrue((references / name).is_file(), f"missing {skill}/{name}")

    def test_skill_bodies_avoid_root_rules(self):
        for path in sorted((REPO_ROOT / "skills").glob("*/SKILL.md")):
            text = path.read_text(encoding="utf-8")
            for forbidden in FORBIDDEN:
                self.assertNotIn(forbidden, text, f"{path.name} references {forbidden}")

    def test_root_rules_retired(self):
        for name in ("artifacts.md", "slicing.md"):
            self.assertFalse((REPO_ROOT / "rules" / name).exists(), f"rules/{name} still exists")

    def test_skill_trees_avoid_root_rules(self):
        for path in (REPO_ROOT / "skills").rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for forbidden in FORBIDDEN:
                self.assertNotIn(forbidden, text, f"{path.relative_to(REPO_ROOT)} references {forbidden}")

    def test_flake_rules_wiring_retired(self):
        flake = (REPO_ROOT / "flake.nix").read_text(encoding="utf-8")
        self.assertNotIn("rulesFile", flake)
        self.assertNotIn("rules/artifacts.md", flake)

    def test_no_host_specific_paths(self):
        pattern = re.compile(r"/home/|~/\.claude|~/\.config/pi|~/\.pi")
        for path in (REPO_ROOT / "skills").rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            self.assertIsNone(pattern.search(text), f"host path in {path.relative_to(REPO_ROOT)}")

    def test_skill_local_cli_resolves_sibling_copy(self):
        canonical = (REPO_ROOT / "scripts" / "iridescent-artifacts").read_bytes()
        for skill in SCRIPTED_SKILLS:
            scripts = REPO_ROOT / "skills" / skill / "scripts"
            wrapper = (scripts / "iridescent-artifacts").read_text(encoding="utf-8")
            self.assertIn("$SELF_DIR/iridescent-artifacts-cli", wrapper)
            self.assertNotIn("../../../", wrapper)
            self.assertNotIn("$PWD", wrapper)
            self.assertEqual(
                (scripts / "iridescent-artifacts-cli").read_bytes(),
                canonical,
                f"CLI copy out of sync in {skill}",
            )

    def test_skill_docs_use_skill_local_cli_pointer(self):
        for path in (REPO_ROOT / "skills").rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            self.assertNotIn(
                "`scripts/iridescent-artifacts",
                text,
                f"root-relative CLI pointer in {path.relative_to(REPO_ROOT)}",
            )

    def test_installed_skill_dir_runs_without_repo(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            installed = root / "installed" / "design"
            shutil.copytree(REPO_ROOT / "skills" / "design", installed)
            artifacts = root / ".artifacts"
            artifacts.mkdir()
            (artifacts / "CONTEXT.md").write_text("# Context\n", encoding="utf-8")
            (artifacts / "ARCHITECTURE.md").write_text("# Architecture\n", encoding="utf-8")
            bash = shutil.which("bash")
            env = {
                **os.environ,
                "ARTIFACTS_DIR": str(artifacts),
                "PATH": f"{Path(sys.executable).parent}:{Path(bash).parent}",
            }
            result = subprocess.run(
                [bash, str(installed / "scripts" / "iridescent-artifacts"), "status"],
                cwd=root,
                env=env,
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("CONTEXT:present", result.stdout)


if __name__ == "__main__":
    unittest.main()
