from pathlib import Path
import unittest

try:
    from draw_support import reference_text, run_cli, section, skill_text, workspace, write_graph
except ModuleNotFoundError:
    from tests.draw_support import reference_text, run_cli, section, skill_text, workspace, write_graph

RULES = "Rules"
WORKFLOW = "Workflow"


class QuestionProtocolTests(unittest.TestCase):
    def test_tool_call_directive(self):
        for phase in ("design", "specify", "draw"):
            assert "structured question tool" in section(skill_text(phase), RULES)

    def test_concrete_options(self):
        import re
        for phase in ("design", "specify", "draw"):
            assert re.search(r"2-4\s+(?:concrete\s+)?options", skill_text(phase))

    def test_recommended_answer(self):
        import re
        for phase in ("design", "specify", "draw"):
            assert re.search(r"one\s+recommended\s+answer|a\s+recommendation", skill_text(phase))

    def test_consequence_direction(self):
        import re
        for phase in ("design", "specify", "draw"):
            assert re.search(r"one-line consequence per answer|answer consequences", skill_text(phase))

    def test_blocking_unanswered_forks(self):
        import re
        for phase in ("design", "specify", "draw"):
            assert re.search(r"block\s+(on|until|before)", skill_text(phase))

    def test_questions_before_design_records(self):
        loop = reference_text("how-to-iridescent", "loop.md")
        assert "questions" in loop and "design records" in loop
        assert loop.index("questions") < loop.index("design records")


class CaseReadinessTests(unittest.TestCase):
    def test_plan_checks_undrawn(self):
        assert "undrawn-specs" in section(skill_text("plan"), WORKFLOW)

    def test_plan_states_undrawn_gate(self):
        workflow = section(skill_text("plan"), WORKFLOW)
        assert workflow.index("undrawn-specs") < workflow.index("unconverted-specs")

    def test_loop_states_case_gate(self):
        loop = reference_text("how-to-iridescent", "loop.md").replace(chr(96), "")
        assert "red tests before tasks" in loop
        assert loop.index("draw skill") < loop.index("plan skill")

    def test_plan_verify_checks_undrawn(self):
        assert "undrawn-specs" in section(skill_text("plan"), "Verify")


class DetailAuthorityTests(unittest.TestCase):
    def test_rules_mark_authoritative_records(self):
        rules = reference_text("doctor-iridescent", "artifacts.md")
        assert "authoritative" in rules and "root records" in rules

    def test_doctor_handles_detail_files(self):
        assert "detail files" in section(skill_text("doctor-iridescent"), WORKFLOW)

    def test_cli_traces_test_links(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts)
            result = run_cli("trace", "S01", cwd=root)
            assert result.returncode == 0, result.stderr
            assert "tests/test_s01.py" in result.stdout


class DetailFieldTests(unittest.TestCase):
    def test_plan_declares_field_contract(self):
        assert "single verification source" in section(skill_text("plan"), RULES)

    def test_rules_describe_detail_fields(self):
        rules = reference_text("doctor-iridescent", "artifacts.md")
        assert "Detail fields" in rules


class TestProofTests(unittest.TestCase):
    def test_draw_scope_states_focus(self):
        assert "one test focused on one observable behavior" in section(skill_text("draw"), RULES)

    def test_draw_names_spec_verify_command(self):
        assert "spec `Verify:` command fails" in section(skill_text("draw"), "Verify")

    def test_draw_keeps_trace_ids_out_of_real_test_files(self):
        rules = section(skill_text("draw"), RULES)
        assert "trace IDs" in rules
        assert "real test files" in rules

    def test_cli_accepts_id_free_test_files(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts)
            result = run_cli("verify-links", cwd=root)
            assert result.returncode == 0, result.stderr
            assert result.stdout.strip() == "OK"

    def test_cli_rejects_missing_test_file(self):
        with workspace() as (root, artifacts):
            write_graph(artifacts)
            (root / "tests" / "test_s01.py").unlink()
            result = run_cli("verify-links", cwd=root)
            assert result.returncode != 0
            assert "Missing test file" in result.stderr


class PlacementTests(unittest.TestCase):
    def test_doctor_handles_detail_files(self):
        assert "detail files" in section(skill_text("doctor-iridescent"), WORKFLOW)

    def test_rules_require_verify_links(self):
        rules = reference_text("doctor-iridescent", "artifacts.md")
        assert "verify-links" in rules

    def test_architecture_blocks_on_placement(self):
        arch = (Path(__file__).resolve().parent.parent / ".artifacts/ARCHITECTURE.md").read_text(encoding="utf-8")
        assert "placement failures that block progress" in arch
