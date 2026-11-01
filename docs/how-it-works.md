# How it works

> Looking for the commands? See the [Walkthrough](walkthrough.md).

The skill follows eight steps. The order matters: **understand the system → place the feature → choose patterns → build → validate → feed back**. Picking a component before knowing where a feature lives and who sees it is how "bolted-on" features happen.

```
 0. System Map ─► 1. Hypothesis ─► 2. PRD in context ─► 3. Placement
                                                              │
 7. Rationale + update map ◄─ 6. Validation plan ◄─ 5. Components ◄─ 4. Patterns
        │
        └──────────── feeds the System Map for the next feature ────────────┘
```

---

## Step 0: Build or load the System Map

The assistant builds a picture of the product as it is today: structure (sections, pages, tabs), user roles and what each can see, main user journeys, vocabulary, visual tokens (colors, spacing, type), reusable patterns, and product-wide rules. If code is available, a scanner script collects facts quickly; the assistant then reads the important files itself.

If a System Map already exists from a previous feature, the assistant reuses it and refreshes only what changed.

*Why:* you can't make something consistent with a product you haven't looked at.

## Step 1: Write a hypothesis

Before analysing in depth, the assistant writes down its first guess: where the feature goes, which pattern it'll use, which existing feature it resembles.

*Why:* borrowed from card-sorting research, where designers sort the cards themselves before watching users. Writing the guess first makes bias visible later.

## Step 2: Read the PRD in context

The assistant extracts goals, users, tasks, data and required states, then checks them against the System Map:
- Which existing **journey** does this extend?
- Does it **overlap** with, or make obsolete, something that exists? (Unification projects often find a meaningful share of features can be retired or merged.)
- Does the PRD use a **new name** for an existing concept, or internal jargon users wouldn't use?
- Where does it **conflict** with an established convention?

## Step 3: Placement

Before choosing any component: which area, which level (top-level menu, page, tab, panel, action), entry points, and which roles see it.

*Why:* placement follows how users work, not how the team or the code is organised. A feature used weekly by one role shouldn't get a top-level menu item for everyone.

## Step 4: Choose patterns (the decision ladder)

For each UI need, the assistant climbs a ladder and stops at the first rung that works:

| Rung | Meaning | Burden of proof |
|---|---|---|
| **Reuse** | An existing pattern does exactly this | Show where it's used |
| **Extend** | Close match; add a small option to the original | Show existing usages aren't affected |
| **Compose** | Combine existing pieces | Show the pieces |
| **Create** | Nothing fits | Written reason why the three above fail |

Each decision gets a **confidence** level. High-confidence decisions are made. Medium/low ones become **Option A vs. Option B** with pros, cons and a recommendation, flagged for your review.

*Why:* in navigation A/B tests on complex products, the option that keeps users oriented often beats the one that saves a click. Showing both options lets a human make that call.

## Step 5: Generate components

Using your product's own components, colors, naming and file structure. No new libraries, no invented colors. Changes to existing components are written as small patches, not copies. Copies are how two almost-identical tables appear. Without code, this step produces a detailed description instead.

## Step 6: Validation plan

Findability and comprehension tasks per user role, satisfaction questions on a 1–7 scale, and a success threshold set **before** testing. For complex products with no onboarding, ~60% task success is a reasonable baseline; one case study reached 76%.

*Why:* evidence is what earns support for consistency work.

## Step 7: Rationale and System Map update

The assistant explains every decision with evidence, compares it to the hypothesis, checks the five layers of consistency, lists trade-offs and proposes what to remove or fix. Then it **updates the System Map**: the new feature, terms, patterns and any inconsistencies found.

---

## The five layers of consistency

A feature only feels native when it's consistent on all five:

| Layer | Question |
|---|---|
| **Visual** | Does it look like the rest? (colors, spacing, components, icons) |
| **Language** | Does it use the same words and tone? |
| **Structure** | Is it where users would look for it? |
| **Behaviour** | Do the same actions work the same way? (save, delete, confirm, empty states) |
| **Functional** | Does it work within the same login, permissions and context switching? |

Visual consistency is the easiest and most noticed. Functional consistency is the hardest and often what daily users value most.

---

## Where the ideas come from

The method draws on publicly shared experience from teams that have unified product portfolios, in fields such as fintech, healthcare, security software and digital agencies:

- **Research-led unification.** Mapping products to use cases and journeys first; open and closed card sorting; recording assumptions before research; multi-level information architecture; agreement thresholds for decisions; goal-based naming; role-based visibility; usability tests with a pre-set bar; A/B-tested navigation; a product vision workshop.
- **Phased delivery.** Business case first; a pragmatic design system on existing tech; phased, shippable steps; deliberate trade-offs with planned compensation; terminology as UX; owning maintenance from the start.
- **Systems thinking.** Unification as an organisational problem: different tech, terms, patterns, roadmaps and teams, all moving at once.
- **Familiar but distinct.** Familiar patterns lower cognitive load, but a product still needs its own identity: consistent inside, distinct outside.
- **Product + UX strategy together.** Joining viability (product strategy) and desirability (UX strategy).
- **One pipeline.** A connected flow from research to design to build, starting from a shared design system.
