# Pattern catalog

Use these names in specs and in `patterns.md` so the team shares one vocabulary. When the product already has its own name for a pattern, use the product's name and map it here.

## Navigation & orientation
- **Global nav** (sidebar / top bar): top-level areas.
- **Section nav**: secondary navigation within an area (sub-sidebar, horizontal tabs under header).
- **Tabs**: peer views of one object.
- **Breadcrumbs**: location in deep hierarchies.
- **Context switcher**: change workspace / tenant / use case / product mode without logging out.
- **Command palette / global search**.
- **Deep link**: URL that opens a specific state.

## Collections
- **Data table**: dense, sortable, comparable records; bulk actions.
- **List**: simpler rows, less comparison.
- **Card grid**: visual items, browsing.
- **Master–detail**: list + detail panel side by side.
- **Filters & facets**, **saved views**, **pagination / infinite scroll**.
- **Bulk action bar**: appears on selection.

## Objects
- **Detail page**: header (title, status, primary actions) + tabs/sections.
- **Side panel / drawer**: quick view or edit without leaving the list.
- **Inline edit**.
- **Activity / history / versions** timeline.
- **Status badge**.

## Creation & editing
- **Form page**, **modal form** (short forms only), **drawer form**.
- **Wizard / stepper**: multi-step with dependency between steps.
- **Builder**: compose rules/queries/flows (condition builder, visual editor).
- **Templates**: start from a preset.
- **Draft / publish** with diff/compare.

## Feedback & safety
- **Toast** (transient success), **inline alert/banner** (persistent context), **validation messages**.
- **Confirm dialog** for destructive/irreversible actions; **undo** as a lighter alternative.
- **Empty state**: first-use (explain + CTA), no-results (clear filters), no-permission (explain + who to ask).
- **Loading**: skeleton, spinner, progress for long jobs.
- **Error state**: what happened + what to do.

## Data display
- **KPI / stat tile**, **chart**, **dashboard**, **comparison / diff view**.

## Settings & permissions
- **Settings page** (grouped sections), **object-level settings tab**.
- **Role-based visibility**: hide vs disable vs explain (follow `global-patterns.md`).

## Choosing quickly
| Need | Usually |
|---|---|
| Compare many records | Data table |
| Edit a few fields fast | Side panel or inline edit |
| Long or multi-part input | Form page or wizard |
| Peer views of one thing | Tabs |
| Action on many items | Bulk action bar |
| Track changes over time | Activity/versions + diff |
| Irreversible action | Confirm dialog (or undo if reversible) |
