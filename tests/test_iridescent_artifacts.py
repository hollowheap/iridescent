import os
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CLI_PATH = REPO_ROOT / "scripts" / "iridescent-artifacts"
SCRIPTED_SKILLS = (
    "design",
    "draw",
    "doctor-iridescent",
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
            "# Architecture\n\n"
            "## System Shape\n\nShape.\n\n"
            "## Module Seams\n\nSeams.\n\n"
            "## Framework & Library Choices\n\nChoices.\n\n"
            "## Data & Contracts\n\nContracts.\n\n"
            "## Operations & Security\n\nOps.\n",
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

    def write_ledger(self, spec_id: str, *case_ids: str) -> None:
        ledger_dir = self.artifacts / "tests"
        ledger_dir.mkdir(exist_ok=True)
        lines = [f"# Test Ledger: {spec_id}", ""]
        for case_id in case_ids:
            lines.extend(
                [f"### {case_id}: Case {case_id}", "- Seam: test", "- Red: true", ""]
            )
        (ledger_dir / f"{spec_id}.md").write_text("\n".join(lines), encoding="utf-8")

    def write_task_detail(self, task_id: str) -> None:
        detail_dir = self.artifacts / "tasks"
        detail_dir.mkdir(exist_ok=True)
        (detail_dir / f"{task_id}.md").write_text(
            f"# Task Detail: {task_id}\n", encoding="utf-8"
        )

    def test_status_and_verify_links_on_empty_graph(self):
        status = self.run_cli("status")
        self.assertEqual(status.returncode, 0, status.stderr)
        self.assertEqual(status.stdout.strip(), "CONTEXT:present REQ:0 DEC:0 SPEC:0 TASK:0")

        verify = self.run_cli("verify-links")
        self.assertEqual(verify.returncode, 0, verify.stderr)
        self.assertEqual(verify.stdout.strip(), "OK")

    def test_decide_groups_under_arch_h2_without_verify_field_and_passes_links(self):
        (self.artifacts / "REQUIREMENTS.md").write_text(
            "# Requirements\n\n### CLI\n\n"
            "- [ ] R01: Manage RDST trace graph\n"
            "  - Verify: python3 -m unittest\n",
            encoding="utf-8",
        )

        res = self.run_cli(
            "decide",
            "R01",
            "Use Python 3 stdlib",
            "--arch",
            "Framework & Library Choices",
            "--context",
            "Need zero runtime deps.",
            "--alternatives",
            "Bash (fragile parsing)",
            "--consequences",
            "Requires Python 3.",
        )
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(res.stdout.strip(), "D01")

        dec_text = (self.artifacts / "DECISIONS.md").read_text(encoding="utf-8")
        self.assertIn("### Framework & Library Choices", dec_text)
        self.assertNotIn("Verify:", dec_text)

        unconverted = self.run_cli("unconverted-decs")
        self.assertEqual(unconverted.returncode, 0, unconverted.stderr)
        self.assertIn("D01 [R01]", unconverted.stdout)

        verify = self.run_cli("verify-links")
        self.assertEqual(verify.returncode, 0, verify.stderr)
        self.assertEqual(verify.stdout.strip(), "OK")

    def test_decide_rejects_verify_flag_and_unknown_arch_section(self):
        (self.artifacts / "REQUIREMENTS.md").write_text(
            "# Requirements\n\n### CLI\n\n"
            "- [ ] R01: Manage RDST trace graph\n"
            "  - Verify: python3 -m unittest\n",
            encoding="utf-8",
        )

        unknown_arch = self.run_cli(
            "decide",
            "R01",
            "Bad section",
            "--arch",
            "Nonexistent Section",
            "--alternatives",
            "None",
            "--consequences",
            "None",
        )
        self.assertNotEqual(unknown_arch.returncode, 0)
        self.assertIn("ARCHITECTURE.md", unknown_arch.stderr)

        with_verify = self.run_cli(
            "decide",
            "R01",
            "Forbidden verify",
            "--arch",
            "System Shape",
            "--alternatives",
            "None",
            "--consequences",
            "None",
            "--verify",
            "true",
        )
        self.assertNotEqual(with_verify.returncode, 0)
        self.assertIn("unrecognized arguments: --verify", with_verify.stderr)

    def test_frontier_next_task_and_bottom_up_sync(self):
        (self.artifacts / "REQUIREMENTS.md").write_text(
            "# Requirements\n\n### Slice\n\n"
            "- [ ] R01: Deliver slice\n"
            "  - Verify: echo ok\n",
            encoding="utf-8",
        )
        (self.artifacts / "DECISIONS.md").write_text(
            "# Decisions\n\n### System Shape\n\n"
            "- [ ] D01 [R01]: Single process\n",
            encoding="utf-8",
        )
        (self.artifacts / "SPECS.md").write_text(
            "# Specs\n\n### Slice\n\n#### System Shape\n\n"
            "- [ ] S01 [R01, D01]: Handle request cleanly\n"
            "  - Verify: echo spec\n"
            "  - Ledger: tests/S01.md\n",
            encoding="utf-8",
        )
        (self.artifacts / "TASKS.md").write_text(
            "# Tasks\n\n### Slice\n\n"
            "- [x] T01 [S01]: First task\n"
            "  - Verify: echo t1\n"
            "  - Detail: tasks/T01.md\n"
            "  - Cases: C01\n"
            "- [ ] T02 [S01] [T01]: Dependent task\n"
            "  - Verify: echo t2\n"
            "  - Detail: tasks/T02.md\n"
            "  - Cases: C02\n",
            encoding="utf-8",
        )
        self.write_ledger("S01", "C01", "C02")
        self.write_task_detail("T01")
        self.write_task_detail("T02")

        frontier = self.run_cli("frontier")
        self.assertEqual(frontier.returncode, 0, frontier.stderr)
        self.assertIn("T02 [S01] [T01]", frontier.stdout)

        nxt = self.run_cli("next-task")
        self.assertEqual(nxt.returncode, 0, nxt.stderr)
        self.assertIn("T02 [S01] [T01]", nxt.stdout)
        self.assertIn("S01 [R01, D01]", nxt.stdout)

        # Complete T02 and settle bottom-up through S01 -> D01 -> R01
        tasks_file = self.artifacts / "TASKS.md"
        tasks_file.write_text(
            tasks_file.read_text(encoding="utf-8").replace("- [ ] T02", "- [x] T02"),
            encoding="utf-8",
        )
        sync = self.run_cli("sync")
        self.assertEqual(sync.returncode, 0, sync.stderr)
        self.assertIn("Synced SPEC S01", sync.stdout)
        self.assertIn("Synced DEC D01", sync.stdout)
        self.assertIn("Synced REQ R01", sync.stdout)

        verify = self.run_cli("verify-links")
        self.assertEqual(verify.returncode, 0, verify.stderr)

    def test_verify_links_and_sync_reject_duplicate_ids_and_cycles(self):
        (self.artifacts / "REQUIREMENTS.md").write_text(
            "# Requirements\n\n### Slice\n\n"
            "- [ ] R01: One\n  - Verify: true\n"
            "- [ ] R01: Duplicate\n  - Verify: true\n",
            encoding="utf-8",
        )
        (self.artifacts / "TASKS.md").write_text(
            "# Tasks\n\n### Slice\n\n"
            "- [ ] T01 [S01] [T02]: Cycle A\n  - Verify: true\n"
            "- [ ] T02 [S01] [T01]: Cycle B\n  - Verify: true\n",
            encoding="utf-8",
        )

        verify = self.run_cli("verify-links")
        self.assertNotEqual(verify.returncode, 0)
        self.assertIn("Duplicate ID: R01", verify.stderr)
        self.assertIn("Dependency cycle:", verify.stderr)

        sync = self.run_cli("sync")
        self.assertNotEqual(sync.returncode, 0)
        self.assertIn("Duplicate ID", sync.stderr)

    def test_reformat_splits_inline_verify_only_outside_fences(self):
        md = self.artifacts / "TASKS.md"
        md.write_text(
            "# Tasks\n\n### Slice\n\n"
            "```markdown\n- [ ] T99 [S01]: Inside fence | Verify: keep inline\n```\n\n"
            "- [ ] T01 [S01]: Outside fence | Verify: echo ok\n",
            encoding="utf-8",
        )

        ref = self.run_cli("reformat", str(md))
        self.assertEqual(ref.returncode, 0, ref.stderr)
        out = md.read_text(encoding="utf-8")
        self.assertIn("- [ ] T99 [S01]: Inside fence | Verify: keep inline", out)
        self.assertIn("- [ ] T01 [S01]: Outside fence\n  - Verify: echo ok", out)

    def test_undrawn_specs_lists_specs_without_ledgers(self):
        (self.artifacts / "REQUIREMENTS.md").write_text(
            "# Requirements\n\n### Slice\n\n"
            "- [ ] R01: Deliver slice\n  - Verify: echo req\n",
            encoding="utf-8",
        )
        (self.artifacts / "DECISIONS.md").write_text(
            "# Decisions\n\n### System Shape\n\n"
            "- [ ] D01 [R01]: Single process\n",
            encoding="utf-8",
        )
        (self.artifacts / "SPECS.md").write_text(
            "# Specs\n\n### Slice\n\n#### System Shape\n\n"
            "- [ ] S01 [R01, D01]: Handle request cleanly\n"
            "  - Verify: echo spec\n",
            encoding="utf-8",
        )

        undrawn = self.run_cli("undrawn-specs")
        self.assertEqual(undrawn.returncode, 0, undrawn.stderr)
        self.assertIn("S01", undrawn.stdout)

        verify = self.run_cli("verify-links")
        self.assertEqual(verify.returncode, 0, verify.stderr)
        self.assertIn("Missing Ledger", verify.stderr)

        self.write_ledger("S01", "C01")
        specs = self.artifacts / "SPECS.md"
        specs.write_text(
            specs.read_text(encoding="utf-8").replace(
                "  - Verify: echo spec\n",
                "  - Verify: echo spec\n  - Ledger: tests/S01.md\n",
            ),
            encoding="utf-8",
        )

        undrawn = self.run_cli("undrawn-specs")
        self.assertEqual(undrawn.returncode, 0, undrawn.stderr)
        self.assertEqual(undrawn.stdout.strip(), "NONE")

        verify = self.run_cli("verify-links")
        self.assertEqual(verify.returncode, 0, verify.stderr)

    def test_verify_links_validates_ledgers_case_refs_and_task_details(self):
        (self.artifacts / "REQUIREMENTS.md").write_text(
            "# Requirements\n\n### Slice\n\n"
            "- [ ] R01: Deliver slice\n  - Verify: echo req\n",
            encoding="utf-8",
        )
        (self.artifacts / "DECISIONS.md").write_text(
            "# Decisions\n\n### System Shape\n\n"
            "- [ ] D01 [R01]: Single process\n",
            encoding="utf-8",
        )
        (self.artifacts / "SPECS.md").write_text(
            "# Specs\n\n### Slice\n\n#### System Shape\n\n"
            "- [ ] S01 [R01, D01]: Handle request cleanly\n"
            "  - Verify: echo spec\n"
            "  - Ledger: tests/S01.md\n",
            encoding="utf-8",
        )
        (self.artifacts / "TASKS.md").write_text(
            "# Tasks\n\n### Slice\n\n"
            "- [ ] T01 [S01]: Draw cases green\n"
            "  - Verify: echo task\n"
            "  - Detail: tasks/T01.md\n"
            "  - Cases: C01, C02\n",
            encoding="utf-8",
        )
        self.write_ledger("S01", "C01", "C02")
        self.write_task_detail("T01")

        verify = self.run_cli("verify-links")
        self.assertEqual(verify.returncode, 0, verify.stderr)
        self.assertEqual(verify.stdout.strip(), "OK")

        self.write_ledger("S01", "C01", "C02", "C03")
        verify = self.run_cli("verify-links")
        self.assertNotEqual(verify.returncode, 0)
        self.assertIn("Unreferenced case: C03", verify.stderr)

        self.write_ledger("S01", "C01", "C02")
        tasks = self.artifacts / "TASKS.md"
        tasks.write_text(
            tasks.read_text(encoding="utf-8").replace("C02", "C99"),
            encoding="utf-8",
        )
        verify = self.run_cli("verify-links")
        self.assertNotEqual(verify.returncode, 0)
        self.assertIn("Unknown case: C99", verify.stderr)

        (self.artifacts / "tasks" / "T01.md").unlink()
        verify = self.run_cli("verify-links")
        self.assertNotEqual(verify.returncode, 0)
        self.assertIn("Missing Task Detail file", verify.stderr)

    def test_skill_wrappers_exist_for_all_scripted_skills_and_omit_curl_fallback(self):
        for skill in SCRIPTED_SKILLS:
            wrapper = REPO_ROOT / "skills" / skill / "scripts" / "iridescent-artifacts"
            self.assertTrue(wrapper.is_file(), f"missing wrapper: {wrapper}")
            self.assertTrue(os.access(wrapper, os.X_OK), f"wrapper not executable: {wrapper}")
            text = wrapper.read_text(encoding="utf-8")
            self.assertNotIn("curl", text)
            self.assertNotIn("artifacts.py", text)

            res = subprocess.run(
                [str(wrapper), "status"],
                cwd=self.workspace,
                env={**os.environ, "ARTIFACTS_DIR": str(self.artifacts)},
                text=True,
                capture_output=True,
            )
            self.assertEqual(res.returncode, 0, f"{skill}: {res.stderr}")
            self.assertIn("CONTEXT:present", res.stdout)


if __name__ == "__main__":
    unittest.main()
