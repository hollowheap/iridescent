"""Cases: C0801"""

from pathlib import Path
import unittest

try:
    from draw_support import run_cli, workspace
except ModuleNotFoundError:
    from tests.draw_support import run_cli, workspace


def write_graph(artifacts, *, supersedes="D01"):
    (artifacts / "REQUIREMENTS.md").write_text(
        "# Requirements\n\n## Skill Contracts\n\n"
        "- [x] R02 [D02]: Deliver replacement\n  - Verify: echo req\n",
        encoding="utf-8",
    )
    (artifacts / "DECISIONS.md").write_text(
        "# Decisions\n\n## Skill Contracts\n\n"
        "- [ ] D02: Replace archived decision\n"
        f"  - Supersedes: {supersedes}\n",
        encoding="utf-8",
    )
    (artifacts / "SPECS.md").write_text(
        "# Specs\n\n## Skill Contracts\n\n"
        "- [x] S03 [R02]: Handle request\n"
        "  - Verify: echo spec\n"
        "  - Tests: tests/test_s03.py\n",
        encoding="utf-8",
    )
    (artifacts / "TASKS.md").write_text(
        "# Tasks\n\n## Skill Contracts\n\n"
        "- [x] T02 [S03] [C02]: Make green\n"
        "  - Verify: echo task\n",
        encoding="utf-8",
    )

    tests = artifacts.parent / "tests"
    tests.mkdir(exist_ok=True)
    (tests / "test_s03.py").write_text("# C02\n", encoding="utf-8")
    tasks = artifacts / "tasks"
    tasks.mkdir(exist_ok=True)
    (tasks / "T02.md").write_text(
        "# Task Detail: T02\n\n## Steps\n\n- Step: make green.\n\n## Notes\n\n- none\n\n## Risk\n\n- low\n",
        encoding="utf-8",
    )

    archive = artifacts / "archive"
    archive.mkdir(exist_ok=True)
    (archive / "DECISIONS.md").write_text(
        "# Archived Decisions\n\n## Skill Contracts\n\n"
        "- [x] D01: Old decision\n",
        encoding="utf-8",
    )


class ArchiveRetirementTests(unittest.TestCase):
    def test_active_decisions_excludes_superseded(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts)
            decisions = artifacts / "DECISIONS.md"
            decisions.write_text(
                "# Decisions\n\n## Skill Contracts\n\n"
                "- [x] D01: Old live decision\n"
                "- [ ] D02: Replace archived decision\n"
                "  - Supersedes: D01\n",
                encoding="utf-8",
            )
            result = run_cli("active-decisions", cwd=root)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("D02: Replace archived decision", result.stdout)
            self.assertNotIn("D01: Old live decision", result.stdout)

    def test_valid_archive_retirement_passes(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts)
            result = run_cli("verify-links", cwd=root)
            self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
