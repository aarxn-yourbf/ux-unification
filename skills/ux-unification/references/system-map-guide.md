# System Map guide

The System Map is a picture of the experience as it exists today. It is the shared ground truth every feature is measured against. It lives in `.ux-unify/system-map/` and is meant to be committed so the whole team uses the same map.

Principles:
- **Roughly right and honest beats long and guessed.** Mark anything not directly seen in code as `[INFERRED]`.
- **Cite files.** Every entry points to where it comes from.
- **User language first.** Record what users see (labels on screen), and note the internal name next to it if different.
- **Incremental.** Build what the current feature needs in depth; keep the rest at summary level and deepen it on later runs.

## Where to look in a codebase

| What | Typical locations |
|---|---|
| Routes / pages | `app/**/page.tsx`, `pages/**`, `src/routes/**`, router config (`createBrowserRouter`, `<Route path=…>`), Vue `router/index.ts`, Angular `*-routing.module.ts` |
| Navigation | `Sidebar`, `Nav`, `Menu`, `AppShell`, `Layout`, `Header` components; nav config arrays (`navItems`, `menuConfig`) |
| Roles / permissions | `roles`, `permissions`, `can(`, `hasPermission`, `useAbility`, `RequireRole`, route guards, feature flags, `ACL` |
| Tokens | `tailwind.config.*`, `theme.ts`, `tokens.json`, CSS custom properties `--*`, SCSS variables, MUI/Chakra theme objects |
| Components | `components/`, `ui/`, `design-system/`, `packages/ui`, Storybook stories (`*.stories.*`) |
| UI strings | i18n files (`locales/**.json`, `messages/**`), JSX text, `label=`, `title=`, `placeholder=` props |
| Global patterns | App shell, toast/notification provider, modal/dialog provider, error boundaries, empty-state components, loading skeletons |

Run `scripts/scan_inventory.py` first; it collects most of this into `_scan.json` / `_scan.md`. Then open the files it ranks highest (most-used components, nav and layout files, theme files) to understand them properly.

## Files and required contents

### `README.md`
- Scope scanned (paths, apps), date, git commit if available.
- Stack summary: framework, language, styling approach, component library, i18n, state/data libraries.
- Known gaps and what is `[INFERRED]`.

### `ia-tree.md`
A tree of the information architecture as the user experiences it, built from navigation config plus routes.

```
Product
├── Investigation            (nav: Sidebar.tsx L12)
│   ├── Alerts               /alerts        → AlertsPage.tsx
│   └── Cases                /cases         → CasesPage.tsx
└── Strategy
    ├── Rules                /rules         → RulesPage.tsx
    └── Data transformations /plans         → PlansPage.tsx  (internal name "Plans")
```
Note routes that exist but are not in navigation (hidden, deep-link only, admin).

### `roles.md`
Role × area matrix. Use ✔ (sees and uses), ○ (sees, rarely uses), ✖ (hidden). Cite the guard/permission code. If roles aren't in code, derive from PRDs/notes and mark `[INFERRED]`.

| Area | Analyst | Data scientist | Admin | Source |
|---|---|---|---|---|
| Alerts | ✔ | ○ | ✔ | `routes.tsx` guard `role in [...]` |

### `journeys.md`
The main jobs users do and the screens that serve each, in order. Keep each to one line of steps:
`Review an alert: Alerts list → Alert detail → Decide (approve/escalate) → Case`
Mark entry points and where journeys cross areas; cross-area hops are where inconsistency hurts most.

### `glossary.md`
| User-facing term | Meaning | Where used | Internal/code name | Notes |
|---|---|---|---|---|
Flag: same concept with different labels; same label for different concepts; technical terms visible to users.

### `tokens.md`
Colors (semantic names if they exist), spacing scale, typography scale, radius, shadows, breakpoints. Note whether components use tokens consistently or hard-code values (count hard-coded hex/px if the scanner found them).

### `patterns.md`
The pattern registry. One entry per pattern:

```
### Data table
- Component(s): src/components/ui/DataTable.tsx
- Used in: 14 files (AlertsPage, CasesPage, RulesPage, …)
- Variants: selectable rows, inline actions, pagination
- States: empty (EmptyState), loading (Skeleton), error (inline Alert)
- Notes: CasesPage uses a hand-rolled <table> instead → debt
```
Also include **divergences**: the same job done differently (e.g. two modal implementations, three ways to confirm deletion). Divergences go to `debt.md` too.

### `global-patterns.md`
Cross-cutting rules every feature must follow: navigation model, context/workspace switching, permissions handling (hide vs disable vs explain), notifications/toasts, confirmation of destructive actions, form validation style, empty/loading/error conventions, date/number formatting, page header structure.

### `debt.md`
Unification debt, accumulated over runs:

| # | Debt | Layer | Evidence | Impact | Suggested fix | Found in |
|---|---|---|---|---|---|---|
| 1 | Two confirm-dialog implementations | Behaviour | `ConfirmModal.tsx`, `DeleteDialog.tsx` | Users see different wording/button order | Consolidate to `ConfirmModal` | feature: bulk-export |

## Refreshing an existing map

1. Read `README.md` for the last scan date/commit.
2. If git is available: `git log --since=<date> --name-only` to see what changed; re-scan only changed areas.
3. Re-run the scanner if many files changed; diff against the previous `_scan.json`.
4. Update entries; don't silently delete history in `debt.md`—mark resolved items as resolved.
