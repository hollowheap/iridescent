from pathlib import Path
import re
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"


def read_skill(name: str) -> str:
    return (SKILLS_DIR / name / "SKILL.md").read_text(encoding="utf-8")


def read_ref(name: str, rel: str) -> str:
    return (SKILLS_DIR / name / "references" / rel).read_text(encoding="utf-8")


class LifecycleConsistencyTests(unittest.TestCase):
    def test_review_read_only_and_severity_discipline(self):
        simplicity = read_ref("review", "simplicity.md").lower()
        review = read_skill("review").lower()
        robust = read_ref("review", "robust.md").lower()

        self.assertNotIn("invert one condition", simplicity)
        self.assertNotIn("update `.artifacts/architecture.md`", robust)
        self.assertNotIn("updates `.artifacts/architecture.md`", review)
        self.assertIn("read-only", review)
        self.assertIn("severity", review)
        self.assertIn("correctness", review)
        self.assertIn("security", review)
        self.assertRegex(review + "\n" + robust, r"drop unrun|drop speculative")

    def test_portable_roles_and_question_controls(self):
        forbidden = re.compile(r"\b(?:(?i:Code Reviewer|Researcher|engineer)|Scout)\b|multi:\s*true")
        for path in sorted(SKILLS_DIR.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            self.assertIsNone(forbidden.search(text), f"non-portable term in {path.relative_to(REPO_ROOT)}")

    def test_grilling_ownership_and_context_only_brainstorm(self):
        brainstorm = read_skill("brainstorm").lower()
        self.assertNotIn("structured question tool", brainstorm)
        self.assertIn("unresolved", brainstorm)
        for phase in ("design", "specify", "draw"):
            text = read_skill(phase).lower()
            self.assertIn("structured question tool", text)
            self.assertRegex(text, r"block\s+(on|until|before)")

    def test_phase_facts_scoping_and_plan_detail_contract(self):
        for phase in ("design", "specify", "plan"):
            text = read_skill(phase).lower()
            self.assertRegex(text, r"facts.*repo|discover.*repo|resolve facts")

        draw = read_skill("draw").lower()
        self.assertRegex(draw, r"shared seam.*provider|when.*shared seam")

        plan = read_skill("plan")
        self.assertNotIn("Edit only `.artifacts/TASKS.md`", plan)
        self.assertIn("tasks/<Txx>.md", plan)
        self.assertRegex(plan.lower(), r"refactor.*feature|separate.*refactor")

        update = read_skill("update").lower()
        self.assertIn("existing persistent review", update)
        self.assertRegex(update, r"preserve superseded|retain superseded")

    def test_review_simplicity_and_exception_ladder(self):
        simplicity = read_ref("review", "simplicity.md").lower()
        self.assertNotIn("on explicit request", simplicity)
        self.assertIn("chesterton", simplicity)
        self.assertIn("dead code", simplicity)
        self.assertRegex(simplicity, r"preserve.*outputs|behavior preservation")
        self.assertRegex(simplicity, r"separate refactor|refactor.*feature")
        self.assertIn("expiry", simplicity)
        self.assertIn("human approval", simplicity)


class SkillFormatTests(unittest.TestCase):
    @staticmethod
    def _workflow_and_rule_lines(text: str) -> list[str]:
        lines: list[str] = []
        in_section = False
        for raw in text.splitlines():
            if raw.startswith("## "):
                in_section = raw in ("## Workflow", "## Rules")
                continue
            if not in_section:
                continue
            stripped = raw.strip()
            if not stripped or stripped.startswith("- Verify:"):
                continue
            if re.match(r"^(?:-|\d+\.)\s+", stripped):
                lines.append(stripped)
        return lines

    def test_workflow_and_rules_avoid_mega_sentences(self):
        offenders: list[str] = []
        for path in sorted(SKILLS_DIR.glob("*/SKILL.md")):
            for line in self._workflow_and_rule_lines(path.read_text(encoding="utf-8")):
                if len(line.split()) > 30:
                    offenders.append(f"{path.parent.name}: {line}")
        self.assertEqual(offenders, [], f"over-folded lines (>30 words): {offenders}")

    def test_workflow_and_rules_avoid_semicolon_chains(self):
        offenders: list[str] = []
        for path in sorted(SKILLS_DIR.glob("*/SKILL.md")):
            for line in self._workflow_and_rule_lines(path.read_text(encoding="utf-8")):
                no_code = re.sub(r"`[^`]+`", "", line)
                if no_code.count(";") >= 2:
                    offenders.append(f"{path.parent.name}: {line}")
        self.assertEqual(offenders, [], f"semicolon chains (>=2): {offenders}")

    def test_skill_structure_and_implement_routing(self):
        for path in sorted(SKILLS_DIR.glob("*/SKILL.md")):
            text = path.read_text(encoding="utf-8")
            for marker in ("name:", "description:", "## Scope", "## Workflow", "## Rules", "- Verify:"):
                self.assertIn(marker, text, f"missing {marker} in {path}")
            workflow = text.split("## Workflow", 1)[1].split("\n## ", 1)[0]
            steps = re.findall(r"^\d+\.\s+", workflow, flags=re.MULTILINE)
            self.assertLessEqual(len(steps), 7, f"too many workflow steps in {path}")

        implement = read_skill("implement")
        self.assertIn("references/boundaries.md", implement)
        self.assertNotIn("Lenses:", implement)


class ImplementationGuidanceTests(unittest.TestCase):
    def test_principles_mirrors_simplicity_preservation_and_slice_failures(self):
        principles = read_ref("implement", "principles.md").lower()
        for term in (
            "1:1",
            "single-adapter",
            "speculative",
            "duplicate",
            "deletion test",
            "chesterton",
            "dead code",
            "outputs",
            "side effects",
            "ordering",
            "deep module",
            "in memory",
            "partial failure",
            "concurrency",
            "fail safe",
        ):
            self.assertIn(term, principles, f"missing '{term}' in implement/references/principles.md")
        self.assertRegex(principles, r"separate.*refactor|refactor.*feature")
        self.assertRegex(principles, r"inline|collapse|canonical")

    def test_boundaries_mirrors_all_five_review_domains(self):
        boundaries_path = SKILLS_DIR / "implement" / "references" / "boundaries.md"
        self.assertTrue(boundaries_path.is_file(), "missing implement/references/boundaries.md")
        text = boundaries_path.read_text(encoding="utf-8").lower()
        for term in (
            "idempotency",
            "status code",
            "timeout",
            "envelope",
            "lock",
            "backfill",
            "transaction",
            "expand-and-contract",
            "least privilege",
            "stack trace",
            "operation",
            "exposure",
            "measure",
            "blocking",
            "startup",
            "n+1",
            "keyboard",
            "contrast",
            "touch target",
            "reduced-motion",
        ):
            self.assertIn(term, text, f"missing '{term}' in implement/references/boundaries.md")

    def test_tdd_runs_drawn_tests_and_draw_owns_quality(self):
        tdd = read_ref("implement", "tdd.md").lower()
        draw = read_skill("draw").lower()
        self.assertIn("drawn", tdd)
        self.assertIn("route to", tdd)
        self.assertIn("invert", tdd)
        self.assertIn("restore", tdd)
        for term in ("honest", "provider", "consumer", "cross-seam", "never weaken"):
            self.assertIn(term, draw)

    def test_implement_workflow_enforces_pre_handoff_self_audit(self):
        implement = read_skill("implement").lower()
        self.assertIn("self-audit", implement)
        self.assertIn("git diff", implement)
        self.assertIn("boundaries.md", implement)
        self.assertNotIn("lens ledger", implement)
        self.assertIn("quick path", implement)


if __name__ == "__main__":
    unittest.main()
