# Unification debt

| # | Debt | Layer | Evidence | Impact | Suggested fix | Found in |
|---|---|---|---|---|---|---|
| 1 | Two confirm dialogs: `DeleteDialog` (Yes/No, hard-coded colors) vs `ConfirmModal` | Behaviour, Visual, Language | `ui/DeleteDialog.tsx`, `pages/CasesPage.tsx`, `ui/ConfirmModal.tsx` | Analysts and managers see different wording, colors and button order for the same job | Replace `DeleteDialog` with `ConfirmModal`; delete `DeleteDialog` | rule-version-history |
| 2 | Cases list uses a hand-rolled `<table>` instead of `DataTable` | Visual, Behaviour | `pages/CasesPage.tsx` | No loading/empty states; different styling | Migrate to `DataTable` | rule-version-history |
| 3 | "Plans" label doesn't describe the job | Language | `Sidebar.tsx`, `PlansPage.tsx` | Users can't predict content | Rename to a goal-based label, e.g. "Data transformations"; validate with users | rule-version-history |
| 4 | i18n set up but strings are inline | Language | `locales/en.json` vs pages | Copy drifts between screens | Move UI strings into `en.json` progressively | rule-version-history |
| 5 | No convention for actions a role can't perform | Structure, Behaviour | `permissions.ts` | Each feature will improvise | Adopt "hide" as the convention (see rule-version-history rationale) and record here | rule-version-history |
