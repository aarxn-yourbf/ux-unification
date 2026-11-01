# The five unification layers

A feature feels like "part of the product" only when it is consistent on all five layers. Visual consistency is the most noticed and the easiest; functional consistency is the hardest and often the most valued by daily users.

Use this as a checklist in Step 7 (and as a self-check while generating code in Step 5). Mark each item **pass / partial / fail / n.a.** with a one-line note and file evidence.

## 1. Visual
- [ ] Only existing tokens (color, spacing, type, radius, shadow); no hard-coded values.
- [ ] Only existing components/primitives, or a documented Extend/Create.
- [ ] Icons from the project's icon set; same sizes as neighbours.
- [ ] Layout grid, page header and density match sibling pages.
- [ ] Theme support (light/dark) works if the product has it.

## 2. Language
- [ ] Every user-facing term exists in the glossary or is added with a reason.
- [ ] No internal/technical terms leak into the UI.
- [ ] Button verbs, casing and tone match existing microcopy.
- [ ] Error and empty-state messages follow the product's structure.
- [ ] Strings go through i18n if the product uses it.

## 3. Structure
- [ ] Placement follows the IA (area, level) and is reachable from the user's journey.
- [ ] No new top-level item without strong justification.
- [ ] Breadcrumbs / tabs / section nav behave like siblings.
- [ ] Role visibility matches the role matrix.

## 4. Behaviour
- [ ] Same interaction for the same job (open, edit, save, cancel, delete, confirm).
- [ ] All states present: empty, loading, error, success, no permission, partial data.
- [ ] Keyboard, focus and accessibility behaviour match existing components.
- [ ] Feedback (toasts, banners, inline) follows global conventions.

## 5. Functional
- [ ] Works within the existing auth/session (no extra login).
- [ ] Respects context switching (workspace/tenant/use case) and keeps state when switching.
- [ ] Uses the same data conventions (formats, filters, sorting, pagination behaviour).
- [ ] Deep links and back/forward navigation behave as elsewhere.

## Summary line
End the check with a single line: `Visual ✔ · Language ✔ · Structure ✔ · Behaviour ◐ · Functional ✔` and list what's needed to turn any ◐/✖ into ✔.
