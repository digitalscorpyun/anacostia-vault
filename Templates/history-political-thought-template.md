<%*
let title = await tp.system.prompt("Enter Note Title", "Untitled");
let topic = await tp.system.prompt("Enter History/Political Thought Topic", "Political Theory");
let quote = await tp.system.prompt("Enter a relevant quote", "No quote available");
let attribution = await tp.system.prompt("Attribution (who said it?)", "Anonymous");
let relatedProject = await tp.system.prompt("Enter Related Project (if any)", "No Related Project");

let kebabTitle = title.replace(/\s+/g, "-").toLowerCase();
let kebabTopic = topic.replace(/\s+/g, "-").toLowerCase();
let kebabRelatedProject = relatedProject.replace(/\s+/g, "-").toLowerCase();
%>

# **History & Political Thought - <% title %>**

> _"<% quote %>"_ — <% attribution %>

## 📌 **Overview**

**<% topic %>** is a key area within **History & Political Thought**, forming the foundation of **political analysis, historical context, and societal understanding**. This note connects to your Zettelkasten for historical and political insights and practical applications.

## 📂 **Categories**

### 📖 **History & Political Thought**
- [[history-political-thought-overview]] – A general overview of history and political thought.
- [[structure-note-political-theories]] – Theories of governance and power.
- [[history-political-thought-the-rise-of-totalitarianism]] – Notes on the rise of totalitarianism.
- [[history-political-thought-real-world-applications]] – Notes on applying historical insights in modern politics.

## 📜 **Core Concepts**
- **Key Theories & Principles:** Foundational ideas behind **<% topic %>**.
- **Historical Roots:** Connections to **key events, philosophers, and political movements**.
- **Connections to Goals & AI:** History’s role in **understanding bias, ethics, and ‘Lion of Anacostia’ objectives**.

## ✊🏾 **Real-World Applications**
- **Governance & Policy:** Applications of **<% topic %>** in modern political systems and policy-making.
- **Education & Research:** How **history and political thought inform academic study and activism**.
- **Technology & AI:** Usage in **analyzing political data and ethical AI frameworks**.

## 🏆 **Study Tips & Mnemonics**
- **Break It Down:** Simplify historical events into timelines and causes.
- **Daily Practice Routine:** Read **5 pages daily** from historical texts or political analyses.
- **Concept Mapping:** Link political theories to **historical events and modern implications**.

## 📖 **Suggested Further Study**
- 📚 **Books:** _“On Tyranny”_ by Timothy Snyder, _“The Origins of Totalitarianism”_ by Hannah Arendt.
- 🎓 **Online Courses:** Coursera’s “Modern & Contemporary American Politics,” Udemy’s history courses.
- 📊 **Problem Sets:** Case studies, political essay prompts.

## 🔗 **Connections in My Zettelkasten**
- [[00-index]] – Main entry point for your vault.
- [[history-political-thought-overview]] – General framework of history and political thought studies.
- [[<% relatedProject %>]] – Related project or advanced study path.

## 📖 **References**
- **Primary Sources & Research Papers:** Landmark works in history and political thought.
- **Historical Contributions:** Key figures like Aristotle, Machiavelli, and Hobbes.

## 🏷️ **Tags**
#history-political-thought #politics #<% kebabTopic %> #learning #society #ethics