# UX Unification (Agent Skill)

An AI agent skill that makes **every new feature feel like it was always part of your product**. It turns a general-purpose AI assistant into a product designer who knows your product: it maps how the product works today, decides where a new feature belongs, reuses what already exists, and explains every decision with evidence.

Works with **any AI assistant or coding agent** that supports `SKILL.md` skills (Claude, Codex, Cursor, GitHub Copilot, Gemini CLI, Junie and others), and with plain chat assistants as custom instructions.

📚 **[Read the Walkthrough](./docs/walkthrough.md)**: when and how to use each command in your day-to-day design work.
🧭 **New to AI skills or not a developer?** Start with **[Getting started](./docs/getting-started.md)**.

---

## 🧩 The Problem It Solves

Products rarely become inconsistent because of bad taste. They become inconsistent **one reasonable decision at a time**. A feature is designed on a blank canvas, so it gets its own table style, its own word for an old concept, its own place in the menu. Each choice makes sense alone. Together, they make the product feel like several products stitched together.

UX Unification flips the order of work. **Understand the system → place the feature → reuse → build → validate → update the system.** Each feature leaves the product more consistent, not less.

---

## 👥 Who It's For

| You are… | Use it to… | Start with |
|---|---|---|
| **Product Designer** | Design new features that fit the existing design system, spot screens that drift, and back every design decision with evidence | `/place` → `/pattern`, `/audit` |
| **Product Manager** | Know where a feature belongs and who should see it before work starts, catch duplicate features, and get a ready-made test plan | `/place`, `/debt`, `/explain` |
| **Solo Builder / Founder** | Keep the product consistent without a dedicated designer, going from idea to UI and code in one run | `/unify` |
| **Engineer** | Reuse the right component instead of writing a new one, get small patches instead of copies, and review PRs for UI consistency | `/build`, `/audit` |

No coding needed for designers and PMs: share screenshots instead of code and the skill runs in design-only mode. See **[Getting started](./docs/getting-started.md)** and the **[Walkthrough](./docs/walkthrough.md)** for each command.

---

## 🔄 The Workflow (8 Steps)

### Phase A: Understand the System
**Role**: Design Ops / UX Architect
- **Step 0 · System Map**: builds a living model of the product (structure, roles, journeys, vocabulary, tokens, patterns, product-wide rules) from code or screenshots. It's reused and refreshed on every run.
- **Step 1 · Hypothesis**: records a first guess *before* looking at evidence, so bias becomes visible later.

### Phase B: Place the Feature
**Role**: Product Designer / PM
- **Step 2 · PRD in context**: maps the PRD to existing journeys and finds overlaps, things to retire, naming conflicts and convention clashes.
- **Step 3 · Placement**: decides where the feature lives, how users reach it, and which roles see it. 🛑 *Checkpoint 1: you confirm.*

### Phase C: Design & Build
**Role**: UI Designer / Front-end Engineer
- **Step 4 · Patterns**: climbs the decision ladder **Reuse → Extend → Compose → Create** with a confidence level per decision; uncertain ones become Option A vs. B. 🛑 *Checkpoint 2: you choose.*
- **Step 5 · Components**: generates code from the project's own components and tokens. Changes to shared components are small patches, never copies.

### Phase D: Validate & Feed Back
**Role**: UX Researcher / Design Lead
- **Step 6 · Validation plan**: findability and comprehension tasks per role, with the success bar set *before* testing.
- **Step 7 · Rationale + System update**: every decision explained with evidence, a five-layer consistency check, trade-offs, and unification debt found. Then the System Map is updated.

---

## ⌨️ Slash Commands

Type a command at the start of a message to jump straight to a step. In tools without slash-command support, just type it as text; the skill recognises it.

| Command | What it does |
|---|---|
| `/unify` | Full workflow for a feature (default) |
| `/map` | Build or refresh the System Map |
| `/place` | Hypothesis, PRD analysis and placement |
| `/pattern` | Choose patterns and write the screen spec |
| `/build` | Generate components from an approved spec |
| `/audit` | Check an existing screen, PR or design for inconsistency |
| `/debt` | List and prioritise existing inconsistencies |
| `/handoff` | Export `handoff.json` for another agent or teammate |
| `/explain` | Rewrite the result for a non-technical reader |

---

## 🔍 Built on Evidence, Not Guesses

An assistant that sounds sure about a product it hasn't really looked at does more harm than good. This skill is built so you can always tell what it actually saw, what it worked out, and what it still needs from you.

| Rule | What it means for you |
|---|---|
| **Show the source** | Every statement about your product points to where it came from: a file, a screenshot, a line in your PRD. It's labelled as seen `[GROUNDED]`, worked out `[INFERRED]` or guessed `[SPECULATIVE]`, so you know how much to trust it. |
| **Ask, don't fill in** | When something is missing (a user role, a screen it wasn't shown, a backend rule), the assistant names the gap and asks. It doesn't invent a plausible answer. |
| **You make the calls** | It stops to check with you after deciding where a feature goes, and before building any option it isn't sure about. |
| **Your code stays yours** | Everything it produces lands in a separate `.ux-unify/` folder. Your source files change only if you ask. |
| **Pick up where you left off** | `/handoff` saves decisions, open questions and confidence in `handoff.json` ([format](./skills/ux-unification/handoff_schema.json)), so the next person, tool or session doesn't start from zero. |

---

## 📤 What You Get

```
.ux-unify/
├── system-map/            ← your product's living model (commit it, share it)
│   ├── ia-tree.md  roles.md  journeys.md  glossary.md
│   ├── tokens.md  patterns.md  global-patterns.md
│   └── debt.md            ← inconsistencies already in your product, with fixes
└── features/<feature>/
    ├── rationale.md       ← read first: decisions in plain language + "Needs your review"
    ├── pattern-spec.md    ← the screen: placement, layout, flow, every state, exact wording
    ├── analysis.md        ← journeys, overlaps, naming, conflicts
    ├── hypothesis.md      ← first guess vs. final outcome
    ├── validation-plan.md ← ready-to-run user test
    ├── components/        ← code + small patches for your developer (when code is shared)
    └── handoff.json
```

See a complete real example in **[`examples/sample-app/.ux-unify/`](./examples/sample-app/.ux-unify/)** and a guided tour in **[Reading the results](./docs/reading-the-results.md)**.

---

## 🔑 Dependencies

- **Feature description** 🟢 Required. A PRD, a brief, or a few sentences.
- **Product code** 🟡 Recommended. Without it the skill runs in **design-only mode** from screenshots.
- **Python 3** ⚪ Optional. Runs the inventory scanner; otherwise the agent reads files directly.
- **Figma / MCP / connectors** ⚪ Not required. 100% text-and-code portable.

---

## 🚀 Installation

### Option 1: CLI (any agent, one command)

```bash
# into ./.agents/skills (read by most agents that support skills)
npx github:aarxn-yourbf/ux-unification add

# into a specific agent's folder
npx github:aarxn-yourbf/ux-unification add --agent claude    # ./.claude/skills
npx github:aarxn-yourbf/ux-unification add --agent cursor    # ./.cursor/skills
npx github:aarxn-yourbf/ux-unification add --agent copilot   # ./.github/skills
npx github:aarxn-yourbf/ux-unification add --agent gemini    # ./.gemini/skills

# for all your projects
npx github:aarxn-yourbf/ux-unification add --global          # ~/.agents/skills

# anywhere else
npx github:aarxn-yourbf/ux-unification add --dir path/to/skills
```

Requires Node.js 16.7+. Run it from your project's root folder.

### Option 2: Copy the folder

Copy `skills/ux-unification/` into your tool's skills folder (`.agents/skills/` works for most).

### Option 3: Chat apps (no terminal)

- **Apps with skill upload** (e.g. Claude): upload [`dist/ux-unification.zip`](./dist/ux-unification.zip) in the app's skills settings.
- **Any other assistant** (ChatGPT, Gemini, a custom GPT or Gem, a chat "project"): add `SKILL.md` as custom instructions, or upload it with the `references/` files as knowledge and tell the assistant *"Follow SKILL.md"*.

Step-by-step for each tool: **[Getting started](./docs/getting-started.md)**.

---

## 💬 Usage

```
/unify docs/prd-bulk-assign.md
```
```
Use the ux-unification skill. Here's the PRD (attached) and our app's code.
Design it so it feels like the rest of the product.
```
```
/audit screenshots attached: this is our new Billing page. What doesn't match the rest of the app?
```
```
/place We want "saved filters" on the dashboard. No code, screenshots attached.
```

No PRD? Use the **[feature brief template](./docs/prd-template.md)**, or just describe *who* it's for, *what* they need to do and *why*.

---

## 📚 Documentation

| Guide | For |
|---|---|
| [Getting started](./docs/getting-started.md) | Installing in any tool, sharing your product, first run. No code required |
| [Walkthrough](./docs/walkthrough.md) | Each command: what it does, when to use it, pro tips |
| [Reading the results](./docs/reading-the-results.md) | What each output file means and what to do with it |
| [How it works](./docs/how-it-works.md) | The method, the five layers of consistency, and where the ideas come from |
| [Feature brief template](./docs/prd-template.md) | Fill-in-the-blanks PRD |
| [FAQ & glossary](./docs/faq.md) | Troubleshooting and plain-language definitions |

---

## 📂 Repository Layout

```
ux-unification/
├── skills/ux-unification/        ← the skill (SKILL.md, README, references, scanner, handoff schema)
├── bin/cli.js                    ← npx installer
├── dist/ux-unification.zip       ← upload package for chat apps
├── docs/                         ← guides
├── examples/                     ← sample app, sample PRD, full output
├── tools/build_dist.py           ← rebuilds dist/ after edits
└── package.json
```

---

## ⚠️ Limitations

- **The AI proposes; people decide.** Review the "Needs your review" items and the code before shipping.
- **Not a substitute for user testing.** It writes the test plan; you run it.
- **Strongest code output for React, Next.js and Vue.** Other stacks get the full analysis and annotated pseudo-code.
- **Roles and journeys are often `[INFERRED]`.** Code rarely says who uses what. Persona notes or analytics improve the result.
- **Very large codebases** may not fit in a chat window. Share the app shell, shared components, styles and the area being changed, or use a coding agent that reads files from disk.

---

## 📄 License

MIT License.
