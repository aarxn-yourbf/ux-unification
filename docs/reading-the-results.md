# Reading the results

After a run, you'll have a folder like this:

```
.ux-unify/
├── system-map/             ← the assistant's picture of your whole product (reused next time)
└── features/<your-feature>/
    ├── rationale.md        ← 1. read first
    ├── pattern-spec.md     ← 2. the design in detail
    ├── analysis.md         ← 3. the thinking behind placement and naming
    ├── validation-plan.md  ← 4. how to test it with users
    ├── hypothesis.md       ← the assistant's first guess, for comparison
    └── components/         ← code for your developer (only if you shared code)
```

You don't need to read everything. Here's what each file is for and what to do with it. Examples come from the sample in [`examples/sample-app/.ux-unify/`](../examples/sample-app/.ux-unify/).

---

## 1. `rationale.md`: the decisions

**Read this first. It's written for non-technical readers.**

| Section | What it tells you | What to do |
|---|---|---|
| **Decision summary** | Where the feature lives and what it's made of, in 3–5 lines | Check it matches your intent |
| **Needs your review** | Decisions the assistant wasn't sure about | **Make these calls.** Each has a recommendation; you can accept it or pick the alternative |
| **Why these patterns** | Each choice, with the places in your product it already appears | Skim. This is the evidence |
| **What was adapted** | Every change to an existing pattern, tied to a line in your PRD | Check nothing surprising was changed |
| **Hypothesis vs. outcome** | What the assistant first assumed vs. what it decided, and why | Often the most insightful part |
| **Five-layer check** | Consistency score: Visual · Language · Structure · Behaviour · Functional | Anything ◐ or ✖ comes with a to-do |
| **Trade-offs** | What you give up and how it's compensated | Agree or push back |
| **System impact** | Things to remove or merge, new inconsistencies found | Add to your backlog |

**In the sample:** the first guess was a separate "Change log" page. After looking at how people actually edit rules, it moved history into a **Versions tab** on the rule's own page. Users need it right after making a change, and the product already uses tabs on detail pages.

---

## 2. `pattern-spec.md`: the design

A complete description of the screen, precise enough to design or build from.

- **Placement:** where it lives, how people get there, who can see it.
- **Decisions table:** each need from your PRD, the pattern chosen, and how confident the assistant is.
- **Layout and flow:** top-to-bottom description and the step-by-step path through it.
- **States:** what the screen looks like when it's empty, loading, failing, succeeding, or when the user lacks permission. These are often forgotten and cause inconsistency.
- **Options A/B:** for uncertain decisions, both options with pros and cons.
- **Microcopy:** every label and message, taken from your product's existing vocabulary.

**What to do:** hand it to your designer as the brief, or to your developer alongside the code.

---

## 3. `analysis.md`: the thinking

- **Journeys:** which existing flow this extends.
- **Overlap:** does this duplicate something you already have? Could something be retired?
- **Terminology:** where your PRD uses different words than your product, with a recommendation. Example: the PRD said "Change log", the product context suggested "Versions".
- **Conflicts:** places your PRD asks for something that breaks an existing convention.

**What to do:** use the overlap and terminology tables in your next planning conversation.

---

## 4. `validation-plan.md`: testing with users

A ready-made usability test: who to recruit, tasks phrased in users' language, questions to ask afterwards, and the **success bar** (decided before testing, so results can't be rationalised afterwards).

**What to do:** run it with 5–8 people per user role, ideally on a prototype. Bring results back to the assistant: *"Here are the test results, update the design and System Map."*

---

## 5. `components/`: for your developer

Only present if you shared code. It contains:
- **New files** (e.g. `RuleVersionsTab.tsx`) built from components your product already has.
- **Patches** (files ending in `.diff`) for existing components that need a small new option. These are deliberately small and backward-compatible, so other screens don't change.
- A **README** saying where each file goes.

Nothing has been changed in your actual product. A developer reviews and applies it.

---

## The System Map

`system-map/` is the assistant's model of your product. It is **reused and updated** every run, so each feature makes the next one easier.

The most immediately useful file for most teams is **`debt.md`**: a list of inconsistencies that already exist in your product, with evidence and suggested fixes. In the sample, the skill found two different confirmation dialogs, a table built differently from all the others, and a menu label ("Plans") that doesn't say what it does.

**What to do:** keep the folder. In a repo, commit it. In a chat app, save the files or add them to your chat project's knowledge.

---

## Symbols you'll see

| Symbol | Meaning |
|---|---|
| ✔ / ◐ / ✖ | pass / partial / fail (consistency check) · or uses / sees read-only / hidden (role tables) |
| **High / Medium / Low** confidence | High = decided. Medium/Low = options given, needs your review |
| `[GROUNDED]` | Seen in your product; a file or screenshot is cited |
| `[INFERRED]` | A reasonable deduction, not directly confirmed. Correct it if wrong |
| `[SPECULATIVE]` | A guess, also listed as an open question. Answer it |
| `← NEW` | Where the new feature sits in the product structure |
| **Reuse / Extend / Compose / Create** | Use as-is / add a small option / combine existing pieces / build new (needs a reason) |
