# Analysis — Rule version history & rollback

## PRD summary
- **Goal:** see, compare and restore previous versions of a rule; rollback < 1 min.
- **Roles:** Data scientist (primary, restores) · Manager (views and compares, cannot restore).
- **Tasks:** list versions → pick two → compare → restore one (with confirmation).
- **Data:** version number, author, date, status, change summary, rule conditions.
- **States:** empty (only one version), loading, error, no permission (manager restore), success (restored).

## Journeys
Extends the existing **Maintain a rule** journey (Rules → Rule detail). The new step sits right after "Save changes": the user who just saved and saw a problem in Performance needs to go back. This is a strong reason to keep the feature *inside* Rule detail rather than in a separate page.

## Overlap
- No existing version or history feature for rules.
- Case detail has an **Activity** tab (`CaseDetailPage.tsx`) — events on a case, not versions. Different concept; do not reuse the label "Activity".
- Nothing becomes obsolete. Engineering-run DB restores (PRD problem) are the manual process this replaces.

## Terminology
| PRD term | Existing term | Proposal | Reason |
|---|---|---|---|
| "Change log" | — | **Versions** (tab label) | Users act on versions (compare, restore), not on a log; shorter as a tab next to "Definition", "Performance" |
| "Restore this version" | "Save changes" pattern (verb + object) | **Restore version** | Matches existing button copy style |
| "Diff" (implied) | — | **Compare** | Avoid technical term; "diff" is engineering language |
| "Fraud manager" | "manager" role | Manager | Same role in `permissions.ts` `[INFERRED]` |

## Conflicts with established patterns
1. `ConfirmModal` always renders the confirm button as `danger`. Restoring is not destructive (it creates a new version). → Extend `ConfirmModal` with `confirmVariant`.
2. `DataTable` has no row selection, PRD requires choosing two versions. → Extend `DataTable` (medium confidence, see options).
3. No convention for an action a role can't perform (manager + restore). → propose "hide" (medium confidence).

## Placement
```
Area: Strategy › Rules
Level: tab "Versions" on Rule detail (RuleDetailPage.tsx), after Definition and Performance
Entry points: (1) Versions tab on Rule detail
              (2) after "Restore version", user lands on Definition with a banner-less success state (toast not available — see note)
Visibility: Data scientist ✔ view + compare + restore · Manager ○ view + compare · Analyst ✖ (no Rules access)
Journey: Rules → Rule detail → Definition → Save changes → Performance → [Versions → Compare → Restore version]
Global patterns: PageHeader + Tabs (detail), DataTable (lists), ConfirmModal (confirmation), EmptyState
Confidence: high — mirrors detail-page tab structure in CaseDetailPage.tsx and RuleDetailPage.tsx

Strategy
└── Rules
    └── Rule detail
        ├── Definition
        ├── Performance
        └── Versions   ← NEW
```
Note: the product has no toast/notification component. Success after restore is shown by switching to the Definition tab with the new version number in the header subtitle (no new pattern introduced).
