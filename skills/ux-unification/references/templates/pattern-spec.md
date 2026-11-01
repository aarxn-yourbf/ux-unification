# Pattern spec — <Feature name>

> PRD: <link or file> · System Map: <commit/date> · Author: ux-unification

## 1. Summary
One paragraph in plain language: what the user can do, where it lives, which main patterns it uses.

## 2. Placement
- Area / level: …
- Entry points: …
- Visibility by role: …
- IA branch (new node marked ← NEW):
```
…
```

## 3. UI needs → pattern decisions
| # | Need (from PRD) | Rung | Pattern / component | Evidence (files) | Confidence |
|---|---|---|---|---|---|
| 1 | | Reuse / Extend / Compose / Create | | | High / Med / Low |

Options A/B for any Medium/Low decisions: see section 7.

## 4. Layout
Describe the screen(s) top to bottom (page header, primary actions, content regions, secondary panels). Reference sibling pages it mirrors.

## 5. Flow
Step-by-step user flow, including where the user comes from and goes next.
```
<Entry> → <Step> → <Step> → <Exit>
```

## 6. States
| State | Trigger | What the user sees | Component |
|---|---|---|---|
| Empty (first use) | | | |
| Empty (no results) | | | |
| Loading | | | |
| Error | | | |
| Success | | | |
| No permission | | | |
| Partial data | | | |

## 7. Options (Medium/Low confidence decisions)
### Decision: …
Option A — … (+/−, assumes …)
Option B — … (+/−, assumes …)
Recommendation: … because …

## 8. Microcopy
| Element | Text | Glossary term / source |
|---|---|---|

## 9. Responsive / accessibility notes
…
