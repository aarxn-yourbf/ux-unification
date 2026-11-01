# Roles × areas

Source: `src/auth/permissions.ts`. ✔ uses · ○ sees, read-only · ✖ hidden

| Area | Analyst | Data scientist | Manager | Source |
|---|---|---|---|---|
| Alerts | ✔ | ✖ | ✔ | permissions.ts `alerts` |
| Cases | ✔ | ✖ | ✔ | permissions.ts `cases` |
| Rules | ✖ | ✔ | ✔ | permissions.ts `rules` |
| Rule detail › Versions (NEW) | ✖ | ✔ view + restore | ○ view only | PRD req. 4 |
| Plans | ✖ | ✔ | ✖ | permissions.ts `plans` |

Note: "Manager" is called "Fraud manager" in PRDs *(inferred same role)*.
