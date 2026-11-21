from contextlib import contextmanager
from pathlib import Path
import subprocess
import tempfile

REPO_ROOT = Path(__file__).resolve().parent.parent
CLI_PATH = REPO_ROOT / "scripts" / "iridescent-artifacts"


def skill_text(name: str) -> str:
    return (REPO_ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")


def reference_text(name: str, rel: str) -> str:
    return (REPO_ROOT / "skills" / name / "references" / rel).read_text(encoding="utf-8")


def section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    if marker not in text:
        return ""
    rest = text.split(marker, 1)[1]
    next_heading = rest.find("\n## ")
    return rest if next_heading < 0 else rest[:next_heading]


def run_cli(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", "-B", str(CLI_PATH), *args],
        cwd=cwd or REPO_ROOT,
        text=True,
        capture_output=True,
    )


@contextmanager
def workspace():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        artifacts = root / ".artifacts"
        artifacts.mkdir()
        (artifacts / "CONTEXT.md").write_text("# Context\n", encoding="utf-8")
        (artifacts / "ARCHITECTURE.md").write_text(
            "# Architecture\n\n## Skill Contracts\n\nContract slice.\n",
            encoding="utf-8",
        )
        yield root, artifacts


def default_task_detail() -> str:
    return (
        "# Task Detail: T01\n\n"
        "## Steps\n\n"
        "- Step: reproduce the case.\n"
        "- Step: make the smallest passing change.\n\n"
        "## Notes\n\n"
        "- none\n\n"
        "## Risk\n\n"
        "- low\n"
    )


def write_graph(
    artifacts: Path,
    *,
    cases: str = "C01",
    detail: str = "tasks/T01.md",
    extra_detail: bool = False,
) -> None:
    root = artifacts.parent
    (artifacts / "REQUIREMENTS.md").write_text(
        "# Requirements\n\n## Skill Contracts\n\n"
        "- [ ] R01 [D01]: Deliver slice\n  - Verify: echo req\n",
        encoding="utf-8",
    )
    (artifacts / "DECISIONS.md").write_text(
        "# Decisions\n\n## Skill Contracts\n\n"
        "- [ ] D01: Single process\n",
        encoding="utf-8",
    )
    (artifacts / "SPECS.md").write_text(
        "# Specs\n\n## Skill Contracts\n\n"
        "- [ ] S01 [R01]: Handle request\n"
        "  - Verify: echo spec\n"
        "  - Tests: tests/test_s01.py\n",
        encoding="utf-8",
    )
    cases_bracket = f" [{cases}]" if cases else ""
    (artifacts / "TASKS.md").write_text(
        "# Tasks\n\n## Skill Contracts\n\n"
        f"- [ ] T01 [S01]{cases_bracket}: Make green\n"
        "  - Verify: echo task\n",
        encoding="utf-8",
    )

    tests_dir = root / "tests"
    tests_dir.mkdir(exist_ok=True)
    case_lines = [f"# {case_id}" for case_id in cases.split(",") if case_id.strip()]
    (tests_dir / "test_s01.py").write_text(
        "\n".join(case_lines) + "\n", encoding="utf-8"
    )

    detail_path = artifacts / (detail or "tasks/T01.md")
    detail_path.parent.mkdir(parents=True, exist_ok=True)
    detail_path.write_text(default_task_detail(), encoding="utf-8")
    if extra_detail:
        (artifacts / "tasks" / "T99.md").write_text("# Task Detail: T99\n", encoding="utf-8")
