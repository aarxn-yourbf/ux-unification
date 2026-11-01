import { createBrowserRouter } from "react-router-dom";
import { AppShell } from "./components/layout/AppShell";
import { AlertsPage } from "./pages/AlertsPage";
import { CasesPage } from "./pages/CasesPage";
import { CaseDetailPage } from "./pages/CaseDetailPage";
import { RulesPage } from "./pages/RulesPage";
import { RuleDetailPage } from "./pages/RuleDetailPage";
import { PlansPage } from "./pages/PlansPage";
export const router = createBrowserRouter([
  { path: "/", element: <AppShell />, children: [
    { path: "alerts", element: <AlertsPage /> },
    { path: "cases", element: <CasesPage /> },
    { path: "cases/:id", element: <CaseDetailPage /> },
    { path: "rules", element: <RulesPage /> },
    { path: "rules/:id", element: <RuleDetailPage /> },
    { path: "plans", element: <PlansPage /> },
  ]},
]);
