---
aliases:
  - "<% tp.date.now('DDMMYYYY') %> Daily"
created: "<% tp.date.now('YYYY-MM-DD HH:mm') %>"
tags:
  - dailynote
  - mindset
  - productivity
  - journaling
title: "<% tp.date.now('dddd MMM D, YYYY') %> – ⌬ Scorpyun Log"
---

## 🔗 Vault Connections

- **Goal Tracking:** [[personal-development-goal-setting]]
- **Journaling Framework:** [[personal-development-daily-journal]]
- **Priority Tasks:** [[weekly-priority-tasks]]
- **Tech & AI Workflow:** [[ai-ml-code-of-ethics]]

---

## 🌞 Morning Kickoff: Today’s Focus

🚀 _"What’s the one thing that will make today a success?"_

- **Main Goal:** 🏆 [[<% await tp.system.prompt("Enter today's main goal") %>]]
- **Top Priorities:** ✍🏾
    - [[<% await tp.system.prompt("Enter task 1") %>]]
    - [[<% await tp.system.prompt("Enter task 2") %>]]
    - [[<% await tp.system.prompt("Enter task 3") %>]]
- **Mindset Check:** 🤔 <% await tp.system.prompt("How are you feeling today?") %>

---

## ✝️ Verse of the Day (Optional)

<%*
let verseSection = "";

try {
  const verse = await tp.system.prompt("Enter Verse of the Day (e.g., John 3:16 AMP)", "");

if (verse) {
  verseSection += `> [!verse] ${verse}\n\n`;

  let quote = await tp.web.daily_quote();

  quote = quote
    .replace(/>?\s*\[!?quote\]\s*/gi, "")
    .replace(/^>\s?/gm, "")
    .trim()
    .replace(/\n+/g, " ");

  verseSection += `> [!quote]\n> ${quote}\n`;
}

} catch (error) {
  verseSection += `> **Error:** Failed to fetch verse or quote.\n`;
}

tR += verseSection;
%>




---

## 🍎 Meal Tracker (Optional)

- **Breakfast:** <% await tp.system.prompt("Enter breakfast (optional)", "") %>
- **Lunch:** <% await tp.system.prompt("Enter lunch (optional)", "") %>
- **Dinner:** <% await tp.system.prompt("Enter dinner (optional)", "") %>
- **Snacks:** <% await tp.system.prompt("Enter snacks (optional)", "") %>

---

## 📊 Progress Check-in

🔹 **Wins from Yesterday:** 🏅 <% await tp.system.prompt("Enter yesterday's wins (optional)", "") %>  
🔹 **Challenges Faced:** ⚠️ <% await tp.system.prompt("Enter challenges faced (optional)", "") %>  
🔹 **Adjustments for Today:** 🔄 <% await tp.system.prompt("Enter adjustments for today (optional)", "") %>

---

## 🧠 Key Insights & Reflections

💡 _"What lessons or breakthroughs did I have today?"_

- **Notable Achievements:** 🏆 <% await tp.system.prompt("Enter notable achievements (optional)", "") %>
- **AI/Tech Learnings:** 🤖 <% await tp.system.prompt("Enter AI/tech learnings (optional)", "") %>
- **Books/Articles Read:** 📚 <% await tp.system.prompt("Enter books/articles read (optional)", "") %>

---

## 📌 AI & Automation Workflow

- **Bias Detection:** [[the-lion-of-anacostia-bias-detection]]
- **Scripts & Automation:** [[fetch-emails]]
- **Obsidian Workflow Enhancements:** [[validate-backlinks]]

---

## 🌙 Evening Wrap-Up

🎯 _"Did I accomplish my goal for today?"_ <% await tp.system.prompt("Did you accomplish your goal? (✅ / ❌)", "❌") %>  
📌 **What went well?** <% await tp.system.prompt("What went well today? (optional)", "") %>  
📌 **What needs improvement?** <% await tp.system.prompt("What needs improvement? (optional)", "") %>  
📌 **One thing I’m grateful for today:** 🙏🏾 <% await tp.system.prompt("What are you grateful for today?", "") %>

---

🚀 _“Every day is an iteration—optimize, execute, and evolve.”_
