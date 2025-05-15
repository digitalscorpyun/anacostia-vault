---
id: '20250511112837'
title: python_basics
category: technical_mastery_python
style: ScorpyunStyle
path: ''
created: '2025-05-09'
updated: '2025-05-11'
status: in_progress
priority: normal
summary: Foundational guide to Python syntax and logic structures, designed to initiate
  mastery of clean scripting, automation, and agent-based programming within the Anacostia
  Vault.
longform_summary: ''
tags:
- python
- programming_basics
- foundational_skills
- technical_mastery
- scorpyunstyle
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


# 🐍 Python Basics

## 📘 Overview

This note anchors the beginning of your Python ritual. These are not just programming fundamentals—they are **glyphs of control**, essential for automation, vault ops, and agent logic. Mastery begins here.

---

## 🧱 Variables & Data Types

### ✍🏽 Assignment & Naming

```python
x = 10
name = "digitalscorpyun"
Variables are dynamically typed.

Always use snake_case in sacred-tech codebases.

📊 Core Data Types
Type	Example
int	42
float	3.14
str	"scorpyun"
bool	True, False
list	[1, 2, 3]
tuple	("vault", 9)
dict	{"name": "Scorpyun"}
set	{1, 2, 3}

🔁 Control Flow
🧭 Conditional Logic
python
Copy
Edit
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
Use if/elif/else for decision-making.

🔄 Loops
python
Copy
Edit
for item in [1, 2, 3]:
    print(item)

while x < 5:
    x += 1
Loop over ranges, lists, dictionaries with intentional control.

🧮 Functions
python
Copy
Edit
def greet(name):
    """Return a ritualized welcome."""
    return f"Welcome, {name}."
Use def to define functions.

Include docstrings ("""text""") for clarity and sacred-tech discipline.

Return values with return.

🧯 Exception Handling
python
Copy
Edit
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero not allowed.")
Use try / except to manage error paths.

finally and else can control flow refinement.

🧠 Type Hints
python
Copy
Edit
def square(n: int) -> int:
    return n * n
Introduced in Python 3.5+, refined since.

Improves readability and tool compatibility (mypy, pylance).

Required for agent-compatible scripts in AVM pipelines.

🔗 Next Steps
Study [[python_overview]] for language evolution & syntax upgrades.

Follow [[python_learning_roadmap]] or [[python_learning_path]] for phased mastery.

Dive into [[python_scripts]] to view real-world sacred-tech usage.

Apply skills in ML logic via [[ai_ml_overview]].

🧪 Practice Prompts
Create a function that calculates compound interest.

Write a script to check whether a string is a palindrome.

Build a dictionary of your top 3 AI models and iterate through it.

“Master the loop, and you master the cycle. Build the function, and you build the future.”
— digitalscorpyun, Algorithmic Griot