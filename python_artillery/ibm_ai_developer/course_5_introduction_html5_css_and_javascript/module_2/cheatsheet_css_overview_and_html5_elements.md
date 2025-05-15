---
id: '20250511112837'
title: Cheatsheet – CSS Overview & HTML5 Elements
category: ibm_ai_certification
style: ScorpyunStyle
path: ''
created: 2025-05-05 16:30
updated: '2025-05-11'
status: in_progress
priority: normal
summary: Quick reference guide for HTML5 tags and CSS elements, aligned with Course
  5 of the IBM AI Developer track.
longform_summary: ''
tags:
- ibm_ai_developer
- html
- css
- cheatsheet
- frontend_basics
- od_comply
cssclasses:
- ibm-track
- html-css-cheatsheet
synapses: []
key_themes: []
bias_analysis: ''
grok_ctx_reflection: ''
quotes: []
adinkra: []
linked_notes: []
---


# 🎯 Cheatsheet – CSS Overview & HTML5 Elements

> _Part of the IBM AI Developer Certification – Course 5_  
> Structured for rapid lookup and sacred-tech front-end fluency.

---

## 🧱 HTML Document Structure

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Document Title</title>
  </head>
  <body>
    Document body here
  </body>
</html>
```

---

## 🔗 Linking & Metadata

- `<link rel="stylesheet" href="styles.css">` – Link external CSS file  
- `<meta name="author" content="Your Name">` – Document metadata  
- `<title>` – Sets the browser tab title  

---

## 🌐 Semantic Elements (Structured Meaning)

<details>
<summary><code>&lt;article&gt;</code> – Self-contained content unit</summary>

```html
<article class="CSS-Style-Reference">
  <h2>HTML</h2>
  <p>HTML is the markup language used to structure content on the web.</p>
</article>
```
</details>

<details>
<summary><code>&lt;aside&gt;</code> – Tangential or side content</summary>

```html
<aside>
  This section contains related but secondary information.
</aside>
```
</details>

<details>
<summary><code>&lt;section&gt;</code> – Logical document chunk</summary>

```html
<section>
  <h2>Introduction</h2>
  <p>This section introduces the document content.</p>
</section>
```
</details>

<details>
<summary><code>&lt;header&gt;</code> & <code>&lt;footer&gt;</code> – Intro/outro content containers</summary>

```html
<header>
  <h1>Header Title</h1>
</header>

<footer>
  <p>Author: digitalscorpyun</p>
</footer>
```
</details>

---

## 🔁 Forms & Input

<details>
<summary>Form Template with Fieldset</summary>

```html
<form action="/script.php">
  <fieldset>
    <legend>User:</legend>
    <label for="fname">First name:</label>
    <input type="text" id="fname" name="fname"><br><br>
    <label for="lname">Last name:</label>
    <input type="text" id="lname" name="lname"><br><br>
    <input type="submit" value="Submit">
  </fieldset>
</form>
```
</details>

---

## 📷 Media & Layout

<details>
<summary><code>&lt;figure&gt;</code> + <code>&lt;figcaption&gt;</code></summary>

```html
<figure>
  <img src="durham.jpg" width="300" height="300">
  <figcaption>Fig.1 – Durham, NC</figcaption>
</figure>
```
</details>

<details>
<summary><code>&lt;div&gt;</code> – Style wrapper block</summary>

```html
<div>
  Used to apply CSS styling to grouped content.
</div>
```
</details>

---

## 📄 Text Content

- `<p>` – Paragraph  
- `<h1>` to `<h6>` – Headings hierarchy  
- `<a href="https://example.com">Link</a>` – Anchor tag  
- `<ul>`, `<ol>`, `<li>` – Lists  

---

## 🧠 Logic & Styling

<details>
<summary><code>&lt;script&gt;</code> – JavaScript embedding</summary>

```html
<script>
  alert("Hello World");
</script>
```
</details>

<details>
<summary><code>&lt;style&gt;</code> – Inline CSS</summary>

```html
<head>
  <style>
    p { color: red; }
  </style>
</head>
```
</details>

---

## 🧾 Tables

```html
<table>
  <tr>
    <th>Header 1</th><th>Header 2</th>
  </tr>
  <tr>
    <td>Cell 1A</td><td>Cell 1B</td>
  </tr>
  <tr>
    <td>Cell 2A</td><td>Cell 2B</td>
  </tr>
</table>
```

---

## 📌 Notes

- Always include `<!DOCTYPE html>` as the first line  
- Semantic tags help with accessibility and SEO  
- `<div>` and `<span>` are non-semantic but useful for layout/styling  
- Use `<fieldset>` to group form fields visually and semantically  

---

_This cheatsheet will evolve as your coursework deepens. Track updates with `course_ref: course_5_html_css_js`._
