# Getting started

This guide is for everyone: product managers, designers, founders and engineers. Pick the path that matches the AI tool you use. No coding is needed for the chat paths.

**You'll need**
- An AI assistant (see the options below).
- The feature you want to build, written down: a PRD, a brief or even a paragraph.
- Your current product: ideally its code, otherwise screenshots.

---

## Step 1: Install the skill in your tool

### A. Coding agents and AI code editors
*Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, Junie and other tools that support `SKILL.md` skills.*

Open a terminal in your project's main folder and run:

```bash
npx github:aarxn-yourbf/ux-unification add
```

This puts the skill in `.agents/skills/ux-unification/`, the shared folder most of these tools read. If your tool uses its own folder, add `--agent`:

| Tool | Command |
|---|---|
| Most tools (shared folder) | `npx github:aarxn-yourbf/ux-unification add` |
| Claude Code | `… add --agent claude` |
| Cursor | `… add --agent cursor` |
| GitHub Copilot | `… add --agent copilot` |
| Gemini CLI | `… add --agent gemini` |
| All your projects | `… add --global` |
| A custom folder | `… add --dir path/to/skills` |

No Node.js? Download the repository (green **Code** button → **Download ZIP**), unzip it, and copy the `skills/ux-unification` folder into `.agents/skills/` in your project.

> Check your tool's documentation for where it looks for skills. Folder names can change between versions. `--dir` lets you install anywhere.

### B. Chat apps that support skill uploads
*For example the Claude app.*

1. Download [`dist/ux-unification.zip`](../dist/ux-unification.zip) from the repository and **don't unzip it**.
2. Open your app's skills settings and choose **upload a skill**. In Claude it's **Customize → Skills → + → Create skill → Upload a skill**, and **code execution** must be on in **Settings → Capabilities**.
3. Make sure the skill is switched **on**.

### C. Any other AI chat
*ChatGPT, Gemini, Copilot chat, a custom GPT or Gem, a chat "project", an internal assistant…*

The skill is plain text, so any assistant can follow it:

1. Download the repository (**Code → Download ZIP**) and unzip it.
2. Open `skills/ux-unification/`. You need **`SKILL.md`** and the **`references`** folder.
3. Then either:
   - **Best:** create a project, custom GPT or Gem. Upload `SKILL.md` and the files in `references/` as **knowledge/files**, and in its **instructions** write:
     > Follow SKILL.md for every request. Read the reference files it mentions when you reach that step.
   - **Quick:** at the start of a chat, attach `SKILL.md` and write *"Follow these instructions for this conversation."*

Plain chat assistants usually can't run the scanner script. That's fine: they read your files directly.

---

## Step 2: Share your product

Give the assistant your current product in whichever way is easiest. More is better, but anything works.

### Best: the code
- **Coding agents:** nothing to do. Run the assistant inside your project folder.
- **Chat apps:** attach the code. Use a GitHub integration if your app has one, or ask a developer for a **zip of the front-end** (without `node_modules`) and attach it.

> **Large product? Share just the important parts:** the app layout/navigation, the shared components folder (often `components`, `ui` or `design-system`), the theme or styles folder, and the screens near your new feature.

### Good: screenshots
No code access? Take screenshots of the main navigation, 3–6 important screens (especially those next to where the feature might go), and any table, form and pop-up dialog. The skill switches to **design-only mode**: same decisions and explanations, no code.

### Optional extras
Who your users are (roles such as "analyst" or "admin"), your design system or brand guide, user complaints, analytics.

---

## Step 3: Ask

Attach or paste your feature description and send:

```
/unify Here's the PRD for [feature]. Make it fit our current product.
```

or in plain words:

```
Use the ux-unification skill. Here's the PRD for [feature] and our product. Design it so it feels like the rest of the app.
```

| You want… | Say… |
|---|---|
| Only where it should go | `/place` + your PRD |
| Which components to use | `/pattern` + your PRD |
| To check an existing screen | `/audit` + screenshot or file |
| A list of existing inconsistencies | `/debt` |
| Something for stakeholders | `/explain` |
| Reports in another language | "Write the reports in Vietnamese." (default: your PRD's language) |

**No PRD?** Describe *who* it's for, *what* they need to do and *why*, or fill in the [feature brief template](prd-template.md). The assistant will turn it into a mini-PRD and check it with you.

---

## Step 4: Answer the two checkpoints

The assistant pauses twice:
1. **Placement:** "I'd put this as a tab on the Rule page, visible to data scientists and managers. OK?"
2. **Uncertain decisions:** "Option A or B for selecting versions? I recommend A because…"

Answer briefly, or say *"use your recommendations"*.

---

## Step 5: Read the results

Start with **`rationale.md`**: plain-language decisions and a **Needs your review** list. Then **`pattern-spec.md`** for the screen in detail. Hand the `components/` folder (and the whole `.ux-unify/` folder) to your developer.

Guided tour: [Reading the results](reading-the-results.md).

---

## Step 6: Next time is faster

Keep the **System Map**. It's reused for every feature.
- **In a project folder:** `.ux-unify/system-map/` stays there. Commit it so your team shares it.
- **In chat apps:** save the files the assistant produced. Next time, attach the `system-map` files (or add them to your project's knowledge) and say *"Here's our existing System Map."*
- **Between tools or people:** `/handoff` produces a `handoff.json` you can give to the next session.

---

## If something doesn't work

| Problem | Fix |
|---|---|
| The assistant ignores the skill | Start your message with `/unify`, or say *"Use the ux-unification skill"*. In chat apps, check the skill is on, or that SKILL.md is in the instructions. |
| `npx` not found | Install Node.js (LTS) from nodejs.org, or copy the folder manually (Step 1A). |
| The skill isn't picked up after install | Check the folder your tool reads skills from and reinstall with `--agent` or `--dir`. Restart the tool. |
| "Too large" / only part of the code was read | Share fewer folders (see the tip in Step 2), or use a coding agent that reads files from disk. |
| Output is too technical | `/explain`, or *"Rewrite this for a non-technical reader."* |
| It invented something | Ask for the tag and source: *"Is that [GROUNDED]? Where did you see it?"* The rules require it to correct itself. |

More in the [FAQ](faq.md).
