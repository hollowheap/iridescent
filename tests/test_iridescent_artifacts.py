import os
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CLI_PATH = REPO_ROOT / "scripts" / "iridescent-artifacts"
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


class IridescentArtifactsTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.workspace = Path(self._tmp.name)
        self.artifacts = self.workspace / ".artifacts"
        self.artifacts.mkdir()
        (self.artifacts / "CONTEXT.md").write_text("# Context\n", encoding="utf-8")
        (self.artifacts / "ARCHITECTURE.md").write_text(
            "# Architecture\n\n## Skill Authoring\n\nAuthoring slice.\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self._tmp.cleanup()

    def run_cli(self, *args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python3", "-B", str(CLI_PATH), *args],
            cwd=cwd or self.workspace,
            text=True,
            capture_output=True,
        )

    def write_test_file(self, spec_id: str) -> None:
        tests_dir = self.workspace / "tests"
        tests_dir.mkdir(exist_ok=True)
        (tests_dir / f"test_{spec_id.lower()}.py").write_text("pass\n", encoding="utf-8")

    def write_task_detail(self, task_id: str) -> None:
        detail_dir = self.artifacts / "tasks"
        detail_dir.mkdir(exist_ok=True)
        (detail_dir / f"{task_id}.md").write_text(
            f"# Task Detail: {task_id}\n\n"
            "## Steps\n\n"
            "- Step: reproduce the test.\n\n"
            "## Notes\n\n"
            "- none\n\n"
            "## Risk\n\n"
            "- low\n",
            encoding="utf-8",
        )

    def write_receipt(self, task_id: str, command: str, result: str = "OK") -> None:
        tasks_dir = self.artifacts / "tasks"
        tasks_dir.mkdir(exist_ok=True)
        lines = [
            "## 2026-01-01 — receipt",
            "",
            f"- Task: {task_id}",
            "",
            "## Verify",
            "",
            f"- `{command}` → {result}",
            "",
        ]
        (tasks_dir / "quick.md").write_text("\n".join(lines), encoding="utf-8")

    def write_open_task_graph(self) -> None:
        (self.artifacts / "DECISIONS.md").write_text(
            "# Decisions\n\n## Skill Authoring\n\n"
            "- [ ] D01: Single process\n",
            encoding="utf-8",
        )
        (self.artifacts / "REQUIREMENTS.md").write_text(
            "# Requirements\n\n## Skill Authoring\n\n"
            "- [ ] R01 [D01]: Deliver slice\n  - Verify: echo req\n",
            encoding="utf-8",
        )
        (self.artifacts / "SPECS.md").write_text(
            "# Specs\n\n## Skill Authoring\n\n"
            "- [ ] S01 [R01]: Handle request cleanly\n"
            "  - Verify: echo spec\n"
            "  - Tests: tests/test_s01.py\n",
            encoding="utf-8",
        )
        (self.artifacts / "TASKS.md").write_text(
            "# Tasks\n\n## Skill Authoring\n\n"
            "- [ ] T01 [S01]: First task\n"
            "  - Verify: echo t1\n"
            "- [ ] T02 [S01] [T01]: Dependent task\n"
            "  - Verify: echo t2\n",
            encoding="utf-8",
        )
        self.write_test_file("S01")
        self.write_task_detail("T01")
        self.write_task_detail("T02")

    def test_status_and_verify_links_on_empty_graph(self):
        status = self.run_cli("status")
        self.assertEqual(status.returncode, 0, status.stderr)
        self.assertEqual(status.stdout.strip(), "CONTEXT:present REQ:0 DEC:0 SPEC:0 TASK:0")

        verify = self.run_cli("verify-links")
        self.assertEqual(verify.returncode, 0, verify.stderr)
        self.assertEqual(verify.stdout.strip(), "OK")

    def test_active_decisions_projects_append_only_log(self):
        (self.artifacts / "DECISIONS.md").write_text(
            "# Decisions\n\n## Skill Authoring\n\n"
            "- [x] D01: Accepted choice\n",
            encoding="utf-8",
        )

        active = self.run_cli("active-decisions")
        self.assertEqual(active.returncode, 0, active.stderr)
        self.assertIn("D01: Accepted choice", active.stdout)

    def test_frontier_and_next_task_handoff(self):
        (self.artifacts / "DECISIONS.md").write_text(
            "# Decisions\n\n## Skill Authoring\n\n"
            "- [ ] D01: Single process\n",
            encoding="utf-8",
        )
        (self.artifacts / "REQUIREMENTS.md").write_text(
            "# Requirements\n\n## Skill Authoring\n\n"
            "- [ ] R01 [D01]: Deliver slice\n  - Verify: echo req\n",
            encoding="utf-8",
        )
        (self.artifacts / "SPECS.md").write_text(
            "# Specs\n\n## Skill Authoring\n\n"
            "- [ ] S01 [R01]: Handle request cleanly\n"
            "  - Verify: echo spec\n"
            "  - Tests: tests/test_s01.py\n",
            encoding="utf-8",
        )
        (self.artifacts / "TASKS.md").write_text(
            "# Tasks\n\n## Skill Authoring\n\n"
            "- [x] T01 [S01]: First task\n"
            "  - Verify: echo t1\n"
            "- [ ] T02 [S01] [T01]: Dependent task\n"
            "  - Verify: echo t2\n",
            encoding="utf-8",
        )
        self.write_test_file("S01")
        self.write_task_detail("T01")
        self.write_task_detail("T02")

        frontier = self.run_cli("frontier")
        self.assertEqual(frontier.returncode, 0, frontier.stderr)
        self.assertIn("T02 [S01] [T01]", frontier.stdout)

        nxt = self.run_cli("next-task")
        self.assertEqual(nxt.returncode, 0, nxt.stderr)
        self.assertIn("TASK - [ ] T02 [S01] [T01]: Dependent task", nxt.stdout)
        self.assertIn("S01 [R01]", nxt.stdout)
        self.assertIn("Tests: tests/test_s01.py", nxt.stdout)
        self.assertIn("Verify: echo t2", nxt.stdout)

        verify = self.run_cli("verify-links")
        self.assertEqual(verify.returncode, 0, verify.stderr)

    def test_complete_marks_task_and_unblocks_dependent(self):
        self.write_open_task_graph()
        self.write_receipt("T01", "echo t1")

        result = self.run_cli("complete", "T01")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Completed T01", result.stdout)
        self.assertIn("- [x] T01 [S01]", (self.artifacts / "TASKS.md").read_text(encoding="utf-8"))

        nxt = self.run_cli("next-task")
        self.assertEqual(nxt.returncode, 0, nxt.stderr)
        self.assertIn("T02", nxt.stdout)

    def test_complete_requires_matching_receipt(self):
        self.write_open_task_graph()
        self.write_receipt("T01", "echo wrong")

        result = self.run_cli("complete", "T01")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Verify mismatch", result.stderr)

    def test_complete_rejects_open_blocker(self):
        self.write_open_task_graph()
        self.write_receipt("T02", "echo t2")

        result = self.run_cli("complete", "T02")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Open blocker", result.stderr)

    def test_next_id_skips_archived_ids(self):
        archive = self.artifacts / "archive"
        archive.mkdir()
        (archive / "DECISIONS.md").write_text(
            "# Retired Decisions\n\n## Skill Authoring\n\n"
            "  - [x] DEC-99: Retired decision\n",
            encoding="utf-8",
        )

        result = self.run_cli("next-id", "d")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "D100")

    def test_skill_wrappers_exist_for_all_scripted_skills(self):
        for skill in SCRIPTED_SKILLS:
            wrapper = REPO_ROOT / "skills" / skill / "scripts" / "iridescent-artifacts"
            skill_cli = wrapper.parent / "iridescent-artifacts-cli"
            self.assertTrue(wrapper.is_file(), f"missing wrapper: {wrapper}")
            self.assertTrue(os.access(wrapper, os.X_OK), f"wrapper not executable: {wrapper}")
            self.assertTrue(skill_cli.is_file(), f"missing skill CLI: {skill_cli}")
            self.assertEqual(skill_cli.read_bytes(), CLI_PATH.read_bytes())
            text = wrapper.read_text(encoding="utf-8")
            self.assertIn("$SELF_DIR/iridescent-artifacts-cli", text)
            self.assertNotIn("../../../", text)
            self.assertNotIn("$PWD", text)
            self.assertNotIn("curl", text)

            result = subprocess.run(
                [str(wrapper), "status"],
                cwd=self.workspace,
                env={**os.environ, "ARTIFACTS_DIR": str(self.artifacts)},
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, f"{skill}: {result.stderr}")
            self.assertIn("CONTEXT:present", result.stdout)


if __name__ == "__main__":
    unittest.main()
