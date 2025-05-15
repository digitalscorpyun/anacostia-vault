---
id: '20250511112837'
title: Reading Summary Template
category: ''
style: ScorpyunStyle
path: ''
created: '2025-05-11'
updated: '2025-05-11'
status: in_progress
priority: normal
summary: ''
longform_summary: ''
tags: []
cssclasses:
- tyrian-purple
- sacred-tech
synapses: []
key_themes: []
bias_analysis: ''
grok_ctx_reflection: ''
quotes: []
adinkra: []
linked_notes: []
---

<%*
// ──────────────────────────────────────────────
// SCORPYUNSTYLE™ SNAKE_CASE SUMMARY TEMPLATE
// For use during active study and reading
// Obsidian Templater version – snake_case everything
// ──────────────────────────────────────────────

// Prompt user input
const userTitle = await tp.system.prompt("📘 Title of Work") || "untitled";
const userFolder = await tp.system.prompt("📂 Folder (e.g., reading_notes)") || "reading_notes";
const userCategory = await tp.system.prompt("🗂️ Category (e.g., afrikan_studies)") || "uncategorized";
const userTags = await tp.system.prompt("🏷️ Additional Tags (comma-separated)") || "";
const userSummary = await tp.system.prompt("📄 Detailed Summary:");
const bullet1 = await tp.system.prompt("🧠 Synapse 1:");
const bullet2 = await tp.system.prompt("🧠 Synapse 2:");
const bullet3 = await tp.system.prompt("🧠 Synapse 3:");
const bullet4 = await tp.system.prompt("🧠 Synapse 4:");
const summaryStyle = await tp.system.suggester(["ScorpyunStyle", "UBW", "GriotBox"], ["ScorpyunStyle"]);

// Convert title to snake_case for filename
function toSnakeCase(str) {
  return str
    .normalize("NFD").replace(/[\u0300-\u036f]/g, '')       // remove accents
    .replace(/[^a-zA-Z0-9]+/g, '_')                         // non-alphanum to _
    .replace(/^_+|_+$/g, '')                                // trim leading/trailing _
    .replace(/__+/g, '_')                                   // collapse multiple _
    .toLowerCase();
}

const snakeTitle = toSnakeCase(userTitle);
const newFileName = `summary_of_${snakeTitle}.md`;

await tp.file.rename(newFileName);
await tp.file.move(`${userFolder}/${newFileName}`);

// Generate timestamps
const now = tp.date.now("YYYY-MM-DD HH:mm:ss");
const idString = `'${tp.date.now("YYYYMMDDHHmmss")}'`;

// Build YAML frontmatter
let out = `---\n`;
out += `id: ${idString}\n`;
out += `title: "summary_of_${snakeTitle}"\n`;
out += `category: "${userCategory}"\n`;
out += `style: "${summaryStyle}"\n`;
out += `path: "${userFolder}"\n`;
out += `created: "${now}"\n`;
out += `updated: "${now}"\n`;
out += `tags: [summary, ${userTags.split(',').map(tag => tag.trim().replace(/[^a-z0-9_]/gi, '_').toLowerCase()).join(', ')}]\n`;
out += `summary: "${userSummary.replace(/"/g, '\\"')}"\n`;
out += `synapses:\n`;
out += `  - "${bullet1 || ""}"\n`;
out += `  - "${bullet2 || ""}"\n`;
out += `  - "${bullet3 || ""}"\n`;
out += `  - "${bullet4 || ""}"\n`;
out += `adinkra:\n`;
out += `  - "🦢 sankofa"\n`;
out += `linked_notes:\n`;
out += `  - [[sankofa_reading_journey]]\n`;
out += `---\n\n`;

// Body content
out += `# summary_of_${snakeTitle}\n\n`;
out += `## 📌 Overview\n${userSummary || "Write your detailed summary here..."}\n\n`;
out += `---\n\n`;
out += `## 🔑 Key Themes\n- **Theme 1:** (Fill in)\n- **Theme 2:** (Fill in)\n- **Theme 3:** (Fill in)\n\n`;
out += `---\n\n`;
out += `## ⚖️ Bias Analysis\n(Identify any ideological, structural, or narrative biases.)\n\n`;
out += `---\n\n`;
out += `## 🤖 Generative AI Reflections\n(How might this text affect AI ethics, design, or decolonial tooling?)\n\n`;
out += `---\n\n`;
out += `## 🔗 Vault Connections\n- [[digitalscorpyun_manifesto_and_syllabus]]\n- [[sankofa_spine]]\n\n`;
out += `---\n\n`;
out += `## 🏷️ Tags\n#summary #${summaryStyle.toLowerCase()} #${userCategory.replace(/\s+/g, '_').toLowerCase()}\n`;

tR += out;
-%>
