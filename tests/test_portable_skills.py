from pathlib import Path
import re
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent
AFFECTED_SKILLS = ("design", "specify", "doctor-iridescent")
FORBIDDEN = ("rules/artifacts.md", "rules/slicing.md")


class S07Tests(unittest.TestCase):
    def test_c01_local_reference_copies(self):
        for skill in AFFECTED_SKILLS:
            references = REPO_ROOT / "skills" / skill / "references"
            for name in ("artifacts.md", "slicing.md"):
                self.assertTrue((references / name).is_file(), f"missing {skill}/{name}")

    def test_c02_skill_bodies_avoid_root_rules(self):
        for path in sorted((REPO_ROOT / "skills").glob("*/SKILL.md")):
            text = path.read_text(encoding="utf-8")
            for forbidden in FORBIDDEN:
                self.assertNotIn(forbidden, text, f"{path.name} references {forbidden}")

    def test_c03_root_rules_retired(self):
        for name in ("artifacts.md", "slicing.md"):
            self.assertFalse((REPO_ROOT / "rules" / name).exists(), f"rules/{name} still exists")

    def test_c04_skill_trees_avoid_root_rules(self):
        for path in (REPO_ROOT / "skills").rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for forbidden in FORBIDDEN:
                self.assertNotIn(forbidden, text, f"{path.relative_to(REPO_ROOT)} references {forbidden}")

    def test_c05_flake_rules_wiring_retired(self):
        flake = (REPO_ROOT / "flake.nix").read_text(encoding="utf-8")
        self.assertNotIn("rulesFile", flake)
        self.assertNotIn("rules/artifacts.md", flake)

    def test_c06_no_host_specific_paths(self):
        pattern = re.compile(r"/home/|~/\.claude|~/\.config/pi|~/\.pi")
        for path in (REPO_ROOT / "skills").rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            self.assertIsNone(pattern.search(text), f"host path in {path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    unittest.main()
