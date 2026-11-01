# Placement guide

Placement decides where a feature lives in the information architecture, how users reach it and who sees it. It comes before pattern choice because the right pattern depends on context: the same "list of items" is a full page in one place and a side panel in another.

## Questions to answer

1. **Which top-level area?** Match the feature to the area whose users and jobs it serves, not to the team that builds it. If areas are split by role or mode of work (e.g. "Investigation" for analysts reviewing alerts vs. "Strategy" for people defining rules and models), use that split.
2. **Which level?** Top-level nav, section, page, tab within a page, panel, or contextual action. Go as deep as is natural; every top-level item competes for attention for every user.
3. **Entry points.** Where is the user when they need this? Put the entry point on that path (a button on the page they're already on beats a new nav item). List all entry points: nav, contextual actions, empty states, notifications, deep links.
4. **Visibility by role.** Who needs it, who doesn't. Hide what a role never uses: irrelevant options add cognitive load. Follow the product's existing convention for no-permission states (hide vs disable vs explain) from `global-patterns.md`.
5. **Journey fit.** Where does the user come from, where do they go next? The feature should continue an existing journey, not create a detour.
6. **Global patterns.** Which cross-cutting rules apply: context switcher, breadcrumbs, page header, notifications, confirmation dialogs.
7. **Scale.** Will this area hold 3 more siblings next year? Prefer placements that stay sensible as the product grows.

## Heuristics

- A feature used often by one role goes where that role works, not where the data technically belongs.
- A configuration of an existing object goes with that object (settings tab, side panel), not in a global "Settings" bucket.
- An action on many items goes on the list (bulk action), not on a new page.
- A new top-level nav item needs a strong reason: a distinct, frequent job for a primary role.
- If two placements are plausible and the choice is hard to reverse, that is a medium-confidence decision: present both.

## Common mistakes

- Placing by org chart or backend service ("this is the Reporting team's feature, so it goes under Reports").
- Creating a new section for one feature.
- Duplicating entry points with different labels.
- Making a feature visible to all roles because "it's harmless".

## Output format (in `analysis.md`)

```
## Placement
Area: Strategy › Rules
Level: tab "Versions" on Rule detail page (RuleDetailPage.tsx)
Entry points: (1) tab on Rule detail; (2) "View history" link in rule list row menu (RulesTable.tsx L88)
Visibility: Data scientist ✔, Fraud manager ✔ (read-only), Analyst ✖ (never edits rules — roles.md)
Journey: Edit rule → Save → [new] Compare with previous version → Publish
Global patterns: tabs (Tabs.tsx), read-only state convention (disabled + tooltip), confirm on revert (ConfirmModal)
Confidence: high — mirrors "Activity" tab on Case detail (CaseDetailPage.tsx)

IA branch:
Strategy
└── Rules
    └── Rule detail
        ├── Definition
        ├── Performance
        └── Versions   ← NEW
```
