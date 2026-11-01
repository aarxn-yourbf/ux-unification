# IA tree

Source: `src/components/layout/Sidebar.tsx` (navItems), `src/routes.tsx`.

```
Sample app
├── Investigation                       (Sidebar section)
│   ├── Alerts            /alerts       → pages/AlertsPage.tsx
│   └── Cases             /cases        → pages/CasesPage.tsx
│       └── Case detail   /cases/:id    → pages/CaseDetailPage.tsx  [tabs: Overview, Activity]
└── Strategy                            (Sidebar section)
    ├── Rules             /rules        → pages/RulesPage.tsx
    │   └── Rule detail   /rules/:id    → pages/RuleDetailPage.tsx  [tabs: Definition, Performance, Versions ← NEW]
    └── Plans             /plans        → pages/PlansPage.tsx  (label "Plans" is vague — see debt #3)
```

Detail pages are reached from list rows (`DataTable onRowClick`, `RulesPage.tsx`), not from navigation.
