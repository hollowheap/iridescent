from pathlib import Path
import unittest

try:
    from draw_support import run_cli, workspace
except ModuleNotFoundError:
    from tests.draw_support import run_cli, workspace


def setup_superseded(
    artifacts,
    *,
    supersedes="S01",
    covers="S01/C01",
    parent="S02",
    include_old=True,
    include_old_case=True,
):
    old = ""
    if include_old:
        old = (
            "- [ ] S01 [R01, D01]: Old spec\n"
            "  - Verify: echo old\n"
            "  - Ledger: tests/S01.md\n\n"
        )
    (artifacts / "REQUIREMENTS.md").write_text(
        "# Requirements\n\n### Slice\n\n"
        "- [ ] R01: Deliver slice\n  - Verify: echo req\n",
        encoding="utf-8",
    )
    (artifacts / "DECISIONS.md").write_text(
        "# Decisions\n\n### System Shape\n\n"
        "- [ ] D01 [R01]: Replace old spec\n",
        encoding="utf-8",
    )
    (artifacts / "SPECS.md").write_text(
        "# Specs\n\n### Slice\n\n#### System Shape\n\n"
        + old
        + "- [ ] S02 [R01, D01]: New spec\n"
        "  - Verify: echo spec\n"
        "  - Ledger: tests/S02.md\n"
        "  - Supersedes: " + supersedes + "\n",
        encoding="utf-8",
    )
    (artifacts / "TASKS.md").write_text(
        "# Tasks\n\n### Slice\n\n"
        "- [ ] T01 [" + parent + "]: New task\n"
        "  - Verify: echo task\n"
        "  - Detail: tasks/T01.md\n"
        "  - Cases: C01\n",
        encoding="utf-8",
    )
    tests = artifacts / "tests"
    tests.mkdir(exist_ok=True)
    old_case = "# Test Ledger: S01\n\n### C01: Old case\n- Seam: test\n- Red: true\n"
    (tests / "S01.md").write_text(
        old_case if include_old_case else "# Test Ledger: S01\n",
        encoding="utf-8",
    )
    (tests / "S02.md").write_text(
        "# Test Ledger: S02\n\n### C01: New case\n- Seam: test\n- Red: true\n  - Covers: " + covers + "\n",
        encoding="utf-8",
    )
    task_dir = artifacts / "tasks"
    task_dir.mkdir(exist_ok=True)
    (task_dir / "T01.md").write_text("# Task Detail: T01\n", encoding="utf-8")


class S08Tests(unittest.TestCase):
    def test_c01_valid_supersession_passes(self):
        with workspace() as (root, artifacts):
            setup_superseded(artifacts)
            result = run_cli("verify-links", cwd=root)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_c02_unresolved_supersedes_fails(self):
        with workspace() as (root, artifacts):
            setup_superseded(artifacts, supersedes="S99")
            result = run_cli("verify-links", cwd=root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Unresolved Supersedes: S99", result.stderr)

    def test_c03_superseded_parent_fails(self):
        with workspace() as (root, artifacts):
            setup_superseded(artifacts, parent="S01")
            result = run_cli("verify-links", cwd=root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Active reference to superseded ID: S01", result.stderr)

    def test_c04_unresolved_covers_fails(self):
        with workspace() as (root, artifacts):
            setup_superseded(artifacts, covers="S99/C01")
            result = run_cli("verify-links", cwd=root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Unresolved Covers: S99/C01", result.stderr)

    def test_c05_missing_superseded_spec_fails(self):
        with workspace() as (root, artifacts):
            setup_superseded(artifacts, include_old=False)
            result = run_cli("verify-links", cwd=root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Unresolved Supersedes: S01", result.stderr)

    def test_c06_missing_superseded_case_fails(self):
        with workspace() as (root, artifacts):
            setup_superseded(artifacts, include_old_case=False)
            result = run_cli("verify-links", cwd=root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Unresolved Covers: S01/C01", result.stderr)


if __name__ == "__main__":
    unittest.main()
