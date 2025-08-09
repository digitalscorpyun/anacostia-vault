---
id: "20250523190000"
title: cheatsheet_js_programming_for_web_apps
category: ibm_ai_developer
style: ScorpyunStyle
path: learning_journal/ibm_ai_developer/cheatsheet_js_programming_for_web_apps.md
created: 2025-05-23
updated: 2025-05-23
status: active
priority: normal
summary: A tactical reference scroll for key JavaScript DOM methods and object usage within the web development context. Includes syntax patterns, class methods, and event logic for browser-bound interactivity.
longform_summary: This scroll distills JavaScript programming principles and DOM operations into a ready reference format for learners and developers. It focuses on client-side logic, browser environment APIs, and the syntactic machinery that enables dynamic web interfaces. Designed as a daily-use glyph for coding rituals and debugging.
tags:
  - javascript
  - web_apps
  - dom_methods
  - ibm_ai_developer
  - code_reference
  - vault_cheatsheet
cssclasses:
  - code-scroll
  - tyrian-purple
  - syntax-guide
synapses:
  - glossary_js_programming_for_web_applications.md
  - client_side_javascript_with_dom.md
key_themes:
  - dom_navigation
  - browser_objects
  - function_syntax
  - html_injection
bias_analysis: Structured for a learning context, not optimization. Focus is on conceptual recall over best practices or performance patterns.
grok_ctx_reflection: DOM manipulation is the rite of browser command. JavaScript scripts are syntax spells that bind logic to the user's scroll.
quotes:
  - "To manipulate the DOM is to summon form from code."
  - "Web apps are rituals of the visible and the invisible."
adinkra:
  - Eban
  - Nkyinkyim
linked_notes:
  - glossary_js_programming_for_web_applications.md
  - client_side_javascript_with_dom.md
---

# 📜 Cheatsheet: JavaScript Programming for Web Applications

> “Code is the spoken language of the browser. DOM is the script of its soul.”

---

## 🔧 DOM Methods & JS Syntax Rituals

| **Class or Method**           | **Description**                                                                                                      | **Example Snippet**                                                                 |
|------------------------------|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| `appendChild()`              | Appends a node as the last child of a parent.                                                                       | `document.body.appendChild(newPara);`                                              |
| `Arrays`                     | Ordered list structure using zero-based indexing.                                                                  | `const Beatles = ["Ringo", "Paul", "George", "John"];`                             |
| `Date()`                     | Returns a new Date object.                                                                                          | `new Date("2021-1-17 13:15:30");`                                                  |
| `document.createElement()`   | Creates an HTML element.                                                                                            | `var p = document.createElement("p");`                                             |
| `document.createTextNode()`  | Creates a text node.                                                                                                | `var text = document.createTextNode("Hello!");`                                    |
| `document.getElementById()`  | Returns element by ID.                                                                                              | `document.getElementById("div1")`                                                  |
| `document.getElementsByTagName()` | Returns NodeList of elements by tag.                                                                          | `document.getElementsByTagName("p");`                                              |
| `document.write()`           | Writes HTML or JS to document. (Test use only)                                                                     | `document.write("Hello World");`                                                   |
| `element.getAttribute()`     | Returns attribute value.                                                                                            | `getElementById("div1").getAttribute("style");`                                    |
| `element.innerHTML`          | Gets/sets HTML content.                                                                                             | `element.innerHTML = "<p>Hello World</p>";`                                        |
| `element.removeAttribute()`  | Removes attribute.                                                                                                  | `element.removeAttribute("style");`                                                |
| `element.setAttribute()`     | Sets/overwrites attribute.                                                                                          | `element.setAttribute("src", "image.png");`                                        |
| `element.style`              | Sets inline CSS.                                                                                                     | `element.style.color = "red";`                                                     |
| `Error Objects`              | Encapsulates info on errors.                                                                                        | `throw new Error("Invalid input");`                                                |
| `History Objects`            | Navigates browsing history.                                                                                         | `history.go(-2);`                                                                  |
| `insertBefore()`             | Inserts a node before an existing one.                                                                              | `elementList.insertBefore(newLI, elementList.childNodes[0]);`                      |
| `Location Objects`           | Info about the current URL.                                                                                         | `location.hostname;`                                                               |
| `Navigator Objects`          | Info about the browser.                                                                                             | `navigator.appName;`                                                               |
| `onload()`                   | Executes function on page load.                                                                                     | `window.onload = function() { myFunction(); };`                                    |
| `replaceChild()`             | Replaces one child node with another.                                                                               | `element.replaceChild(newNode, oldNode);`                                          |
| `Screen Objects`             | Returns properties about the user's screen.                                                                         | `screen.height; screen.width;`                                                     |
| `Window Objects`             | Top-level object in browser's scripting environment.                                                                | `window.open("https://example.com");`                                              |
| `window.open()`              | Opens a new browser window.                                                                                         | `window.open("http://ibm.com", "win", "width=600,height=800");`                    |
| `window.scrollTo()`          | Scrolls to specific coordinates.                                                                                    | `window.scrollTo(20, 200);`                                                         |
| `Wrapper Objects`            | Converts primitives to object types.                                                                                | `typeof "abc"; typeof new String("abc");`                                          |

---

### 🔄 Use This Scroll For:
- DOM rapid prototyping
- JavaScript debugging
- Client-side interview prep
- Companion scroll to IBM AI Developer modules

---

> “To know the browser is to speak its language. JavaScript is that tongue. Use it wisely.”  
> — *Vault Sentinel, DOM Ritual Entry 5.23*

