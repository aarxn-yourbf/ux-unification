# Decision ladder

For every UI need in the PRD, climb from the bottom rung up and stop at the first one that works. The burden of proof increases with each rung.

## 1. Reuse
An existing pattern does exactly this job in this kind of context.
- Evidence: file paths where it is used for the same job.
- Allowed changes: content, labels, data. No new props.

## 2. Extend
An existing pattern is a close match; add a variant, prop or slot.
- Evidence: the original component and why it almost fits.
- Rule: change the original (patch/diff), don't copy it. Check the change doesn't break existing usages (list them).
- Typical: new column type, new variant of a badge, optional footer slot.

## 3. Compose
Existing components combine into the needed pattern.
- Evidence: each building block and where it's used.
- Rule: the composition should look like it was always there. If the product already composes similar things somewhere, copy that composition's structure.

## 4. Create
Nothing above works.
- Required: a written reason why rungs 1–3 fail (not "it's nicer").
- Build from existing tokens and primitives; it should be visually indistinguishable in style from the rest.
- Register it in `patterns.md` as a new pattern so the next feature can reuse it.
- Ask: is this need actually common? If yes, it may belong in the design system; note that as a proposal.

## Confidence rubric

Score each decision. The thresholds borrow the logic of card-sort analysis: strong agreement is decided directly; split agreement gets a careful look by product and UX together.

| Confidence | Signals | What to do |
|---|---|---|
| **High** | Pattern used ≥3 times for the same job; PRD needs fit without conflict; placement is obvious | Decide. One-line justification + evidence |
| **Medium** | Pattern used for a similar but not identical job; or 2 plausible patterns; or a PRD requirement bends a convention | Options A and B, recommend one, flag for review |
| **Low** | No precedent; PRD conflicts with a global pattern; placement unclear; stack unfamiliar | Options A and B (or more), state the assumption each needs, recommend validation before build |

## Options A/B format

```
### Need: navigate between rule versions
Option A — Tabs on Rule detail (Reuse: Tabs.tsx, used in CaseDetail, AlertDetail)
+ Users always see which level they are on
+ Consistent with other detail pages
− One extra click to reach versions
Assumes: versions are viewed in the context of one rule

Option B — Separate "Versions" page in Rules section (Compose: PageHeader + DataTable)
+ Fewer clicks from the rules list
− New top-level-ish location; users may not know where they are
Assumes: users browse versions across many rules

Recommendation: A. Clarity of location beats one saved click; matches 2 existing detail pages.
Validate with: findability task #2 in validation-plan.md
```

When weighing options, remember a lesson from navigation A/B tests in complex products: the option with more clicks but clearer orientation often wins clearly. Don't optimise click count at the expense of "where am I?". The final design can still borrow the parts users liked from the losing option.
