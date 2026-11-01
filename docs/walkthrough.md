# UX Unification: Detailed Walkthrough

This guide breaks down every command in the skill: what it does, when the agent activates it, when you should reach for it, and how to get the most from it. It is written for product designers, PMs and engineers working with any AI assistant.

> **⚡ Pro Tip:** You don't need long prompts. Once the skill is installed, start a message with a command (`/unify`, `/audit`…) and attach what you have. Everything after the command is treated as input.

---

## How the pieces fit

```
          ┌──────────── /map ────────────┐
          ▼                              │
   System Map ──► /place ──► /pattern ──► /build ──► validation ──► /handoff
          ▲            🛑            🛑                               │
          │                                                          │
          └──── every run updates the map ◄── /audit, /debt ◄────────┘
```

`/unify` runs the whole chain. The other commands let you run one part, or come back to a part later.

---

## /unify: Full workflow
- **What it does:** Steps 0–7. Builds or loads the System Map, writes a hypothesis, analyses the PRD, decides placement, chooses patterns, generates components, writes a validation plan and a rationale, and updates the System Map.
- **When the agent activates:** you share a PRD or feature idea together with your product and ask for UI, a design or "where should this go".
- **When you should use it:** the first time a feature is designed, or when you want everything in one go.
- **Pro tip:** expect two pauses, at **placement** and at **uncertain decisions**. Answering them takes a minute and is where your judgment matters most. Say *"don't stop, use your recommendations"* if you'd rather review at the end.

## /map: Build or refresh the System Map
- **What it does:** creates `.ux-unify/system-map/`: the product's structure, roles, journeys, glossary, tokens, patterns, product-wide rules, and existing inconsistencies.
- **When the agent activates:** automatically at the start of every run if no map exists, or if the product changed since the last update.
- **When you should use it:** once per product before your first feature, after a big redesign, or when onboarding a new designer or engineer. The map doubles as documentation.
- **Pro tip:** for a monorepo or a product family, say which apps to include. The most valuable output is the list of **the same job done differently across apps**.

## /place: Decide where a feature lives
- **What it does:** hypothesis, PRD analysis (journeys, overlaps, naming, conflicts) and placement (area, level, entry points, who sees it).
- **When the agent activates:** when you ask "where should this go?" or "who should see this?"
- **When you should use it:** early, before anyone opens a design tool. It's also good for PRD reviews: overlaps and naming conflicts surface here.
- **Pro tip:** read the **Overlap** section. "Adding is also a moment to remove" is often where the biggest wins hide.

## /pattern: Choose patterns and write the spec
- **What it does:** for each UI need, climbs **Reuse → Extend → Compose → Create**, rates confidence, writes Option A/B for uncertain decisions, and produces `pattern-spec.md` with layout, flow, every state and exact wording.
- **When the agent activates:** when you ask which component or pattern to use.
- **When you should use it:** to brief a designer, or to feed a UI-generation tool a spec that is already consistent with your product.
- **Pro tip:** a **Create** decision always comes with a written reason. If the reason is weak, push back. That's how one-off components are avoided.

## /build: Generate components
- **What it does:** writes components into `.ux-unify/features/<feature>/components/` using your own components, tokens and conventions, plus small `.diff` patches for shared components that need a new option.
- **When the agent activates:** after a spec is approved, in full mode (code available).
- **When you should use it:** when you want a developer-ready starting point, not production code.
- **Pro tip:** check `components/README.md` first. It lists where each file goes and what still needs wiring (APIs, permissions). Ask *"apply it to src/"* only when you're ready to change real code.

## /audit: Check something that already exists
- **What it does:** compares a screen, feature, PR or design (code, screenshot or description) with the System Map across the five layers (visual, language, structure, behaviour, functional) and returns findings with evidence, severity and a fix.
- **When the agent activates:** when you ask "does this fit?", "what's inconsistent here?" or share a PR for review.
- **When you should use it:** before design reviews and merges, and when a screen "feels off" but nobody can say why.
- **Pro tip:** findings are added to `debt.md`, so audits accumulate into a backlog instead of being forgotten.

## /debt: Prioritise existing inconsistencies
- **What it does:** lists everything in `debt.md`, ranked by user impact and effort, grouped by layer.
- **When you should use it:** sprint planning, design-system roadmaps, or building a business case for unification work.
- **Pro tip:** ask *"which three fixes would users notice most?"*. Unification gets funded when it's framed as user and business impact.

## /handoff: Pass context on
- **What it does:** writes `handoff.json` (summary, placement, decisions with confidence tags, items needing review, open questions, artifacts).
- **When you should use it:** passing work to another agent or skill, a teammate, or a future session.
- **Pro tip:** start a new session with *"here's the handoff.json"* instead of re-explaining. Less context lost, fewer invented details.

## /explain: Make it readable for anyone
- **What it does:** rewrites the latest rationale for a non-technical reader: decisions, why, and what needs a decision from them.
- **When you should use it:** before sharing with stakeholders, leadership or clients.

---

## Confidence tags at a glance

| Tag | Meaning | What to do |
|---|---|---|
| `[GROUNDED]` | Seen in your product; a file or screenshot is cited | Trust, spot-check |
| `[INFERRED]` | Deduced from grounded facts; reasoning given | Confirm if it matters |
| `[SPECULATIVE]` | A guess; also listed as an open question | Answer the question |
| **High / Medium / Low** | Confidence in a *decision* | Medium/Low come with options and need your call |
