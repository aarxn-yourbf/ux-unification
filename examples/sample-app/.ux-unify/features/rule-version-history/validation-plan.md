# Validation plan — Rule version history & rollback

## Hypotheses
1. Data scientists find versions from Rule detail without help (Versions tab, not a separate page).
2. "Versions" and "Restore version" are understood correctly; "Restore" is understood as *creating a new version*, not overwriting.
3. Row checkboxes (Option A) let users compare any two versions faster and more successfully than "Compare with active" (Option B).
4. Managers don't miss the hidden restore action (Option A for permissions).

## Participants
| Role | Count | Must have |
|---|---|---|
| Data scientist | 6 | Edits rules at least weekly |
| Manager | 4 | Reviews rule changes |

## Format
Moderated, 30 min, clickable prototype (high fidelity, built from existing components). A/B for Decision 4: half of data scientists see A, half see B (5 each if recruiting allows 10).

## Tasks
| # | Role | Task | Expected path | Measures |
|---|---|---|---|---|
| 1 | DS, Mgr | "Rule *High-value card-not-present* started flagging too many transactions yesterday. Find out what changed." | Rules → rule → Versions → tick 2 → Compare | success, first click, difficulty 1–7 |
| 2 | DS | "Put the rule back the way it was last week." | Versions → Restore version on v6 → confirm | success, time (target < 1 min), difficulty |
| 3 | DS | "Compare version 4 with version 6." | tick v4 + v6 → Compare (A) | success A vs B |
| 4 | Mgr | "Could you undo this change yourself? What would you do?" | Recognises they can't; knows to ask a data scientist | comprehension |
| 5 | All | "What do you think will happen when you press *Restore version*?" | "A new version with the old conditions" | comprehension |

## Post-session questions
- How well would this match your work process and needs? (1–7)
- How intuitive was it to find and use? (1–7)
- Did anything work differently from the rest of the product?
- What did you like? What should improve?

## Success thresholds (set before testing)
- Overall task success ≥ 70% (familiar area, small feature)
- Task 2 median time < 60 s (PRD metric)
- Task 5 comprehension ≥ 80%
- A/B: Option A is kept if it is not more than 10 points worse than B on task 1 and wins on task 3
- Satisfaction ≥ 5 / 7

## After testing
Update `pattern-spec.md` (selection model, copy), `glossary.md` ("Versions", "Restore version"), `system-map/global-patterns.md` (permission convention), `debt.md`.
