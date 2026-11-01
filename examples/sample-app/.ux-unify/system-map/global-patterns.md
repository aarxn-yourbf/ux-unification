# Global patterns

- **Navigation:** left Sidebar with two sections (Investigation, Strategy). Detail pages reached from list rows. (`Sidebar.tsx`, `RulesPage.tsx`)
- **Page structure:** `PageHeader` (title + actions) then content. (`PageHeader.tsx`)
- **Object detail:** `PageHeader` + `Tabs`. (`RuleDetailPage.tsx`, `CaseDetailPage.tsx`)
- **Destructive confirmation:** `ConfirmModal` with Cancel (secondary) + action (danger) right-aligned. (`ConfirmModal.tsx`)
- **Empty / loading:** handled inside `DataTable` (pulse block, `EmptyState`).
- **Permissions:** area-level role lists in `permissions.ts` with `hasPermission`. No convention yet for actions within an allowed area *(proposed in rule-version-history: hide actions the role cannot perform)*.
- **Microcopy:** buttons are verb + object, sentence case ("Save changes", "New rule").
- **i18n:** `react-i18next` installed and `en.json` exists, but pages use inline strings (debt #4).
