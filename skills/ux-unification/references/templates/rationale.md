# Rationale — <Feature name>

## 1. Decision summary
Plain language, 3–5 lines: where the feature lives, which patterns it uses, what changed versus existing patterns, what needs review.

**Needs your review:** <list of Medium/Low confidence decisions, or "none">

## 2. Why these patterns
For each key decision:
- **Decision:** …
- **Evidence:** used in `path/a.tsx`, `path/b.tsx` (N usages) for <same job>.
- **Why it fits this PRD:** …

## 3. What was adapted for this PRD — and why
| Change vs. existing pattern | PRD requirement it serves | Impact on existing usages |
|---|---|---|

No change without a PRD reason. If a change was needed for technical reasons, say so.

## 4. Hypothesis vs. outcome
| Hypothesis (Step 1) | Final decision | Why it changed (or held) |
|---|---|---|

## 5. Five-layer consistency check
| Layer | Status | Note / evidence |
|---|---|---|
| Visual | ✔ / ◐ / ✖ | |
| Language | | |
| Structure | | |
| Behaviour | | |
| Functional | | |

Summary: `Visual ✔ · Language ✔ · Structure ✔ · Behaviour ◐ · Functional ✔`
To reach full ✔: …

## 6. Trade-offs
| Accepted cost | Who is affected | Why accepted | Compensation / follow-up |
|---|---|---|---|

## 7. System impact
- **Remove / merge proposals:** …
- **New unification debt found:** … (added to `system-map/debt.md` #…)
- **System Map updates made:** ia-tree, roles, journeys, glossary, patterns, debt.
- **Open questions:** …

---
<details><summary>Technical notes</summary>

Files generated, where they go, what to wire (routes, permissions, API), patches to existing components and the usages they touch.
</details>
