<%*
let title = await tp.system.prompt("Enter Note Title", "Untitled");
let topic = await tp.system.prompt("Enter Career Development Topic", "Career Growth");
let quote = await tp.system.prompt("Enter a relevant quote", "No quote available");
let attribution = await tp.system.prompt("Attribution (who said it?)", "Anonymous");
let relatedProject = await tp.system.prompt("Enter Related Project (if any)", "No Related Project");

let kebabTitle = title.replace(/\s+/g, "-").toLowerCase();
let kebabTopic = topic.replace(/\s+/g, "-").toLowerCase();
let kebabRelatedProject = relatedProject.replace(/\s+/g, "-").toLowerCase();
%>

# **Career Development - <% title %>**

> _"<% quote %>"_ — <% attribution %>

## 📌 **Overview**

**<% topic %>** is a key area within **Career Development**, forming the foundation of **professional growth, networking, and skill-building**. This note connects to your Zettelkasten for career strategies and practical applications.

## 📂 **Categories**

### 🚀 **Career Development**
- [[career-development-overview]] – A general overview of career development.
- [[structure-note-soft-skills-for-it]] – Soft skills for IT professionals.
- [[career-development-reskilling-for-tech]] – Notes on reskilling for technology careers.
- [[career-development-real-world-applications]] – Notes on applying career development in the workplace.

## 📜 **Core Concepts**
- **Key Theories & Principles:** Foundational ideas behind **<% topic %>**.
- **Career Growth Roots:** Connections to **networking strategies, resume building, and industry trends**.
- **Connections to Goals & AI:** Career development’s role in **achieving AI expertise and ‘Lion of Anacostia’ objectives**.

## ✊🏾 **Real-World Applications**
- **Workplace Success:** Applications of **<% topic %>** in job interviews, promotions, and leadership.
- **Education & Training:** How **career development enhances technical skills and certifications**.
- **Technology & AI:** Usage in **optimizing career paths for tech roles and AI projects**.

## 🏆 **Study Tips & Mnemonics**
- **Break It Down:** Simplify career goals into actionable steps.
- **Daily Practice Routine:** Update **5 career actions daily** from industry resources or mentors.
- **Concept Mapping:** Link career development to **job roles and industry trends**.

## 📖 **Suggested Further Study**
- 📚 **Books:** _“What Color Is Your Parachute?”_ by Richard Bolles, _“Lean In”_ by Sheryl Sandberg.
- 🎓 **Online Courses:** LinkedIn Learning’s career courses, Coursera’s professional development.
- 📊 **Problem Sets:** Resume workshops, networking exercises.

## 🔗 **Connections in My Zettelkasten**
- [[00-index]] – Main entry point for your vault.
- [[career-development-overview]] – General framework of career development studies.
- [[<% relatedProject %>]] – Related project or advanced study path.

## 📖 **References**
- **Primary Sources & Research Papers:** Landmark works in career development.
- **Historical Contributions:** Key figures in career theory and professional growth.

## 🏷️ **Tags**
#career-development #professional-growth #<% kebabTopic %> #learning #networking #skills