#!/usr/bin/env python3
"""Structural validator for the socratic-elenchus skill.

Checks that the repository honours the skill contract it claims to follow:
frontmatter shape, reference resolution, example discipline, and the
invariants that the design depends on. No third-party dependencies.

Usage:
    python scripts/validate.py [--root .] [--json]
Exit code 0 = all checks pass, 1 = at least one failure.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)
MD_LINK = re.compile(r"\]\(([^)#]+?)(?:#[^)]*)?\)")
CJK = re.compile(r"[\u4e00-\u9fff]")

TRIGGER_HINTS = [
    "帮我理清楚",
    "我有点纠结",
    "站不站得住",
    "苏格拉底",
    "help me think this through",
    "ask me socratically",
    "does this claim hold up",
]

FORBIDDEN_IN_EXAMPLES = ["所以你是错的", "你的定义是错的", "so you are wrong"]


@dataclass
class Check:
    name: str
    ok: bool
    detail: str = ""


@dataclass
class Report:
    checks: list[Check] = field(default_factory=list)

    def add(self, name: str, ok: bool, detail: str = "") -> None:
        self.checks.append(Check(name, ok, detail))

    @property
    def failed(self) -> list[Check]:
        return [c for c in self.checks if not c.ok]


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = FRONTMATTER.match(text)
    if not match:
        return None
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if not sep:
            return None
        data[key.strip()] = value.strip().strip("'\"")
    return data


def check_frontmatter(report: Report, root: Path) -> dict[str, str] | None:
    skill = root / "SKILL.md"
    if not skill.exists():
        report.add("SKILL.md exists", False, "missing")
        return None
    text = skill.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    report.add("SKILL.md frontmatter parses", meta is not None)
    if meta is None:
        return None

    name = meta.get("name", "")
    report.add("name is kebab-case", bool(KEBAB.match(name)), name or "empty")
    report.add("name matches directory", name == root.name, f"{name} vs {root.name}")
    report.add("description present", bool(meta.get("description")), "")
    report.add("whenToUse present", bool(meta.get("whenToUse")), "")

    desc = meta.get("description", "")
    report.add("description <= 500 chars", len(desc) <= 500, f"{len(desc)} chars")
    hits = [t for t in TRIGGER_HINTS if t.lower() in desc.lower()]
    report.add("description carries trigger phrases", len(hits) >= 2, f"{len(hits)} hits")

    body_lines = len(text.splitlines())
    report.add("SKILL.md <= 160 lines", body_lines <= 160, f"{body_lines} lines")
    return meta


def check_bilingual(report: Report, root: Path, meta: dict[str, str]) -> None:
    en = root / "SKILL.en.md"
    report.add("SKILL.en.md exists", en.exists())
    if not en.exists():
        return
    text = en.read_text(encoding="utf-8")
    en_meta = parse_frontmatter(text)
    report.add("SKILL.en.md frontmatter parses", en_meta is not None)
    if en_meta:
        report.add("SKILL.en.md name matches", en_meta.get("name") == meta.get("name"))
        report.add(
            "SKILL.en.md description <= 500 chars",
            len(en_meta.get("description", "")) <= 500,
            f"{len(en_meta.get('description', ''))} chars",
        )

    zh_h2 = len(re.findall(r"^## ", (root / "SKILL.md").read_text(encoding="utf-8"), re.M))
    en_h2 = len(re.findall(r"^## ", text, re.M))
    report.add("bilingual section count within 2", abs(zh_h2 - en_h2) <= 2, f"zh={zh_h2} en={en_h2}")


def check_references(report: Report, root: Path) -> None:
    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    refs = sorted(set(re.findall(r"references/[A-Za-z0-9._-]+\.md", skill_text)))
    report.add("SKILL.md cites references", len(refs) >= 2, f"{len(refs)} cited")
    for ref in refs:
        report.add(f"cited reference exists: {ref}", (root / ref).exists())

    ref_dir = root / "references"
    if ref_dir.is_dir():
        for path in sorted(ref_dir.glob("*.md")):
            rel = path.relative_to(root).as_posix()
            report.add(f"reference is cited: {rel}", rel in skill_text)


def check_examples(report: Report, root: Path) -> None:
    for sub in ("examples", "examples/en"):
        directory = root / sub
        if not directory.is_dir():
            continue
        files = sorted(directory.glob("*.md"))
        report.add(f"{sub} has files", bool(files), f"{len(files)} files")
        if not files:
            continue
        for path in files:
            text = path.read_text(encoding="utf-8")
            rel = path.relative_to(root).as_posix()

            if sub == "examples":
                speaker = re.compile(r"^\*\*(?:教练|用户)\*\*：(.+)$")
                closing_marker = "收束"
                takeaway = "这段示范了什么"
            else:
                speaker = re.compile(r"^\*\*(?:Coach|User)\*\*:\s*(.+)$")
                closing_marker = "closing"
                takeaway = "What this demonstrates"

            report.add(f"{rel}: has takeaway section", takeaway in text)

            multi = []
            for line_no, line in enumerate(text.splitlines(), 1):
                match = speaker.match(line.strip())
                if not match:
                    continue
                body = match.group(1)
                if closing_marker.lower() in body.lower():
                    continue
                marks = body.count("？") + body.count("?")
                if marks > 1:
                    multi.append(f"L{line_no}({marks})")
            report.add(f"{rel}: one question per turn", not multi, ", ".join(multi) or "ok")

            bad = [p for p in FORBIDDEN_IN_EXAMPLES if p in text]
            report.add(f"{rel}: no verdict phrasing", not bad, ", ".join(bad) or "ok")


def check_repo(report: Report, root: Path) -> None:
    files = ["README.md", "README.zh-CN.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md"]
    for name in files:
        report.add(f"{name} exists", (root / name).exists())

    license_text = (root / "LICENSE").read_text(encoding="utf-8") if (root / "LICENSE").exists() else ""
    report.add("LICENSE has a real holder", "<YOUR NAME>" not in license_text and "Copyright (c)" in license_text)

    readme = (root / "README.md").read_text(encoding="utf-8") if (root / "README.md").exists() else ""
    report.add("README states version", bool(re.search(r"Version \d+\.\d+\.\d+", readme)))
    report.add("README has license section", "## License" in readme)

    changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8") if (root / "CHANGELOG.md").exists() else ""
    report.add("CHANGELOG has 1.0.0", "[1.0.0]" in changelog)


def check_links(report: Report, root: Path) -> None:
    broken: list[str] = []
    for path in root.rglob("*.md"):
        if any(part in {".git", "node_modules"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        for target in MD_LINK.findall(text):
            target = target.strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                broken.append(f"{path.relative_to(root).as_posix()} -> {target}")
    report.add("relative markdown links resolve", not broken, "; ".join(broken[:5]) or "ok")


def check_zh_en_parity(report: Report, root: Path) -> None:
    zh = (root / "SKILL.md").read_text(encoding="utf-8")
    en = (root / "SKILL.en.md").read_text(encoding="utf-8") if (root / "SKILL.en.md").exists() else ""
    if not en:
        return
    zh_rows = len(re.findall(r"^\|", zh, re.M))
    en_rows = len(re.findall(r"^\|", en, re.M))
    report.add("bilingual table rows comparable", abs(zh_rows - en_rows) <= 2, f"zh={zh_rows} en={en_rows}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    report = Report()

    meta = check_frontmatter(report, root)
    if meta:
        check_bilingual(report, root, meta)
    check_references(report, root)
    check_examples(report, root)
    check_repo(report, root)
    check_links(report, root)
    check_zh_en_parity(report, root)

    if args.json:
        print(json.dumps(
            [{"check": c.name, "ok": c.ok, "detail": c.detail} for c in report.checks],
            ensure_ascii=False, indent=2,
        ))
    else:
        width = max(len(c.name) for c in report.checks)
        for c in report.checks:
            status = "PASS" if c.ok else "FAIL"
            print(f"[{status}] {c.name.ljust(width)}  {c.detail}")
        print()
        print(f"{len(report.checks) - len(report.failed)}/{len(report.checks)} checks passed")

    return 0 if not report.failed else 1


if __name__ == "__main__":
    sys.exit(main())
