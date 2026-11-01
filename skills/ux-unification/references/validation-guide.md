# Validation guide

Unification decisions are hypotheses until users confirm them. A lightweight test plan, with the success bar set in advance, turns "we think it fits" into evidence, and evidence is what earns leadership support for unification work.

## What to test

1. **Findability**: can users find the feature from where they naturally are?
   - "You want to [goal in user language]. Where would you go?" (first-click and path)
2. **Comprehension**: do labels mean what we think?
   - "What would you expect to find under '[label]'?"
3. **Task completion**: can they do the primary task end to end in the prototype?
4. **Consistency perception**: does it feel like the rest of the product?
   - "Did anything here work differently from what you're used to in [product]?"

## Metrics

| Metric | How | Scale |
|---|---|---|
| Task success | Completed without help | % per task, per role, overall |
| Perceived difficulty | After each task | 1 (very hard) – 7 (very easy) |
| Satisfaction / fit with workflow | After session | 1 (doesn't improve at all) – 7 (drastically improves) |
| Expectations | "What did you expect to happen?" | Qualitative |
| First-click accuracy | Unmoderated tools (heatmaps, click paths) | % |

## Thresholds

Set them before testing and write them in the plan. Reference points:
- Complex B2B product, no onboarding or training: ~60% task success is a reasonable baseline; exceeding it is a strong result.
- Simpler or consumer flows: aim higher (75–85%).
- For A/B options: decide the margin that counts as a clear win (e.g. ≥15 points of task success).

## Participants

Recruit per role from `roles.md`; each role that sees the feature gets its own tasks. 5–8 per role finds most issues; ~10 per option for an A/B comparison. Require experience with the area being tested.

## Format

Moderated sessions for complex/expert products (participants unused to research exercises benefit from guidance); unmoderated prototype tests for findability and first-click at scale.

## Template content for `validation-plan.md`
Use `templates/validation-plan.md`. Include: hypotheses (from the rationale), participant profile, tasks (with expected path), metrics, thresholds, A/B script if any, and how results feed back (update `pattern-spec.md`, `glossary.md`, `debt.md`).
