# Generated components — rule-version-history

Proposals only. Nothing here has been applied to `src/`.

| File | Type | Goes to | Notes |
|---|---|---|---|
| `RuleVersionsTab.tsx` | Compose | `src/pages/rules/RuleVersionsTab.tsx` | The Versions tab. Uses only existing components |
| `VersionDiff.tsx` | Create | `src/components/ui/VersionDiff.tsx` | New pattern, registered in `patterns.md` |
| `DataTable.selectable.diff` | Extend | `src/components/ui/DataTable.tsx` | Optional selection; existing usages unchanged (AlertsPage, RulesPage) |
| `ConfirmModal.confirmVariant.diff` | Extend | `src/components/ui/ConfirmModal.tsx` | Default "danger" kept; RuleDetailPage unchanged |
| `StatusBadge.archived.diff` | Extend | `src/components/ui/StatusBadge.tsx` | Adds `archived` |
| `Button.disabled.diff` | Extend | `src/components/ui/Button.tsx` | Adds `disabled` |
| `RuleDetailPage.wiring.diff` | Wiring | `src/pages/RuleDetailPage.tsx` | Adds the tab |

To wire: versions API (list + restore), current role from auth context, and moving new strings to `src/locales/en.json` (debt #4).
