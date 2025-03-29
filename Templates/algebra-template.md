<%*
// Define variables first using await tp.system.prompt() to ensure they’re initialized before use
const projectName = await tp.system.prompt("Project Name:", "Math for AI Bias Detection");
const topic = await tp.system.prompt("Topic:", "Linear Equations");
const category = await tp.system.prompt("Category:", "Algebra");
const quote = await tp.system.prompt("Quote:", "Mathematics is the language of the universe");
const quoteAttribution = await tp.system.prompt("Quote Attribution:", "Galileo Galilei");
const relatedProject = await tp.system.prompt("Related Project:", "the-lion-of-anacostia-bias-detection");

// Convert to kebab-case for consistency (required for filename and tags/links)
const formattedTopic = topic.replace(/\s+/g, "-").toLowerCase();
const fileName = `algebra-${formattedTopic}`;
const filePath = `mathematics/algebra/${fileName}.md`;

// Rename the note if it's currently untitled, with error handling
if (tp.file.title === "Untitled") {
    try {
        await tp.file.rename(fileName);
        await new Promise(resolve => setTimeout(resolve, 1000)); // Brief delay to allow rename to register
    } catch (error) {
        console.error(`Error renaming file to ${fileName}: ${error.message}`);
        throw new Error(`Failed to rename file. Check console for details.`);
    }
}

// Ensure TFile is available by accessing Obsidian's app context using a known file
let indexFile = app.vault.getAbstractFileByPath("00-index.md");
if (!indexFile) {
    const fallbackPaths = ["00-index/00-index.md", "index.md"];
    for (let path of fallbackPaths) {
        indexFile = app.vault.getAbstractFileByPath(path);
        if (indexFile) break;
    }
    if (!indexFile) {
        console.error("Error: Could not find 00-index.md, 00-index/00-index.md, or index.md. Creating 00-index.md.");
        await app.vault.create("00-index.md", "# 00-index\n\n## 🔗 Connections in My Zettelkasten");
        indexFile = app.vault.getAbstractFileByPath("00-index.md");
    }
}
const TFile = indexFile.constructor;

// Check and create backlink target files if missing, with updated paths
const backlinkNotes = [
    { name: "00-index", path: "00-index.md" },
    { name: "algebra-overview", path: "mathematics/algebra/algebra-overview.md" },
    { name: "the-lion-of-anacostia-bias-detection", path: "the-lion-of-anacostia/the-lion-of-anacostia-bias-detection.md" }
];

for (let note of backlinkNotes) {
    if (!app.vault.getAbstractFileByPath(note.path)) {
        console.warn(`Warning: ${note.name}.md not found. Creating it.`);
        if (note.name === "algebra-overview") {
            await app.vault.create(note.path, `# ${note.name.replace(/-/g, " ")}\n\n## 🔗 Connections in My Zettelkasten`);
        } else if (note.name === "the-lion-of-anacostia-bias-detection") {
            await app.vault.create(note.path, `# ${note.name.replace(/-/g, " ")}\n\n## 🔗 Connections in My Zettelkasten`);
        } else {
            await app.vault.create(note.path, `# ${note.name}\n\n## 🔗 Connections in My Zettelkasten`);
        }
    }
}

// Automatically add backlinks to key notes with a longer delay and retry mechanism
await new Promise(resolve => setTimeout(resolve, 4000)); // Increased to 4 seconds for indexing
for (let note of backlinkNotes) {
    let attempts = 2; // Retry once if needed
    while (attempts > 0) {
        try {
            let targetNote = app.vault.getAbstractFileByPath(note.path);
            if (targetNote && targetNote instanceof TFile) {
                let content = await app.vault.read(targetNote);
                if (!content.includes(`- [[${fileName}]]`)) {
                    let newContent = content.trim();
                    if (newContent.includes("## 🔗 Connections in My Zettelkasten")) {
                        newContent = newContent.replace(
                            /## 🔗 Connections in My Zettelkasten([\s\S]*?)(?=\n##|\n$)/,
                            `## 🔗 Connections in My Zettelkasten$1\n- [[${fileName}]] – Notes on ${topic} and its mathematical applications.`
                        );
                    } else {
                        newContent += `\n\n## 🔗 Connections in My Zettelkasten\n- [[${fileName}]] – Notes on ${topic} and its mathematical applications.`;
                    }
                    await app.vault.modify(targetNote, newContent);
                    break; // Success, exit loop
                }
                break; // Backlink already exists, exit loop
            } else {
                console.warn(`Attempt ${3 - attempts}: Could not find backlink note ${note.name}.md. Retrying...`);
            }
        } catch (error) {
            console.error(`Attempt ${3 - attempts} error adding backlink to ${note.name}.md: ${error.message}`);
            attempts--;
            if (attempts > 0) {
                await new Promise(resolve => setTimeout(resolve, 1000)); // Wait 1 second before retrying
            }
        }
    }
}
%>

# <% topic %>

> _"<% quote %>"_  
> — <% quoteAttribution %>

## 📌 Overview

**<% topic %>** is a fundamental **<% category %>** concept, offering insights into algebraic principles from Wang’s "Everything You Need to Ace Pre-Algebra and Algebra I in One Big Fat Notebook." It connects to bias modeling in AI and supports projects like *The Lion of Anacostia* for mathematical analysis in Africana Studies.

---

## 📂 Categories

### 🔢 **Algebra**
- **Core Concept:** [[<% fileName %>]]  
- **Foundational Topics:** [[algebra-linear-equations]]  
- **Applications:** [[algebra-bias-detection]]  
- **Historical Context:** [[algebra-overview]]  
- **Interdisciplinary Links:** [[africana-studies-overview]]  

---

## 🧮 Mathematical Context

- [ ] Explore how **<% topic %>** applies to linear equations, quadratic functions, or inequalities.  
- [ ] Identify key formulas or theorems that define its mathematical role.  
- [ ] Connect its applications to real-world problems, such as bias detection in AI.  

---

## ✍🏽 Key Figures & Contributions

### **Mathematicians**
- [ ] Key contributors (e.g., Euclid, Al-Khwarizmi, Wang).  

### **Applications in AI**
- [ ] How **<% topic %>** supports AI algorithms (e.g., linear regression for bias modeling).  

### **Educational Impact**
- [ ] Theorists and educators driving mathematical understanding.  

---

## 🌍 Impact & Applications

- [ ] How has **<% topic %>** influenced mathematics, AI, and data science?  
- [ ] What lessons does it provide for modeling bias in Africana Studies or technology?  
- [ ] Who continues to apply this concept in modern research?  

---

## 📖 Reference Notes
- [[book-summaries]] – Essential readings (e.g., Wang’s notebook).  
- [[online-articles]] – Key digital sources on algebra and AI.  
- [[research-papers]] – Scholarly insights on mathematical applications.  

---

## 🔗 Connections in My Zettelkasten
- [[00-index]] – **Main Knowledge Hub**  
- [[algebra-overview]] – **Category Overview**  
- [[<% relatedProject %>]] – **Related Project**  

---

## 📖 References
- [ ] **Core Texts & Research** (e.g., Wang’s "Everything You Need to Ace Pre-Algebra and Algebra I," AI bias studies).  

---

## 🏷️ Tags
#Algebra #<% formattedTopic %> #Mathematics #Learning #AI

📂 **File Path:** mathematics/algebra/<% fileName %>.md