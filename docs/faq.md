# FAQ & troubleshooting

## General

**Which AI tools does this work with?**
Any. Tools that support `SKILL.md` skills (Claude, Codex, Cursor, GitHub Copilot, Gemini CLI, Junie and others) load it automatically. Any other assistant (ChatGPT, Gemini, an internal bot) can follow `SKILL.md` as custom instructions. See [Getting started](getting-started.md).

**Do I need to know how to code?**
No. Share screenshots and a feature description and you'll get placement, pattern choices, a detailed screen spec, exact wording, a test plan and the reasoning. Sharing code adds developer-ready code and more precise evidence.

**Will it change my product's code?**
No. Everything goes into a separate `.ux-unify/` folder (or is returned as documents in a chat). Your real code only changes if you explicitly ask, and a developer should review it.

**Will I get mockups?**
You get a precise written spec and, with code, working components. For visuals, ask your assistant to *"turn pattern-spec.md into a mockup"*, or give the spec to a UI-generation or design tool. Because the spec is built from your existing patterns, the result will match your product.

**Does it replace a designer or UX researcher?**
No. It does the systematic groundwork (inventory, consistency checks, options, a test plan) so people can spend their time on judgment: the "Needs your review" decisions and real user testing.

**What languages does it write in?**
Reports follow the language of your PRD unless you ask otherwise. Code follows your project's conventions.

**Which tech stacks are supported?**
Any, for the analysis. Code generation is strongest for React, Next.js and Vue (TypeScript or JavaScript). For other stacks the assistant produces annotated pseudo-code and says so.

## Using it

**The assistant didn't use the skill.**
Start your message with `/unify`, or say *"Use the ux-unification skill"*. In coding agents, check the skill folder is where your tool looks (reinstall with `--agent` or `--dir`) and restart the tool. In chat apps, check the skill is switched on, or that `SKILL.md` is in the instructions or knowledge.

**My tool doesn't support slash commands.**
Type them as plain text at the start of your message. The skill recognises them either way.

**My codebase is too big for the chat.**
Share only the app layout/navigation, the shared components folder, the styles/theme folder and the screens near the new feature. Or use a coding agent that reads files from disk.

**My chat assistant can't access my private repository.**
Use your assistant's GitHub/GitLab integration if it has one (you may need to grant access to that repository), or ask a developer for a zip of the front-end code.

**It can't run the scanner script.**
That's fine. The scanner only speeds up Step 0; the assistant reads the files directly instead.

**How do I make the second feature faster?**
Keep the System Map. In a project folder it stays in `.ux-unify/system-map/`. In chat apps, attach the saved `system-map` files next time or add them to your chat project's knowledge. Or start with the previous `handoff.json`.

**The result is too technical, or not technical enough.**
`/explain` for a plain-language version, or *"Give me the developer details."*

**I disagree with a decision.**
Say why, e.g. *"Managers do need to see the restore button. Show it disabled with an explanation."* The assistant updates the spec, the code and the System Map's conventions so future features follow your decision.

**It stated something that isn't true about our product.**
Ask *"Is that [GROUNDED]? Where did you see it?"* The rules require every claim to be tagged and cited; an untagged or wrongly tagged claim should be corrected or removed.

**Can a team share one System Map?**
Yes, that's the point. Commit `.ux-unify/system-map/` to your repository, or keep it in a shared chat project.

## Glossary

| Term | Meaning |
|---|---|
| **Agent skill** | A folder of instructions (`SKILL.md` plus reference files) that teaches an AI assistant how to do a specific job well. |
| **PRD** | Product Requirements Document: what a feature should do and why. A few paragraphs is fine. |
| **UX unification** | Making separate parts of a product feel like one product: same look, words, structure, behaviour and logic. |
| **System Map** | The skill's living model of your product, reused for every feature. |
| **IA (information architecture)** | How a product is organised: sections, pages, tabs, menus. |
| **Pattern** | A reusable way of solving a UI problem, e.g. a data table, a confirmation dialog, tabs. |
| **Component** | A reusable piece of UI in code that implements a pattern, e.g. `DataTable`. |
| **Design token** | A named design value (color, spacing, font size) used everywhere instead of raw values. |
| **Microcopy** | The small text in an interface: button labels, error messages, empty-state text. |
| **States** | The conditions a screen can be in: empty, loading, error, success, no permission. |
| **Role** | A type of user with certain permissions, e.g. analyst, admin. |
| **Journey** | The sequence of steps a user takes to get something done. |
| **Unification debt** | Existing inconsistencies in the product, like two different dialogs for the same job. |
| **Reuse / Extend / Compose / Create** | The decision ladder: use as-is / add a small option / combine existing pieces / build new. |
| **`[GROUNDED]` / `[INFERRED]` / `[SPECULATIVE]`** | Confidence tags: seen and cited / deduced / guessed. |
| **Checkpoint** | A pause where the assistant asks you to confirm before continuing. |
| **Handoff** | `handoff.json`: a structured summary for the next agent, session or person. |
| **Patch / diff** | A file describing a small change to existing code, for a developer to review and apply. |
