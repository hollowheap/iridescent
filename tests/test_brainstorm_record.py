from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent
DOC = ROOT / ".artifacts" / "BRAINSTORM.md"


class BrainstormRecordTests(unittest.TestCase):
    def text(self):
        return DOC.read_text(encoding="utf-8")

    def section(self, name):
        text = self.text()
        marker = "## " + name
        if marker not in text:
            return ""
        rest = text.split(marker, 1)[1]
        next_heading = rest.find("\n## ")
        return rest if next_heading < 0 else rest[:next_heading]

    def test_destination_names_user_change(self):
        self.assertIn("user", self.section("Destination").lower())

    def test_facts_cite_local_evidence(self):
        self.assertIn(".artifacts/", self.section("Facts"))

    def test_options_name_design(self):
        self.assertIn("`design`", self.section("Options"))

    def test_no_question_fields(self):
        text = self.text().lower()
        self.assertNotIn("## approval", text)
        self.assertNotIn("structured question", text)

    def test_no_fixed_comparison_sections(self):
        text = self.text()
        self.assertNotIn("## Archetypes", text)
        self.assertNotIn("## Trade-offs", text)

    def test_no_stale_markers(self):
        text = self.text().lower()
        self.assertNotIn("supersedes", text)
        self.assertNotIn("stale", text)


if __name__ == "__main__":
    unittest.main()
