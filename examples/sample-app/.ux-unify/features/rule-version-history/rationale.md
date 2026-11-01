# Rationale — Rule version history & rollback

## 1. Decision summary
Version history lives in a new **Versions** tab on Rule detail, next to Definition and Performance, so it sits on the path users already take when they edit a rule. The list reuses the standard data table and status badge; restoring reuses the existing confirmation dialog. Only one new pattern is introduced: a side-by-side **comparison view**, because nothing like it exists. Four existing components get small, backward-compatible additions.

**Needs your review:**
- Decision 4 — checkboxes (max 2) in DataTable vs "Compare with active" (recommend checkboxes).
- Decision 7 — hide vs disable Restore for managers (recommend hide, and make it the product convention).
- The new `VersionDiff` pattern (Create).

## 2. Why these patterns
- **Tab on Rule detail** — detail pages already use `PageHeader` + `Tabs` (`RuleDetailPage.tsx`, `CaseDetailPage.tsx`). Versions are a peer view of the same object, which is exactly what tabs are for. A separate page (my first hypothesis) would add a location users must learn and break the "edit → check → fix" loop.
- **DataTable for the list** — every list in the product uses it (`AlertsPage.tsx`, `RulesPage.tsx`); it brings loading and empty states for free.
- **StatusBadge** — status is shown this way in both lists (`AlertsPage.tsx`, `RulesPage.tsx`).
- **ConfirmModal for restore** — the product's confirmation pattern (`RuleDetailPage.tsx`). Using it keeps button order, wording style and look identical.
- **EmptyState** — used by `DataTable` and `PlansPage.tsx`.

## 3. What was adapted for this PRD — and why
| Change vs. existing pattern | PRD requirement | Impact on existing usages |
|---|---|---|
| `DataTable`: optional `selectable`, `maxSelected` | Req. 2 — compare any two versions | None; off by default (AlertsPage, RulesPage) |
| `ConfirmModal`: `confirmVariant` | Req. 3 — confirmation for restore, which is not destructive, so a red button would mislead | None; default stays "danger" (RuleDetailPage) |
| `StatusBadge`: `archived` | Req. 1 — show status of past versions | None; new key only |
| `Button`: `disabled` | Compare needs exactly two selections | None; optional prop |
| Comparison shown inline, not in a modal | Req. 2 — diffs are long; users scroll between list and diff | — |

## 4. Hypothesis vs. outcome
| Hypothesis | Final decision | Why it changed |
|---|---|---|
| New "Change log" page under Rules | Versions **tab** on Rule detail | Journey analysis: users need history right after editing a rule; detail pages already use tabs |
| Diff in a modal | Inline comparison under the table | Length of diffs; modal would hide the table |
| Similar to Case "Activity" | Different concept, different label | Activity = events; Versions = restorable snapshots |
| Diff is the biggest risk | Confirmed — only Create in this feature | No precedent in the product |

## 5. Five-layer consistency check
| Layer | Status | Note / evidence |
|---|---|---|
| Visual | ✔ | Only existing tokens (`border`, `surface`, `muted`, `danger`, `primary`, `rounded-card`); `VersionDiff` built from them |
| Language | ◐ | Terms follow glossary and verb + object style; strings are inline like the rest of the app, not in `en.json` (debt #4) |
| Structure | ✔ | Tab on detail page; no new nav item; role visibility per `roles.md` |
| Behaviour | ✔ | Same table, badge, confirmation; all states specified |
| Functional | ◐ | Depends on a versions API and auth context for role (not in this repo) |

Summary: `Visual ✔ · Language ◐ · Structure ✔ · Behaviour ✔ · Functional ◐`
To reach full ✔: move strings to i18n; confirm the API returns author, date, summary and conditions per version.

## 6. Trade-offs
| Accepted cost | Who | Why accepted | Follow-up |
|---|---|---|---|
| One more tab on Rule detail | Data scientists, managers | Keeps history in context; cheaper than a new section | Watch tab usage |
| Managers can't see that restore exists | Managers | Less clutter; consistent with area-level hiding | Validation task 4; revisit if managers are confused |
| Shared component changes (4) | All features using them | Small, optional, backward compatible; avoids copies | Review existing usages in PR |
| No toast after restore | Data scientists | Product has no toast pattern; adding one is a bigger decision | Consider a product-wide feedback pattern (new debt candidate) |

## 7. System impact
- **Remove / merge proposals:** none for this feature. The engineering restore process (PRD problem) can be retired.
- **New unification debt found:** #1 two confirm dialogs, #2 hand-rolled table on Cases, #3 vague "Plans" label, #4 i18n not used, #5 no convention for actions a role can't perform. See `system-map/debt.md`.
- **System Map updates made:** `ia-tree.md` (Versions tab), `roles.md` (new row), `journeys.md` (2 journeys), `glossary.md` (Version, Restore version, Compare), `patterns.md` (DataTable/StatusBadge/ConfirmModal variants, VersionDiff), `global-patterns.md` (permission convention proposal), `debt.md` (#1–#5).
- **Open questions:** Does the backend keep full condition snapshots per version? Should restoring require a summary note?

---
<details><summary>Technical notes</summary>

See `components/README.md`. Generated: `RuleVersionsTab.tsx`, `VersionDiff.tsx`; patches for `DataTable`, `ConfirmModal`, `StatusBadge`, `Button`; wiring diff for `RuleDetailPage`. To wire: versions list/restore API, current role from auth context.
</details>
