#!/usr/bin/env python3
"""
scan_inventory.py — quick, dependency-free inventory of a front-end codebase
for the ux-unification skill.

It collects facts that seed the System Map:
  - stack (framework, styling, component libs, i18n, router)
  - routes (Next.js app/pages dirs, React Router, Vue Router)
  - navigation / layout / shell files
  - components and how many files use each one (JSX usage)
  - design tokens (Tailwind config, CSS custom properties, theme files)
    and hard-coded colors outside token files
  - UI strings (i18n files + JSX text + label-like props)
  - permission / role / feature-flag hints
  - global-pattern candidates (modal, toast, empty state, ...)
  - possible divergences (several components doing the same job)

It is a starting point, not a source of truth: read the files it ranks highest.

Usage:
  python scan_inventory.py <repo-path> [--out scan.json] [--md scan.md]
                           [--max-strings 400] [--include-dir src]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

IGNORE_DIRS = {
    "node_modules", ".git", "dist", "build", ".next", ".nuxt", ".output", "out",
    "coverage", ".ux-unify", "vendor", ".turbo", ".cache", ".svelte-kit",
    "storybook-static", "__pycache__", ".venv", "venv", "target", ".idea", ".vscode",
}
CODE_EXT = {".tsx", ".jsx", ".ts", ".js", ".vue", ".svelte", ".mjs", ".cjs"}
MARKUP_EXT = {".tsx", ".jsx", ".vue", ".svelte", ".html"}
STYLE_EXT = {".css", ".scss", ".sass", ".less", ".pcss"}
MAX_FILE_BYTES = 600_000

STACK_DEPS = {
    "framework": ["next", "react", "vue", "nuxt", "@angular/core", "svelte", "@sveltejs/kit", "solid-js", "react-native", "expo"],
    "styling": ["tailwindcss", "styled-components", "@emotion/react", "sass", "@vanilla-extract/css", "@stitches/react", "unocss"],
    "component_library": ["@mui/material", "@chakra-ui/react", "antd", "@mantine/core", "@radix-ui/react-dialog",
                          "@headlessui/react", "react-bootstrap", "@fluentui/react", "primereact", "vuetify",
                          "element-plus", "@nextui-org/react", "@ark-ui/react", "react-aria-components"],
    "i18n": ["react-i18next", "i18next", "next-intl", "react-intl", "vue-i18n", "@lingui/core", "next-i18next"],
    "router": ["react-router-dom", "react-router", "@tanstack/react-router", "vue-router", "wouter"],
    "data": ["@tanstack/react-query", "swr", "@apollo/client", "redux", "@reduxjs/toolkit", "zustand", "pinia", "jotai"],
    "forms": ["react-hook-form", "formik", "zod", "yup"],
    "icons": ["lucide-react", "@heroicons/react", "react-icons", "@tabler/icons-react", "@phosphor-icons/react", "@mui/icons-material"],
}

NAV_NAME_RE = re.compile(r"(sidebar|sidenav|navbar|nav(igation)?|menu|appshell|app-shell|shell|layout|header|topbar|breadcrumb)", re.I)
GLOBAL_PATTERN_KEYWORDS = {
    "modal/dialog": r"modal|dialog|drawer|sheet",
    "confirm": r"confirm",
    "toast/notification": r"toast|notif|snackbar|sonner",
    "empty state": r"empty",
    "loading": r"skeleton|spinner|loader|loading",
    "error": r"errorboundary|error[-_]?state|errorpage|fallback",
    "alert/banner": r"alert|banner|callout",
    "table": r"table|grid|datagrid",
    "form": r"form|field|input",
    "tabs": r"^tabs?$|^tab(?!le)|tabs$",
    "page header": r"pageheader|page[-_]header|pagetitle",
    "button": r"button|btn",
    "badge/status": r"badge|chip|tag|pill|status",
    "card": r"card",
}
PERMISSION_RE = re.compile(
    r"\b(hasPermission|can\(|useAbility|usePermission|RequireRole|RequireAuth|ProtectedRoute|isAdmin|"
    r"roles?\s*(?::|=(?![\"'])|===)|permissions?\s*[:=]|featureFlag|useFeatureFlag|useFlag|isEnabled\()"
)
JSX_TAG_RE = re.compile(r"<([A-Z][A-Za-z0-9]*(?:\.[A-Z][A-Za-z0-9]*)?)[\s/>]")
EXPORT_COMPONENT_RE = re.compile(
    r"export\s+(?:default\s+)?(?:function|const|class)\s+([A-Z][A-Za-z0-9]*)"
)
JSX_TEXT_RE = re.compile(r">\s*([A-Za-zÀ-ỹ][^<>{}\n]{1,80}?)\s*<")
LABEL_PROP_RE = re.compile(r"\b(label|title|placeholder|aria-label|tooltip|description|emptyText|confirmText|cancelText)=\"([^\"]{2,100})\"")
HEX_RE = re.compile(r"#(?:[0-9a-fA-F]{3}){1,2}\b")
TW_ARBITRARY_RE = re.compile(r"\b[a-z-]+-\[(?:#|\d)[^\]]*\]")
CSS_VAR_DEF_RE = re.compile(r"(--[A-Za-z0-9-_]+)\s*:\s*([^;]+);")
RR_PATH_RE = re.compile(r"""path\s*[:=]\s*["'`]([^"'`]+)["'`]""")


def read(p: Path) -> str:
    try:
        if p.stat().st_size > MAX_FILE_BYTES:
            return ""
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def walk(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS and not d.startswith(".")]
        for f in filenames:
            yield Path(dirpath) / f


def rel(p: Path, root: Path) -> str:
    try:
        return str(p.relative_to(root))
    except ValueError:
        return str(p)


def detect_stack(root: Path, files: list[Path]) -> dict:
    deps: dict[str, str] = {}
    pkg_files = [f for f in files if f.name == "package.json"]
    for pf in pkg_files:
        try:
            data = json.loads(read(pf) or "{}")
        except json.JSONDecodeError:
            continue
        for key in ("dependencies", "devDependencies", "peerDependencies"):
            deps.update(data.get(key, {}) or {})
    stack = {cat: [d for d in names if d in deps] for cat, names in STACK_DEPS.items()}
    stack["typescript"] = "typescript" in deps or any(f.suffix in {".ts", ".tsx"} for f in files)
    stack["shadcn_ui"] = any(f.name == "components.json" for f in files)
    stack["package_json_files"] = [rel(p, root) for p in pkg_files]
    stack["monorepo_hint"] = len(pkg_files) > 1
    return stack


def next_route_from(path: Path, base: Path, kind: str) -> str | None:
    parts = list(path.relative_to(base).parts)
    if kind == "app":
        if path.stem not in {"page"}:
            return None
        parts = parts[:-1]
        parts = [p for p in parts if not (p.startswith("(") and p.endswith(")")) and not p.startswith("@")]
    else:  # pages
        if parts and parts[0] in {"api"}:
            return None
        if path.stem.startswith("_"):
            return None
        parts[-1] = path.stem
        if parts[-1] == "index":
            parts = parts[:-1]
    return "/" + "/".join(parts)


def find_routes(root: Path, files: list[Path], file_routing: bool) -> list[dict]:
    routes = []
    for f in files:
        if not file_routing or f.suffix not in CODE_EXT:
            continue
        parts = f.parts
        for kind in ("app", "pages"):
            if kind in parts:
                idx = len(parts) - 1 - list(reversed(parts)).index(kind)
                base = Path(*parts[: idx + 1])
                try:
                    r = next_route_from(f, base, kind)
                except Exception:
                    r = None
                if r:
                    routes.append({"path": r, "file": rel(f, root), "source": f"next-{kind}"})
                break
    for f in files:
        if f.suffix not in CODE_EXT:
            continue
        name = f.name.lower()
        text = read(f)
        if not text:
            continue
        if ("route" in name or "router" in name or "<Route" in text or "createBrowserRouter" in text
                or "createRouter" in text):
            for m in RR_PATH_RE.finditer(text):
                p = m.group(1)
                if " " not in p and (p.startswith(("/", ":", "*")) or re.match(r"^[A-Za-z0-9_-]", p)) and "." not in p:
                    line = text.count("\n", 0, m.start()) + 1
                    routes.append({"path": p, "file": f"{rel(f, root)}:{line}", "source": "router-config"})
    seen, out = set(), []
    for r in routes:
        k = (r["path"], r["file"])
        if k not in seen:
            seen.add(k)
            out.append(r)
    return sorted(out, key=lambda r: r["path"])


def find_components(root: Path, files: list[Path]) -> dict[str, list[str]]:
    defs: dict[str, list[str]] = defaultdict(list)
    for f in files:
        if f.suffix not in MARKUP_EXT and f.suffix not in {".ts", ".js"}:
            continue
        if any(seg in {"test", "tests", "__tests__", "stories"} for seg in f.parts) or ".test." in f.name or ".spec." in f.name or ".stories." in f.name:
            continue
        text = read(f)
        if not text:
            continue
        names = set(EXPORT_COMPONENT_RE.findall(text))
        if f.suffix in {".vue", ".svelte"} and f.stem[:1].isupper():
            names.add(f.stem)
        if f.suffix in {".ts", ".js"}:
            names = {n for n in names if "<" in text or "createElement" in text}
        for n in names:
            defs[n].append(rel(f, root))
    return defs


def count_usage(root: Path, files: list[Path], component_names: set[str]) -> tuple[Counter, dict[str, list[str]]]:
    usage_files: dict[str, set[str]] = defaultdict(set)
    for f in files:
        if f.suffix not in MARKUP_EXT:
            continue
        text = read(f)
        if not text:
            continue
        tags = set(t.split(".")[0] for t in JSX_TAG_RE.findall(text))
        if f.suffix == ".vue":
            for n in component_names:
                kebab = re.sub(r"(?<!^)(?=[A-Z])", "-", n).lower()
                if f"<{kebab}" in text:
                    tags.add(n)
        for t in tags & component_names:
            usage_files[t].add(rel(f, root))
    counts = Counter({k: len(v) for k, v in usage_files.items()})
    return counts, {k: sorted(v) for k, v in usage_files.items()}


def find_tokens(root: Path, files: list[Path]) -> dict:
    token_files, css_vars, tw_configs = [], {}, []
    for f in files:
        n = f.name.lower()
        if n.startswith("tailwind.config"):
            tw_configs.append(rel(f, root))
        if re.search(r"(theme|tokens?|colors?|palette|variables|design[-_]?system)", n) and f.suffix in CODE_EXT | STYLE_EXT | {".json"}:
            token_files.append(rel(f, root))
        if f.suffix in STYLE_EXT:
            for m in CSS_VAR_DEF_RE.finditer(read(f)):
                css_vars.setdefault(m.group(1), {"value": m.group(2).strip()[:60], "file": rel(f, root)})
    return {
        "tailwind_configs": tw_configs,
        "token_files": sorted(set(token_files)),
        "css_custom_properties": dict(list(css_vars.items())[:300]),
        "css_custom_property_count": len(css_vars),
    }


def find_hardcoded(root: Path, files: list[Path], token_files: set[str]) -> dict:
    hex_by_file, tw_arb_by_file = Counter(), Counter()
    for f in files:
        if f.suffix not in MARKUP_EXT and f.suffix not in STYLE_EXT:
            continue
        r = rel(f, root)
        if r in token_files or "tailwind.config" in r:
            continue
        text = read(f)
        if f.suffix in STYLE_EXT:
            text = CSS_VAR_DEF_RE.sub("", text)
        h = len(HEX_RE.findall(text))
        a = len(TW_ARBITRARY_RE.findall(text))
        if h:
            hex_by_file[r] = h
        if a:
            tw_arb_by_file[r] = a
    return {
        "hex_colors_total": sum(hex_by_file.values()),
        "hex_colors_top_files": hex_by_file.most_common(15),
        "tailwind_arbitrary_values_total": sum(tw_arb_by_file.values()),
        "tailwind_arbitrary_top_files": tw_arb_by_file.most_common(15),
    }


def flatten(d, prefix=""):
    if isinstance(d, dict):
        for k, v in d.items():
            yield from flatten(v, f"{prefix}.{k}" if prefix else str(k))
    elif isinstance(d, str):
        yield prefix, d


def find_strings(root: Path, files: list[Path], max_strings: int) -> dict:
    i18n_files, i18n_strings = [], []
    for f in files:
        if f.suffix != ".json":
            continue
        if not any(seg.lower() in {"locales", "locale", "i18n", "lang", "langs", "messages", "translations"} for seg in f.parts):
            continue
        try:
            data = json.loads(read(f) or "{}")
        except json.JSONDecodeError:
            continue
        i18n_files.append(rel(f, root))
        for k, v in flatten(data):
            i18n_strings.append({"key": k, "text": v[:100], "file": rel(f, root)})
    inline = Counter()
    where: dict[str, str] = {}
    for f in files:
        if f.suffix not in MARKUP_EXT:
            continue
        text = read(f)
        if not text:
            continue
        for m in JSX_TEXT_RE.finditer(text):
            s = m.group(1).strip()
            if len(s) < 2 or re.fullmatch(r"[\W\d_]+", s) or "=>" in s or "&&" in s:
                continue
            inline[s] += 1
            where.setdefault(s, rel(f, root))
        for m in LABEL_PROP_RE.finditer(text):
            s = m.group(2).strip()
            inline[s] += 1
            where.setdefault(s, rel(f, root))
    inline_list = [{"text": s, "count": c, "first_seen": where[s]} for s, c in inline.most_common(max_strings)]
    return {
        "i18n_files": i18n_files,
        "i18n_string_count": len(i18n_strings),
        "i18n_sample": i18n_strings[:max_strings],
        "inline_strings": inline_list,
    }


def find_permissions(root: Path, files: list[Path], limit=80) -> list[dict]:
    hits = []
    for f in files:
        if f.suffix not in CODE_EXT:
            continue
        text = read(f)
        if not text:
            continue
        for m in PERMISSION_RE.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            line = text.splitlines()[line_no - 1].strip()[:140] if text else ""
            key = f"{rel(f, root)}:{line_no}"
            if hits and hits[-1]["file"] == key:
                continue
            hits.append({"file": key, "match": m.group(1), "line": line})
            if len(hits) >= limit:
                return hits
    return hits


def nav_files(root: Path, files: list[Path]) -> list[str]:
    out = []
    for f in files:
        if f.suffix in MARKUP_EXT | {".ts", ".js"} and NAV_NAME_RE.search(f.stem):
            out.append(rel(f, root))
    return sorted(out)


def component_kind(name: str, paths: list[str]) -> str:
    joined = " ".join(paths).replace("\\", "/")
    if name.endswith(("Page", "Screen", "View", "Route")) or re.search(r"(^|/)(pages|app|screens|views|routes)/", joined):
        return "page"
    if re.search(r"(^|/)(layout|layouts|shell)/", joined) or NAV_NAME_RE.search(name):
        return "layout"
    return "component"


def group_patterns(defs: dict[str, list[str]], usage: Counter) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = {}
    for label, pattern in GLOBAL_PATTERN_KEYWORDS.items():
        rx = re.compile(pattern, re.I)
        members = [
            {"component": n, "defined_in": defs[n][:3], "used_in_files": usage.get(n, 0)}
            for n in defs if rx.search(n) and component_kind(n, defs[n]) != "page"
        ]
        if members:
            groups[label] = sorted(members, key=lambda m: -m["used_in_files"])
    return groups


def divergence_hints(groups: dict[str, list[dict]]) -> list[str]:
    hints = []
    for label, members in groups.items():
        used = [m for m in members if m["used_in_files"] > 0]
        if label in {"form", "button"}:
            continue
        if len(used) >= 2:
            names = ", ".join(f"{m['component']} ({m['used_in_files']})" for m in used[:6])
            hints.append(f"{label}: {len(used)} components in use — {names}. Check whether they do the same job.")
    return hints


def to_markdown(r: dict) -> str:
    L = []
    L.append(f"# Inventory scan — {r['repo']}")
    L.append(f"_Scanned {r['scanned_at']} · {r['file_count']} files · generated by scan_inventory.py — a starting point, verify by reading the files._\n")
    s = r["stack"]
    L.append("## Stack")
    for k in STACK_DEPS:
        if s.get(k):
            L.append(f"- **{k}**: {', '.join(s[k])}")
    L.append(f"- **typescript**: {s['typescript']} · **shadcn/ui**: {s['shadcn_ui']} · **monorepo hint**: {s['monorepo_hint']}")
    L.append("\n## Routes")
    if r["routes"]:
        L.append("| Path | File | Source |\n|---|---|---|")
        for x in r["routes"][:200]:
            L.append(f"| `{x['path']}` | `{x['file']}` | {x['source']} |")
    else:
        L.append("_No routes detected — check router setup manually._")
    L.append("\n## Navigation / layout / shell files")
    L += [f"- `{f}`" for f in r["nav_files"][:60]] or ["_None found._"]
    L.append("\n## Most-used components")
    L.append("| Component | Kind | Used in (files) | Defined in |\n|---|---|---|---|")
    for c in [c for c in r["components"] if c["kind"] != "page"][:80]:
        L.append(f"| {c['name']} | {c['kind']} | {c['used_in_files']} | `{'`, `'.join(c['defined_in'][:2])}` |")
    pages = [c for c in r["components"] if c["kind"] == "page"]
    if pages:
        L.append("\n## Pages / screens")
        L += [f"- {c['name']} — `{c['defined_in'][0]}`" for c in pages[:80]]
    L.append("\n## Pattern groups (by component name)")
    for label, members in r["pattern_groups"].items():
        L.append(f"- **{label}**: " + ", ".join(f"{m['component']} ({m['used_in_files']})" for m in members[:10]))
    L.append("\n## Possible divergences")
    L += [f"- {h}" for h in r["divergence_hints"]] or ["_None detected by name._"]
    t = r["tokens"]
    L.append("\n## Tokens")
    L.append(f"- Tailwind configs: {', '.join(f'`{x}`' for x in t['tailwind_configs']) or '—'}")
    L.append(f"- Token/theme files: {', '.join(f'`{x}`' for x in t['token_files'][:20]) or '—'}")
    L.append(f"- CSS custom properties: {t['css_custom_property_count']}")
    for name, v in list(t["css_custom_properties"].items())[:40]:
        L.append(f"  - `{name}`: `{v['value']}` ({v['file']})")
    h = r["hardcoded"]
    L.append("\n## Hard-coded values outside token files")
    L.append(f"- Hex colors: {h['hex_colors_total']} · Tailwind arbitrary values: {h['tailwind_arbitrary_values_total']}")
    for f, n in h["hex_colors_top_files"][:10]:
        L.append(f"  - `{f}`: {n} hex")
    for f, n in h["tailwind_arbitrary_top_files"][:10]:
        L.append(f"  - `{f}`: {n} arbitrary")
    st = r["strings"]
    L.append("\n## UI strings")
    L.append(f"- i18n files: {', '.join(f'`{x}`' for x in st['i18n_files'][:10]) or '—'} ({st['i18n_string_count']} strings)")
    L.append("- Most frequent inline strings:")
    for x in st["inline_strings"][:60]:
        L.append(f"  - \"{x['text']}\" ×{x['count']} (`{x['first_seen']}`)")
    L.append("\n## Permission / role / flag hints")
    for p in r["permissions"][:40]:
        L.append(f"- `{p['file']}` — {p['line']}")
    if not r["permissions"]:
        L.append("_None found — roles may be server-side or not modelled._")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("repo")
    ap.add_argument("--out", help="write JSON here")
    ap.add_argument("--md", help="write Markdown summary here")
    ap.add_argument("--max-strings", type=int, default=400)
    ap.add_argument("--include-dir", action="append", help="limit scan to these subdirectories (repeatable)")
    a = ap.parse_args()

    root = Path(a.repo).resolve()
    if not root.is_dir():
        sys.exit(f"Not a directory: {root}")
    scan_roots = [root / d for d in a.include_dir] if a.include_dir else [root]
    files = [f for sr in scan_roots if sr.exists() for f in walk(sr)]
    # always include package.json files at root for stack detection
    files += [p for p in root.glob("package.json") if p not in files]

    stack = detect_stack(root, files)
    defs = find_components(root, files)
    usage, usage_files = count_usage(root, files, set(defs))
    tokens = find_tokens(root, files)
    groups = group_patterns(defs, usage)

    components = sorted(
        ({"name": n, "kind": component_kind(n, d), "defined_in": d, "used_in_files": usage.get(n, 0),
          "used_by": usage_files.get(n, [])[:25]}
         for n, d in defs.items()),
        key=lambda c: (-c["used_in_files"], c["name"]),
    )

    result = {
        "repo": str(root),
        "scanned_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "file_count": len(files),
        "stack": stack,
        "routes": find_routes(root, files, file_routing=bool(set(stack["framework"]) & {"next", "nuxt", "@sveltejs/kit"})),
        "nav_files": nav_files(root, files),
        "components": components,
        "pattern_groups": groups,
        "divergence_hints": divergence_hints(groups),
        "tokens": tokens,
        "hardcoded": find_hardcoded(root, files, set(tokens["token_files"])),
        "strings": find_strings(root, files, a.max_strings),
        "permissions": find_permissions(root, files),
    }

    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    md = to_markdown(result)
    if a.md:
        Path(a.md).parent.mkdir(parents=True, exist_ok=True)
        Path(a.md).write_text(md, encoding="utf-8")
    if not a.out and not a.md:
        print(md)
    else:
        print(f"Scanned {len(files)} files · {len(result['routes'])} routes · {len(components)} components · "
              f"{len(result['divergence_hints'])} divergence hints")


if __name__ == "__main__":
    main()
