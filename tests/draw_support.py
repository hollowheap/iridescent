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
            "# Architecture\n\n"
            "## System Shape\n\nShape.\n\n"
            "## Module Seams\n\nSeams.\n\n"
            "## Framework & Library Choices\n\nChoices.\n\n"
            "## Data & Contracts\n\nContracts.\n\n"
            "## Operations & Security\n\nOps.\n",
            encoding="utf-8",
        )
        yield root, artifacts


def default_ledger(case_ids: str) -> str:
    lines = ["# Test Ledger: S01", ""]
    for case_id in [c.strip() for c in case_ids.split(",") if c.strip()]:
        lines.extend([f"### {case_id}: Case", "- Seam: test", "- Red: true", ""])
    return "\n".join(lines)


def write_graph(
    artifacts: Path,
    *,
    cases: str = "C01",
    detail: str = "tasks/T01.md",
    ledger_text: str | None = None,
    ledger_link: bool = True,
    extra_detail: bool = False,
) -> None:
    (artifacts / "REQUIREMENTS.md").write_text(
        "# Requirements\n\n### Slice\n\n"
        "- [ ] R01: Deliver slice\n  - Verify: echo req\n",
        encoding="utf-8",
    )
    (artifacts / "DECISIONS.md").write_text(
        "# Decisions\n\n### System Shape\n\n"
        "- [ ] D01 [R01]: Single process\n",
        encoding="utf-8",
    )
    spec = (
        "# Specs\n\n### Slice\n\n#### System Shape\n\n"
        "- [ ] S01 [R01, D01]: Handle request\n"
        "  - Verify: echo spec\n"
    )
    if ledger_link:
        spec += "  - Ledger: tests/S01.md\n"
    (artifacts / "SPECS.md").write_text(spec, encoding="utf-8")

    task = "# Tasks\n\n### Slice\n\n- [ ] T01 [S01]: Make green\n  - Verify: echo task\n"
    if detail is not None:
        task += f"  - Detail: {detail}\n"
    if cases is not None:
        task += f"  - Cases: {cases}\n"
    (artifacts / "TASKS.md").write_text(task, encoding="utf-8")

    tests_dir = artifacts / "tests"
    tests_dir.mkdir(exist_ok=True)
    (tests_dir / "S01.md").write_text(
        ledger_text or default_ledger(cases or "C01"), encoding="utf-8"
    )

    tasks_dir = artifacts / "tasks"
    tasks_dir.mkdir(exist_ok=True)
    (tasks_dir / "T01.md").write_text("# Task Detail: T01\n", encoding="utf-8")
    if extra_detail:
        (tasks_dir / "T99.md").write_text("# Task Detail: T99\n", encoding="utf-8")
