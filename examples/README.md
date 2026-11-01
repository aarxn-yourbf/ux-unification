# Examples

- `prd-rule-version-history.md`: the input PRD.
- `sample-app/src/`: a small React + TypeScript + Tailwind app (a fictional risk-management tool) used as the "current experience". It deliberately contains some inconsistency: two confirm dialogs, a hand-rolled table, a vague nav label, and inline strings despite i18n.
- `sample-app/.ux-unify/`: the full output of running the skill on that app with that PRD.

Try it yourself: delete `sample-app/.ux-unify/`, give your AI assistant the PRD and the `sample-app` folder (with the skill installed), and compare.
