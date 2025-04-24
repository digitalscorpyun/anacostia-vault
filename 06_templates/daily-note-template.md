---
aliases:
  - "<% tp.date.now('DDMMYYYY') %> Daily"
created: "<% tp.date.now('YYYY-MM-DD HH:mm') %>"
tags:
  - dailynote
  - mindset
  - productivity
  - journaling
title: "<% tp.date.now('dddd MMM D, YYYY') %> – ⚡️ Scorpyun Log"
---

## 🔗 Vault Connections

- **Goal Tracking:** [[personal-development-goal-setting]]
- **Journaling Framework:** [[personal-development-daily-journal]]
- **Priority Tasks:** [[weekly-priority-tasks]]
- **Tech & AI Workflow:** [[ai-ml-code-of-ethics]]

---

## 🌞 Morning Kickoff: Today’s Focus

> 🏆 **Main Goal:**  
<% await tp.system.prompt("Enter today's main goal") %>

> ✍🏾 **Top Priorities:**  
- <% await tp.system.prompt("Enter task 1") %>  
- <% await tp.system.prompt("Enter task 2") %>  
- <% await tp.system.prompt("Enter task 3") %>

> 🤔 **Mindset Check:**  
<% await tp.system.prompt("How are you feeling today?") %>

---

## ✝️ Verse of the Day (Optional)

<%*
let verseBlock = "";
try {
  const verse = await tp.system.prompt("Enter Verse of the Day (e.g., John 3:16 AMP)", "");
  if (verse) {
    verseBlock += `> [!verse] ${verse}\n\n`;

    let quote = await tp.web.daily_quote();
    quote = quote
      .replace(/>?\s*\[!?quote\]\s*/gi, "")
      .replace(/^>\s?/gm, "")
      .trim()
      .replace(/\n+/g, " ");
    verseBlock += `> [!quote] ${quote}`;
  }
} catch (error) {
  verseBlock += "> ⚠️ Error: Failed to fetch verse or quote.";
}
tR += verseBlock;
%>

---

## 🍎 Meal Tracker

- **Breakfast:** <% await tp.system.prompt("Enter breakfast") %>
- **Lunch:** <% await tp.system.prompt("Enter lunch") %>
- **Dinner:** <% await tp.system.prompt("Enter dinner") %>
- **Snacks:** <% await tp.system.prompt("Enter snacks") %>

---

## 📊 Daily Review

- **Yesterday’s Wins:** <% await tp.system.prompt("Enter yesterday's wins") %>
- **Challenges Faced:** <% await tp.system.prompt("Enter challenges faced") %>
- **Adjustments for Today:** <% await tp.system.prompt("Enter adjustments for today") %>

---

## 🧠 Reflections

- **Notable Achievements:** <% await tp.system.prompt("Enter notable achievements") %>
- **AI/Tech Learnings:** <% await tp.system.prompt("Enter AI/tech learnings") %>
- **Books/Articles Read:** <% await tp.system.prompt("Enter books/articles read") %>

---

## 🌙 Evening Wrap-Up

- ✅ **Did I accomplish today’s goal?**  
<% await tp.system.prompt("Did you accomplish your goal? (✅ / ❌)", "❌") %>

- 📌 **What went well?**  
<% await tp.system.prompt("What went well today?") %>

- 📌 **What needs improvement?**  
<% await tp.system.prompt("What needs improvement?") %>

- 🙏🏾 **One thing I’m grateful for today:**  
<% await tp.system.prompt("What are you grateful for today?") %>

---

🚀 *“Every day is an iteration—optimize, execute, and evolve.”*
