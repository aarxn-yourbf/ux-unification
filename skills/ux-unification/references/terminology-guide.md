# Terminology guide

Language is a layer of the experience. Users build their mental model from labels, so two words for one concept (or one word for two concepts) quietly breaks the feeling of a single product. Unification projects consistently find that naming is one of the hardest and most valuable parts.

## Checks to run on every PRD

1. **New name for an existing concept.** Compare every noun in the PRD with `glossary.md`. If the PRD says "Workspace" and the product says "Project" for the same thing, keep the existing term unless there is a strong reason to rename everywhere (then that's a debt item, not a local change).
2. **Same name, different concept.** If the PRD reuses an existing label for something new, propose a distinct label.
3. **Leaked internal language.** Flag terms that come from the implementation or the org rather than the user's job: service names, table/model names, codenames, team names, acronyms users don't use. A strong signal: a concept that research participants consistently remove or rename when sorting is an internal concept, not a user one.
4. **Label describes the goal.** Prefer labels that say what the user achieves. Abstract labels ("Plans", "Engine", "Hub", "Center") are a smell; ask "what does the user do there?" and name that ("Data transformations": clean, change, map data).
5. **User vocabulary vs. product vocabulary.** If support/success teams or customers describe the job with different words than the product, the product is probably wrong. When unsure, keep the original term and add a short description (a pattern used in card-sort preparation), and list the naming for validation in Step 6.

## Output

In `analysis.md`, a table:

| PRD term | Existing term (glossary) | Proposal | Reason |
|---|---|---|---|
| "Job" | "Rule run" (`RunsPage.tsx`) | Use "Rule run" | Same concept, existing term in 6 screens |
| "Pipeline config" | — | "Data transformations" | PRD term is internal; users describe the goal |

Then use the proposed terms consistently in the pattern spec, microcopy and generated code, and add new terms to `glossary.md` in Step 7.

## Microcopy consistency

Match existing conventions for: button verbs (Save vs Submit vs Apply), sentence vs title case, destructive action wording, empty-state tone, error message structure (what happened + what to do). Find two or three existing examples in code and mirror them.
