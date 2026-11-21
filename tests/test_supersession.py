"""Cases: C0801"""

from pathlib import Path
import unittest

try:
    from draw_support import run_cli, workspace
except ModuleNotFoundError:
    from tests.draw_support import run_cli, workspace


def write_graph(artifacts, *, old_tree: bool = False):
    artifacts.mkdir(parents=True, exist_ok=True)
    (artifacts / "ARCHITECTURE.md").write_text(
        "# Architecture\n\n## Skill Contracts\n\nContract slice.\n",
        encoding="utf-8",
    )

    old_req = (
        "- [x] R01 [D01]: Old requirement\n  - Verify: echo old\n"
        if old_tree
        else ""
    )
    (artifacts / "REQUIREMENTS.md").write_text(
        "# Requirements\n\n## Skill Contracts\n\n"
        f"{old_req}"
        "- [x] R02 [D02]: Deliver replacement\n  - Verify: echo req\n",
        encoding="utf-8",
    )
    (artifacts / "DECISIONS.md").write_text(
        "# Decisions\n\n## Skill Contracts\n\n"
        "- [x] D01: Old decision\n"
        "- [x] D02: Replace old decision\n"
        "  - Supersedes: D01\n",
        encoding="utf-8",
    )

    old_spec = (
        "- [x] S01 [R01]: Old spec\n"
        "  - Verify: echo old spec\n"
        "  - Tests: tests/test_s01.py\n"
        if old_tree
        else ""
    )
    (artifacts / "SPECS.md").write_text(
        "# Specs\n\n## Skill Contracts\n\n"
        f"{old_spec}"
        "- [x] S03 [R02]: Handle request\n"
        "  - Verify: echo spec\n"
        "  - Tests: tests/test_s03.py\n",
        encoding="utf-8",
    )

    old_task = (
        "- [x] T01 [S01] [C0101]: Old task\n  - Verify: echo old task\n"
        if old_tree
        else ""
    )
    (artifacts / "TASKS.md").write_text(
        "# Tasks\n\n## Skill Contracts\n\n"
        f"{old_task}"
        "- [x] T02 [S03] [C02]: Make green\n"
        "  - Verify: echo task\n",
        encoding="utf-8",
    )

    tests = artifacts.parent / "tests"
    tests.mkdir(exist_ok=True)
    (tests / "test_s03.py").write_text("# C02\n", encoding="utf-8")
    if old_tree:
        (tests / "test_s01.py").write_text("# C0101\n", encoding="utf-8")

    tasks = artifacts / "tasks"
    tasks.mkdir(exist_ok=True)
    (tasks / "T02.md").write_text(
        "# Task Detail: T02\n\n## Steps\n\n- Step: make green.\n\n## Notes\n\n- none\n\n## Risk\n\n- low\n",
        encoding="utf-8",
    )
    if old_tree:
        (tasks / "T01.md").write_text(
            "# Task Detail: T01\n\n## Steps\n\n- Step: retired.\n\n## Notes\n\n- none\n\n## Risk\n\n- low\n",
            encoding="utf-8",
        )


class ArchiveRetirementTests(unittest.TestCase):
    def test_active_decisions_excludes_superseded(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts)
            result = run_cli("active-decisions", cwd=root)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("D02: Replace old decision", result.stdout)
            self.assertNotIn("D01: Old decision", result.stdout)

    def test_valid_archive_retirement_passes(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts)
            result = run_cli("verify-links", cwd=root)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_archive_dry_run_lists_subtree(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts, old_tree=True)
            result = run_cli("archive", "--dry-run", cwd=root)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("REQ R01", result.stdout)
            self.assertIn("SPEC S01", result.stdout)
            self.assertIn("TASK T01", result.stdout)

    def test_archive_moves_superseded_subtree(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts, old_tree=True)
            result = run_cli("archive", cwd=root)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Archived REQ R01", result.stdout)
            self.assertIn("Archived TASK T01", result.stdout)

            self.assertIn("R01", (artifacts / "archive" / "REQUIREMENTS.md").read_text(encoding="utf-8"))
            self.assertIn("S01", (artifacts / "archive" / "SPECS.md").read_text(encoding="utf-8"))
            self.assertIn("T01", (artifacts / "archive" / "TASKS.md").read_text(encoding="utf-8"))
            self.assertIn("C0101", (artifacts / "archive" / "tests" / "S01.md").read_text(encoding="utf-8"))
            self.assertNotIn("R01", (artifacts / "REQUIREMENTS.md").read_text(encoding="utf-8"))
            self.assertFalse((artifacts / "tasks" / "T01.md").exists())

            verify = run_cli("verify-links", cwd=root)
            self.assertEqual(verify.returncode, 0, verify.stderr)


if __name__ == "__main__":
    unittest.main()
