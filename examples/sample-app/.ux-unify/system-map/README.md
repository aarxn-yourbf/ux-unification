# System Map — Sample app

- **Scope:** `src/` (single app) · **Last updated:** 2026-11-01 (feature: rule-version-history)
- **Stack:** React 18 + TypeScript, React Router v6 (`src/routes.tsx`), Tailwind with CSS-variable tokens (`src/styles/tokens.css`, `tailwind.config.js`), react-i18next (`src/locales/en.json`), lucide-react icons.
- **Known gaps:** no Storybook; roles are defined in `src/auth/permissions.ts` but navigation does not filter by them *(inferred: filtering may happen elsewhere)*; journeys are inferred from routes and pages, not from analytics.
