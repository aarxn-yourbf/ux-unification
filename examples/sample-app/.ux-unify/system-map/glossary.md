# Glossary

| User-facing term | Meaning | Where used | Internal name | Notes |
|---|---|---|---|---|
| Alerts | Transactions flagged for review | Sidebar, AlertsPage | alerts | |
| Cases | Grouped investigation work | Sidebar, CasesPage | cases | |
| Rules | Conditions that score transactions | Sidebar, RulesPage | rules | |
| Plans | Data preparation configs | Sidebar, PlansPage | plans | Vague; users likely mean data transformations — debt #3 |
| Activity | Timeline of events on a case | CaseDetailPage tab | — | Events, not versions |
| Save changes | Primary save verb | RuleDetailPage, en.json `common.save` | — | Pattern: verb + object |
| Delete | Destructive action | RuleDetailPage, ConfirmModal default | — | |
| Version | A saved snapshot of a rule | NEW (rule-version-history) | — | PRD called the list "Change log"; tab is "Versions" |
| Restore version | Create a new version from an old one | NEW | rollback | PRD "Restore this version" shortened to verb + object |
| Compare | Show differences between two versions | NEW | diff | |
