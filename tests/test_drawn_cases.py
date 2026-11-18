from pathlib import Path
import unittest

try:
    from draw_support import reference_text, run_cli, section, skill_text, workspace, write_graph
except ModuleNotFoundError:
    from tests.draw_support import reference_text, run_cli, section, skill_text, workspace, write_graph

RULES = "Rules"
WORKFLOW = "Workflow"


class S01Tests(unittest.TestCase):
    def test_c01_tool_call_directive(self):
        for phase in ("brainstorm", "design", "specify", "plan"):
            assert "structured question tool" in section(skill_text(phase), RULES)

    def test_c02_concrete_options(self):
        import re
        for phase in ("brainstorm", "design", "specify", "plan"):
            assert re.search(r"2-4\s+(?:concrete\s+)?options", skill_text(phase))

    def test_c03_recommended_answer(self):
        import re
        for phase in ("brainstorm", "design", "specify", "plan"):
            assert re.search(r"one\s+recommended\s+answer|a\s+recommendation", skill_text(phase))

    def test_c04_consequence_direction(self):
        import re
        for phase in ("brainstorm", "design", "specify", "plan"):
            assert re.search(r"one-line consequence per answer|answer consequences", skill_text(phase))

    def test_c05_blocking_unanswered_forks(self):
        import re
        for phase in ("brainstorm", "design", "specify", "plan"):
            assert re.search(r"block\s+(on|until|before)", skill_text(phase))

    def test_c06_questions_before_design_records(self):
        loop = reference_text("how-to-iridescent", "loop.md")
        assert "questions" in loop and "design records" in loop
        assert loop.index("questions") < loop.index("design records")


class S02Tests(unittest.TestCase):
    def test_c01_plan_checks_undrawn(self):
        assert "undrawn-specs" in section(skill_text("plan"), WORKFLOW)

    def test_c02_plan_states_undrawn_gate(self):
        workflow = section(skill_text("plan"), WORKFLOW)
        assert workflow.index("undrawn-specs") < workflow.index("unconverted-specs")

    def test_c03_cli_exposes_next_cases(self):
        result = run_cli()
        assert result.returncode != 0
        assert "next-cases" in result.stderr

    def test_c04_cli_lists_next_cases(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts, cases="C01, C02")
            result = run_cli("next-cases", cwd=root)
            assert result.returncode == 0, result.stderr
            assert "T01 C01\nT01 C02" in result.stdout

    def test_c05_loop_states_case_gate(self):
        loop = reference_text("how-to-iridescent", "loop.md").replace(chr(96), "")
        assert "red cases before tasks" in loop
        assert loop.index("draw skill") < loop.index("plan skill")

    def test_c06_plan_verify_checks_undrawn(self):
        assert "undrawn-specs" in section(skill_text("plan"), "Rules")


class S03Tests(unittest.TestCase):
    def test_c01_rules_mark_authoritative_records(self):
        rules = reference_text("doctor-iridescent", "artifacts.md")
        assert "authoritative" in rules and "root records" in rules

    def test_c02_doctor_handles_detail_files(self):
        assert "detail files" in section(skill_text("doctor-iridescent"), WORKFLOW)

    def test_c03_cli_detects_orphan_details(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts, extra_detail=True)
            result = run_cli("verify-links", cwd=root)
            assert result.returncode == 0, result.stderr
            assert "orphan detail file: tasks/T99.md" in result.stderr

    def test_c04_cli_validates_details(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts, detail=None)
            result = run_cli("verify-links", cwd=root)
            assert result.returncode != 0
            assert "Missing Detail: T01" in result.stderr

    def test_c05_cli_scopes_case_ids_to_ledgers(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts)
            specs = (artifacts / "SPECS.md").read_text(encoding="utf-8")
            specs += "- [ ] S02 [R01, D01]: Second spec\n  - Verify: echo spec2\n  - Ledger: tests/S02.md\n"
            (artifacts / "SPECS.md").write_text(specs, encoding="utf-8")
            tasks = (artifacts / "TASKS.md").read_text(encoding="utf-8")
            tasks += "- [ ] T02 [S02]: Second task\n  - Verify: echo task2\n  - Detail: tasks/T02.md\n  - Cases: C01\n"
            (artifacts / "TASKS.md").write_text(tasks, encoding="utf-8")
            (artifacts / "tests" / "S02.md").write_text("# Test Ledger: S02\n\n### C01: Case\n- Seam: test\n- Red: true\n", encoding="utf-8")
            (artifacts / "tasks" / "T02.md").write_text("# Task Detail: T02\n", encoding="utf-8")
            result = run_cli("verify-links", cwd=root)
            assert result.returncode == 0, result.stderr
            assert "Duplicate case ID across ledgers" not in result.stderr

    def test_c06_cli_traces_ledger_links(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts)
            result = run_cli("trace", "S01", cwd=root)
            assert result.returncode == 0, result.stderr
            assert "tests/S01.md" in result.stdout


class S04Tests(unittest.TestCase):
    def test_c01_cli_detects_duplicate_cases_field(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts)
            tasks = artifacts / "TASKS.md"
            tasks.write_text(tasks.read_text(encoding="utf-8") + "  - Cases: C02\n", encoding="utf-8")
            result = run_cli("verify-links", cwd=root)
            assert result.returncode != 0
            assert "Duplicate Cases field" in result.stderr

    def test_c02_cli_detects_invalid_case_id(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts, cases="X01")
            result = run_cli("verify-links", cwd=root)
            assert result.returncode != 0
            assert "Invalid case ID" in result.stderr

    def test_c03_plan_declares_field_contract(self):
        assert "detail fields are contract" in section(skill_text("plan"), RULES)

    def test_c04_cli_checks_field_order(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts)
            tasks = artifacts / "TASKS.md"
            text = tasks.read_text(encoding="utf-8")
            tasks.write_text(
                text.replace(
                    "  - Detail: tasks/T01.md\n  - Cases: C01\n",
                    "  - Cases: C01\n  - Detail: tasks/T01.md\n",
                ),
                encoding="utf-8",
            )
            result = run_cli("verify-links", cwd=root)
            assert result.returncode != 0
            assert "Cases field order" in result.stderr

    def test_c05_cli_checks_detail_extension(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts, detail="tasks/T01.txt")
            result = run_cli("verify-links", cwd=root)
            assert result.returncode != 0
            assert "Wrong path for detail" in result.stderr

    def test_c06_rules_describe_detail_fields(self):
        rules = reference_text("doctor-iridescent", "artifacts.md")
        assert "Detail fields" in rules


class S05Tests(unittest.TestCase):
    def test_c01_draw_scope_states_focus(self):
        assert "one case focused on one observable behavior" in section(skill_text("draw"), RULES)

    def test_c02_draw_scope_names_red_command(self):
        assert "Red command" in section(skill_text("draw"), RULES)

    def test_c03_cli_checks_missing_red(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts, ledger_text="# Test Ledger: S01\n\n### C01: Case\n- Seam: test\n")
            result = run_cli("verify-links", cwd=root)
            assert result.returncode != 0
            assert "Missing Red: C01" in result.stderr

    def test_c04_cli_checks_missing_seam(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts, ledger_text="# Test Ledger: S01\n\n### C01: Case\n- Red: true\n")
            result = run_cli("verify-links", cwd=root)
            assert result.returncode != 0
            assert "Missing Seam: C01" in result.stderr

    def test_c05_cli_checks_duplicate_case_ids(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts, ledger_text="# Test Ledger: S01\n\n### C01: One\n- Seam: test\n- Red: true\n\n### C01: Two\n- Seam: test\n- Red: true\n")
            result = run_cli("verify-links", cwd=root)
            assert result.returncode != 0
            assert "Duplicate case ID in ledger" in result.stderr

    def test_c06_cases_defines_red_focus(self):
        assert "one observable behavior per Red command" in reference_text("draw", "cases.md")


class S06Tests(unittest.TestCase):
    def test_c01_doctor_handles_detail_files(self):
        assert "detail files" in section(skill_text("doctor-iridescent"), WORKFLOW)

    def test_c02_cli_detects_orphan_detail_file(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts, extra_detail=True)
            result = run_cli("verify-links", cwd=root)
            assert "orphan detail file" in result.stderr

    def test_c03_cli_reports_placement_drift(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts, detail="bad/T01.md")
            result = run_cli("verify-links", cwd=root)
            assert result.returncode != 0
            assert "Wrong path for detail" in result.stderr

    def test_c04_rules_require_verify_links(self):
        rules = reference_text("doctor-iridescent", "artifacts.md")
        assert "verify-links" in rules

    def test_c05_cli_reports_missing_detail_file(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts)
            (artifacts / "tasks" / "T01.md").unlink()
            result = run_cli("verify-links", cwd=root)
            assert result.returncode != 0
            assert "Missing Task Detail file" in result.stderr

    def test_c06_architecture_blocks_on_placement(self):
        arch = (Path(__file__).resolve().parent.parent / ".artifacts/ARCHITECTURE.md").read_text(encoding="utf-8")
        assert "placement failures that block progress" in arch
