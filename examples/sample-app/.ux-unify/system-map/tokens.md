# Tokens

Source: `src/styles/tokens.css`, mapped in `tailwind.config.js`.

| Token | Tailwind | Value |
|---|---|---|
| --color-primary | `primary` | #2563eb |
| --color-surface | `surface` | #ffffff |
| --color-border | `border` | #e5e7eb |
| --color-danger | `danger` | #dc2626 |
| --color-muted | `muted` | #6b7280 |
| --radius-card | `rounded-card` | 12px |
| --space-page | — | 24px (not mapped in Tailwind) |

Hard-coded values: 2 hex colors in `DeleteDialog.tsx` (debt #1). `StatusBadge.tsx` uses Tailwind palette classes (green/yellow) instead of semantic tokens *(minor)*.
No success/warning tokens exist; status colors live inside `StatusBadge`.
