<%* 
// Define variables using await tp.system.prompt() to get user input
const projectName = await tp.system.prompt("Project Name:", "AI and Machine Learning");
const topic = await tp.system.prompt("Topic:", "Neural Networks");
const category = await tp.system.prompt("Category:", "AI/ML");
const quote = await tp.system.prompt("Quote:", "The development of full artificial intelligence could spell the end of the human race.");
const quoteAttribution = await tp.system.prompt("Quote Attribution:", "Stephen Hawking");
const relatedProject = await tp.system.prompt("Related Project:", "the-lion-of-anacostia-bias-detection");

// Convert variables to kebab-case for consistency
const formattedCategory = category.replace(/\//g, "-").toLowerCase();
const formattedTopic = topic.replace(/\s+/g, "-").toLowerCase();
const fileName = `${formattedCategory}-${formattedTopic}`;
const filePath = `ai-ml/${fileName}.md`;

// Ensure file renaming happens only when a file exists
if (tp.file.title === "Untitled" && tp.file.path) {
    try {
        await tp.file.rename(fileName);
        await new Promise(resolve => setTimeout(resolve, 1000)); // Delay for rename to register
        console.log(`✅ Successfully renamed file to ${fileName}`);
    } catch (error) {
        console.error(`⚠️ Error renaming file: ${error.message}`);
    }
} else {
    console.log(`📄 File already named: ${tp.file.title}`);
}

// Assign values to be used inside the note
tR += `# ${formattedCategory.toUpperCase()} - ${topic}\n\n`;
tR += `> _"${quote}"_\n> — ${quoteAttribution}\n\n`;
tR += "## 📌 Overview\n\n";
tR += `**${topic}** is a core **${category}** concept, pivotal in advancing artificial intelligence and machine learning applications. It connects to projects like *The Lion of Anacostia* for bias detection in AI models.\n\n`;

tR += "## 📂 Categories\n\n";
tR += `- **Core Concept:** [[${fileName}]]\n`;
tR += `- **Foundational Topics:** [[${formattedCategory}-${formattedTopic}]]\n`;
tR += `- **Applications:** [[${formattedCategory}-bias-detection]]\n`;
tR += `- **Theoretical Context:** [[${formattedCategory}-overview]]\n`;
tR += "- **Interdisciplinary Links:** [[africana-studies-overview]]\n\n";

tR += "## 🧠 Technical Context\n\n";
tR += "- [ ] Explore how **" + topic + "** functions in deep learning architectures.\n";
tR += "- [ ] Identify key algorithms or frameworks (e.g., TensorFlow, PyTorch).\n";
tR += "- [ ] Connect its applications to real-world AI challenges, such as bias mitigation.\n\n";

tR += "## 🌍 Impact & Applications\n\n";
tR += "- [ ] How has **" + topic + "** shaped AI, data science, and technology?\n";
tR += "- [ ] What lessons does it offer for bias modeling in Africana Studies?\n";
tR += "- [ ] Who continues to innovate with this technology?\n\n";

tR += "## 📖 Reference Notes\n\n";
tR += "- [[book-summaries]] – Essential readings (e.g., *Deep Learning* by Goodfellow).\n";
tR += "- [[online-articles]] – Key digital sources on AI/ML.\n";
tR += "- [[research-papers]] – Scholarly insights on neural networks.\n\n";

tR += "## 🔗 Connections in My Zettelkasten\n\n";
tR += "- [[00-index]] – **Main Knowledge Hub**\n";
tR += `- [[${formattedCategory}-overview]] – **Category Overview**\n`;
tR += `- [[${relatedProject}]] – **Related Project**\n\n`;

tR += "## 📖 References\n\n";
tR += "- [ ] **Core Texts & Research** (e.g., *Deep Learning*, AI ethics studies).\n\n";

tR += "## 🏷️ Tags\n\n";
tR += `#AI #ML #${formattedTopic} #Technology #Learning\n\n`;
tR += `📂 **File Path:** ${filePath}\n`;
%>
