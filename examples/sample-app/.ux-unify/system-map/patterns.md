# Pattern registry

### Page header
- Component: `src/components/ui/PageHeader.tsx` — used in 6 files (every page)
- Title left, actions right.

### Data table
- Component: `src/components/ui/DataTable.tsx` — used in AlertsPage, RulesPage (+ RuleVersionsTab, NEW)
- Built-in loading (pulse block) and empty state (`EmptyState`). Row click navigates.
- Variant added: `selectable` + `maxSelected` (rule-version-history, Extend).
- Divergence: CasesPage uses a hand-rolled `<table>` (debt #2).

### Tabs (detail pages)
- Component: `src/components/ui/Tabs.tsx` — RuleDetailPage, CaseDetailPage
- Peer views of one object. Rule detail gains "Versions".

### Status badge
- Component: `src/components/ui/StatusBadge.tsx` — AlertsPage, RulesPage (+ RuleVersionsTab)
- Statuses: active, draft, paused; `archived` added (rule-version-history, Extend).

### Confirm dialog
- Component: `src/components/ui/ConfirmModal.tsx` — RuleDetailPage (+ RuleVersionsTab)
- Variant added: `confirmVariant` (default "danger") so non-destructive confirmations use primary.
- Divergence: `DeleteDialog.tsx` on CasesPage (debt #1).

### Empty state
- Component: `src/components/ui/EmptyState.tsx` — DataTable, PlansPage (+ RuleVersionsTab)

### Version diff (NEW, Create)
- Component: `VersionDiff.tsx` (rule-version-history). Side-by-side comparison of rule conditions. Reusable for any versioned object.
