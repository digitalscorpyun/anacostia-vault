<%*
// ----------------------------------------------------------------
// Templater Summary Template: Distinguish Summary from Synapses
// ----------------------------------------------------------------

// Prompt user for Title
let userTitle = await tp.system.prompt("Enter Title:");
if (!userTitle) { userTitle = "untitled"; }

// Prompt user for the folder path
let userFolder = await tp.system.prompt("Enter Folder Path (existing folder):");
if (!userFolder) userFolder = "."

// Prompt user for Category, Additional Tags, etc.
let userCategory = await tp.system.prompt("Enter Category:");
let userTags = await tp.system.prompt("Enter Additional Tags (comma-separated):");

// Prompt for a more detailed, paragraph style summary
let userLongSummary = await tp.system.prompt("Enter your detailed summary:");

// Prompt for bullet-point synapses
let bullet1 = await tp.system.prompt("Synapse 1 (short bullet)");
let bullet2 = await tp.system.prompt("Synapse 2 (short bullet)");
let bullet3 = await tp.system.prompt("Synapse 3 (short bullet)");
let bullet4 = await tp.system.prompt("Synapse 4 (short bullet)");

// Convert title to kebab-case for renaming
function toKebabCase(str) {
  return str.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
}
let kebabTitle = toKebabCase(userTitle);

// Rename the file to "summary-of-<kebabTitle>.md"
let newFileName = "summary-of-" + kebabTitle + ".md";
await tp.file.rename(newFileName);

// Move it to the specified folder
await tp.file.move(userFolder + "/" + newFileName);

// Prepare Timestamps and an ID
let now = tp.date.now("YYYY-MM-DD HH:mm:ss");
let idString = "'" + tp.date.now("YYYYMMDDHHmmss") + "'"; // store ID as text

// Build the YAML front matter
let out = "";
out += "---\n";
out += "id: " + idString + "\n";
out += "title: \"summary-of-" + kebabTitle + "\"\n";
out += "category: \"" + userCategory + "\"\n";
out += "path: \"📂 " + userFolder + "\"\n";
out += "created: \"📅 " + now + "\"\n";
out += "updated: \"🕒 " + now + "\"\n";
out += "tags: [summary_if_user_tags_out, user_tags_out, generative_ai, africana_studies]\n";
// Store the long-form summary in a "summary" field
out += "summary: \"" + userLongSummary + "\"\n";
// Each bullet goes into the synapses array
out += "synapses:\n";
out += "  - \"" + (bullet1 || "") + "\"\n";
out += "  - \"" + (bullet2 || "") + "\"\n";
out += "  - \"" + (bullet3 || "") + "\"\n";
out += "  - \"" + (bullet4 || "") + "\"\n";
out += "adinkra:\n";
out += "  - \"🦢 sankofa\"\n";
out += "---\n\n";

// Now let's create the body content
out += "# summary-of-" + kebabTitle + "\n\n";
out += "## 📌 Overview\n" + (userLongSummary || "Write your detailed summary here...") + "\n\n";
out += "---\n\n";
out += "## 🔑 Key Themes\n";
out += "- **Theme 1:** (Fill in details)\n";
out += "- **Theme 2:** (Fill in details)\n";
out += "- **Theme 3:** (Fill in details)\n\n";
out += "---\n\n";
out += "## ⚖️ Bias Analysis\n(Identify biases present in the text or discussed by the author.)\n\n";
out += "---\n\n";
out += "## 🤖 Implications for Generative AI\n(Reflect on how the text's insights can influence AI ethics, fairness, and decolonial computational practices.)\n\n";
out += "---\n\n";
out += "## 🔗 Connections to the Anacostia Vault\n";
out += "- [[the-lion-of-anacostia-bias-detection]]\n";
out += "- [[africana-studies-overview]]\n";
out += "- [[ai-ml-central-hub]]\n\n";
out += "---\n\n";
out += "## 🏷️ Tags\n#d_at_a_s_ov_er_ei_gn_tys_um_ma_ry #d_at_a_s_ov_er_ei_gn_tyg_en_er_at_iv_e_a_i #d_at_a_s_ov_er_ei_gn_tya_fr_ic_an_a_s_tu_di_es\n";

tR += out;
-%>



