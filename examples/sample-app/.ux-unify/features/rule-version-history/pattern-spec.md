# Pattern spec — Rule version history & rollback

> PRD: `examples/prd-rule-version-history.md` · System Map: 2026-11-01 · Author: ux-unification

## 1. Summary
A **Versions** tab on Rule detail lists every saved version of the rule in the standard data table. Users tick two versions and press **Compare** to see the rule conditions side by side. Data scientists can **Restore version** from any past row; a confirmation dialog explains that this creates a new version. Managers see the same tab without the restore action.

## 2. Placement
See `analysis.md › Placement`. Tab order: Definition · Performance · Versions.

## 3. UI needs → pattern decisions
| # | Need (from PRD) | Rung | Pattern / component | Evidence | Confidence |
|---|---|---|---|---|---|
| 1 | Put history in context of one rule | Reuse | Tabs on detail page | `RuleDetailPage.tsx`, `CaseDetailPage.tsx` | High |
| 2 | List versions with author, date, status, summary | Reuse | `DataTable` | `AlertsPage.tsx`, `RulesPage.tsx` | High |
| 3 | Show version status | Extend | `StatusBadge` + `archived` | `AlertsPage.tsx`, `RulesPage.tsx` | High |
| 4 | Choose two versions to compare | Extend | `DataTable` + `selectable`, `maxSelected` | `DataTable.tsx` | Medium → §7 |
| 5 | Compare two versions | Create | `VersionDiff` (built from tokens) | none — no comparison view exists | Medium |
| 6 | Restore with confirmation | Extend | `ConfirmModal` + `confirmVariant="primary"` | `RuleDetailPage.tsx` | High |
| 7 | Hide restore from managers | Compose | `hasPermission` + conditional render | `permissions.ts` | Medium → §7 |
| 8 | Only one version | Reuse | `EmptyState` | `DataTable.tsx`, `PlansPage.tsx` | High |

## 4. Layout
Inside the Versions tab, top to bottom:
1. Toolbar row: helper text "Select two versions to compare" (muted) on the left; **Compare** button (secondary, disabled until 2 selected) on the right.
2. `DataTable` columns: ☐ · Version · Status · Author · Saved · Summary · (row action) **Restore version** (secondary button, data scientist only, hidden on the active version).
3. When Compare is pressed: `VersionDiff` appears below the table (same page, no modal) with "Close comparison" link. Inline rather than modal because diffs are long and users scroll between table and diff.

Mirrors: Rule detail header and tabs (`RuleDetailPage.tsx`), table density of `RulesPage.tsx`.

## 5. Flow
```
Rule detail → Versions tab → tick v7 and v6 → Compare → read diff
           → Restore version (v6) → ConfirmModal "Restore version 6?" → Restore version
           → new version v8 created (copy of v6) → Definition tab, header subtitle "Version 8"
```

## 6. States
| State | Trigger | What the user sees | Component |
|---|---|---|---|
| Empty | Rule has 1 version | "This rule has only one version. Versions appear here each time you save changes." | `EmptyState` |
| Loading | Fetching versions | Pulse block | `DataTable` loading |
| Error | Fetch fails | "Couldn't load versions. Try again." + Retry button | `EmptyState` with action |
| Selection < 2 | 0–1 rows ticked | Compare disabled, helper text visible | `Button` |
| Selection = 2 | 2 rows ticked | Further checkboxes disabled | `DataTable` `maxSelected` |
| Comparing | Compare pressed | `VersionDiff` under table | `VersionDiff` |
| Restoring | Confirm pressed | Confirm button shows "Restoring…" | `ConfirmModal` |
| Success | Restore done | Switch to Definition, subtitle shows new version | `Tabs`, `PageHeader` |
| No permission | Manager | No Restore column action; everything else identical | conditional render |

## 7. Options (Medium confidence decisions)

### Decision 4: how users pick two versions
**Option A — Row checkboxes, max 2 (Extend DataTable)**
+ Matches the PRD exactly (any two versions)
+ Adds selection to DataTable, which future bulk actions (e.g. bulk alert assignment) will need
− Changes a shared component (2 existing usages; default off, so no visual change there)
Assumes: users sometimes compare two old versions, not only "old vs current"

**Option B — "Compare with active" row action (Reuse DataTable)**
+ No change to DataTable; one click per comparison
− Can't compare two past versions (PRD req. 2 partly unmet)
Assumes: users almost always compare against the active version

**Recommendation: A.** It satisfies the PRD and the extension is reusable. Validate with task 3.

### Decision 7: what managers see for Restore
**Option A — Hide the action** — cleaner, matches area-level hiding in `permissions.ts`; managers may not know restore exists.
**Option B — Disabled button with tooltip "Only data scientists can restore versions"** — explains the rule; adds a disabled control on every row.
**Recommendation: A**, and record "hide actions the role cannot perform" in `global-patterns.md` as the product convention (debt #5).

## 8. Microcopy
| Element | Text | Source |
|---|---|---|
| Tab | Versions | glossary (new) |
| Helper | Select two versions to compare | — |
| Button | Compare | glossary (new) |
| Row action | Restore version | glossary (new), verb + object like "Save changes" |
| Confirm title | Restore version {n}? | ConfirmModal title pattern "Delete rule?" |
| Confirm message | This creates version {next} with the same conditions as version {n}. The current version stays in the history. | — |
| Confirm button | Restore version | — |
| Empty | This rule has only one version. Versions appear here each time you save changes. | EmptyState |
| Diff headers | Version {a} · {date} / Version {b} · {date} | — |

## 9. Accessibility
Checkboxes have `aria-label="Select version {n}"`; diff marks added/removed lines with text prefixes (+/−), not color only.
