#!/usr/bin/env node
// Installer for the ux-unification agent skill.
// Usage: npx github:aarxn-yourbf/ux-unification add [--agent <name>] [--global] [--dir <path>]

const fs = require("fs");
const os = require("os");
const path = require("path");

const SKILL = "ux-unification";
const REPO = "github:aarxn-yourbf/ux-unification";
const SOURCE = path.join(__dirname, "..", "skills", SKILL);

// Folder each agent reads skills from (relative to the project, or to the home folder with --global).
// `.agents/skills` is the shared location read by most agents that support SKILL.md.
const AGENTS = {
  agents: ".agents/skills",
  claude: ".claude/skills",
  cursor: ".cursor/skills",
  copilot: ".github/skills",
  gemini: ".gemini/skills",
};

function help(code = 0) {
  console.log(`
UX Unification: install the agent skill

  npx ${REPO} add                    install to ./.agents/skills (works with most agents)
  npx ${REPO} add --agent claude     install to ./.claude/skills
  npx ${REPO} add --global           install to ~/.agents/skills (all projects)
  npx ${REPO} add --dir <path>       install to any folder
  npx ${REPO} where                  show the folder each --agent option uses

Agents: ${Object.keys(AGENTS).join(", ")}
No skills support in your tool? Use SKILL.md as custom instructions. See README.
`);
  process.exit(code);
}

function arg(name) {
  const i = process.argv.indexOf(name);
  return i > -1 ? process.argv[i + 1] : undefined;
}

const command = process.argv[2];
if (!command || command === "help" || command === "--help" || command === "-h") help(0);

if (command === "where") {
  for (const [k, v] of Object.entries(AGENTS)) {
    const g = ["agents", "claude"].includes(k) ? `   (with --global: ~/${v})` : "";
    console.log(`  --agent ${k.padEnd(8)} ./${v}${g}`);
  }
  process.exit(0);
}

if (command !== "add") {
  console.error(`\n❌ Unknown command '${command}'.`);
  help(1);
}

const agent = arg("--agent") || "agents";
if (!AGENTS[agent]) {
  console.error(`\n❌ Unknown agent '${agent}'. Choose one of: ${Object.keys(AGENTS).join(", ")}, or use --dir <path>.\n`);
  process.exit(1);
}
const GLOBAL_OK = ["agents", "claude"]; // verified personal folders: ~/.agents/skills, ~/.claude/skills
if (process.argv.includes("--global") && !arg("--dir") && !GLOBAL_OK.includes(agent)) {
  console.error(`\n❌ --global isn't set up for '${agent}'. Use --global alone (~/.agents/skills), or --dir with your tool's personal skills folder.\n`);
  process.exit(1);
}
const base = arg("--dir")
  ? path.resolve(arg("--dir"))
  : path.join(process.argv.includes("--global") ? os.homedir() : process.cwd(), AGENTS[agent]);
const target = path.join(base, SKILL);

if (!fs.existsSync(SOURCE)) {
  console.error(`\n❌ Skill files not found at ${SOURCE}.\n`);
  process.exit(1);
}

const existed = fs.existsSync(target);
fs.mkdirSync(base, { recursive: true });
fs.cpSync(SOURCE, target, {
  recursive: true,
  force: true,
  filter: (src) => !src.includes("__pycache__") && !src.endsWith(".pyc") && !src.endsWith(".DS_Store"),
});

console.log(`\n📦 ${existed ? "Updated" : "Installed"} '${SKILL}' → ${target}`);
console.log(`✅ Done. Ask your assistant: "/unify <your PRD>" or "Use the ux-unification skill on this feature."\n`);
