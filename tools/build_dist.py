#!/usr/bin/env python3
"""Rebuild dist/ux-unification.zip from skills/ux-unification.

Usage (from the repo root):  python3 tools/build_dist.py

The zip contains the skill folder at its root, which is the layout chat apps expect
when you upload a skill.
"""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "ux-unification"
DIST = ROOT / "dist"
SKIP_PARTS = {"__pycache__", ".DS_Store"}


def check_skill() -> None:
    md = SKILL_DIR / "SKILL.md"
    if not md.exists():
        sys.exit(f"Missing {md}")
    text = md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit("SKILL.md must start with YAML frontmatter between --- lines")
    front = m.group(1)
    name = re.search(r"^name:\s*(.+)$", front, re.M)
    desc = re.search(r"^description:\s*(.+)$", front, re.M)
    if not name or name.group(1).strip() != SKILL_DIR.name:
        sys.exit(f"frontmatter 'name' must equal the folder name '{SKILL_DIR.name}'")
    if not desc or len(desc.group(1)) > 1024:
        sys.exit("frontmatter 'description' is missing or longer than 1024 characters")
    if "<" in desc.group(1) or ">" in desc.group(1):
        sys.exit("description must not contain angle brackets")


def build(target: Path) -> int:
    count = 0
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(SKILL_DIR.rglob("*")):
            if f.is_dir() or any(p in SKIP_PARTS for p in f.parts) or f.suffix == ".pyc":
                continue
            z.write(f, f.relative_to(SKILL_DIR.parent))
            count += 1
    return count


def main() -> None:
    check_skill()
    DIST.mkdir(exist_ok=True)
    n = build(DIST / "ux-unification.zip")
    print(f"built dist/ux-unification.zip ({n} files)")


if __name__ == "__main__":
    main()
