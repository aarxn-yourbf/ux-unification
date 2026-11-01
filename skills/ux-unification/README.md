# UX Unification

**ID:** `ux-unification`
**Category:** Product Design · Design Systems · UX Strategy
**Works in:** any AI assistant or coding agent that can read a `SKILL.md` (or accept it as instructions)

## Overview

UX Unification is the **coherence keeper** of the design workflow. Give it a feature (a PRD, brief or a few sentences) and your current product (code, or just screenshots). It works out how the product already works, where the feature belongs, what can be reused, and how to build it so it feels native, then explains every decision with evidence.

It also keeps a **System Map**, a living model of your product's structure, roles, journeys, vocabulary, tokens and patterns. Every run updates the map, so each feature makes the next one easier and more consistent.

## 🛠️ Modes

### Full mode (code available)
- **Purpose:** decisions grounded in the real codebase, plus code for developers.
- **Key behavior:** runs the inventory scanner, cites files as evidence, writes components from the project's own building blocks, and expresses changes to shared components as small patches.

### Design-only mode (screenshots or description)
- **Purpose:** the same decisions for people without code access.
- **Key behavior:** builds the System Map from what is visible, tags it `[INFERRED]`, and describes components instead of writing them.

## ⌨️ Commands

| Command | Use it to… |
|---|---|
| `/unify` | Run the full workflow for a feature |
| `/map` | Build or refresh the System Map |
| `/place` | Decide where a feature lives and who sees it |
| `/pattern` | Choose patterns and write the screen spec |
| `/build` | Generate components from an approved spec |
| `/audit` | Check an existing screen, PR or design for inconsistency |
| `/debt` | List and prioritise existing inconsistencies |
| `/handoff` | Export `handoff.json` for another agent or teammate |
| `/explain` | Rewrite the result for a non-technical reader |

## ⚡ When to trigger

- You have a PRD and want UI that **fits the existing product**.
- You're unsure **which component or pattern** to use, or **where** a feature should go.
- A feature **looks bolted on** and you want to know why.
- You're merging products or areas and need to find **where they diverge**.
- Before a design review or PR, to **audit consistency**.

## 🔄 How it fits a design workflow

1. **Frame:** define the problem and write the PRD (any tool or skill).
2. **Unify:** `/place` and `/pattern` to decide placement and patterns against the System Map.
3. **Build:** `/build`, or hand `pattern-spec.md` to a designer or a UI-generation tool.
4. **Validate:** run `validation-plan.md` with users; `/audit` the result.
5. **Hand off:** `/handoff` to pass decisions and open questions downstream.

## 🔑 Dependencies

| Need | Required? |
|---|---|
| Feature description | 🟢 Yes. A few sentences is enough |
| Product code | 🟡 Recommended. Without it, design-only mode |
| Ability to run Python 3 | ⚪ Optional. Speeds up Step 0; otherwise the agent reads files |
| Figma, MCP or any connector | ⚪ Not required |

## 📂 Files

```
ux-unification/
├── SKILL.md               instructions the agent follows
├── README.md              this file
├── handoff_schema.json    shape of handoff.json
├── references/            guides loaded at each step + output templates
└── scripts/scan_inventory.py
```
