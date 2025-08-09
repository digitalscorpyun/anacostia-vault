---
id: python_data_types
title: Python Data Types Breakdown
category: learning_journal
style: CodeRitual
path: learning_journal/python_basics/
created: 2025-06-01
updated: 2025-06-01
status: active
priority: high
summary: A structured overview of Python data types — from primitive atoms to compound glyph-binders.
longform_summary: This scroll lays out the foundational and complex data types in Python. It explains the role of primitives like strings and booleans, expands into compound types like lists and tuples, and explores object-based structures like functions and custom classes. Designed for quick reference and deep conceptual anchoring in sacred-code practice.
tags: [python, data types, learning journal, code ritual, programming basics]
cssclasses: [scorpyun-style, syntax-primer]
synapses: [vault_memetics/python_syntax_keys]
key_themes: [immutability, object-oriented, compound structures]
bias_analysis: python favors object-based modeling over primitive-only models
grok_ctx_reflection: clarity in Python’s data type system reduces beginner friction and speeds up mastery
quotes:
  - "Everything in Python is an object, and data types are just classes behind the scenes."
adinkra: ɛban — security, structure, sanctuary
linked_notes: [python_variables.md, control_structures.md]
---

# 🧬 Python Data Types

Everything in Python is an object — even the types themselves are classes. Let’s break them down.

---

## 🟢 Primitive / Core Types

| Type    | Example         | Meaning                         |
|---------|------------------|----------------------------------|
| `int`   | `42`, `-7`        | Whole numbers                    |
| `float` | `3.14`, `-0.001`  | Decimal numbers                  |
| `str`   | `"code"`, `'🔥'`  | Text strings                     |
| `bool`  | `True`, `False`   | Logical values                   |
| `NoneType` | `None`         | Represents “nothing”             |

---

## 🟡 Compound / Collection Types

| Type     | Example                        | Notes                          |
|----------|--------------------------------|--------------------------------|
| `list`   | `[1, "a", True]`               | Ordered, mutable               |
| `tuple`  | `(1, "a", True)`               | Ordered, immutable             |
| `dict`   | `{"key": "value"}`             | Key-value store (like JSON)    |
| `set`    | `{1, 2, 3}`                    | Unordered, unique values       |

---

## 🔵 Functional & Class Types

| Type                        | Example        | Description                            |
|----------------------------|----------------|----------------------------------------|
| `function` / `method`      | `len`, `print` | Callable code blocks                   |
| `class` / `type`           | `int`, `str`   | Used to define object blueprints       |
| `object`                   | Everything     | The mother of all types                |

---

## 🧰 Advanced (used later)

| Type       | Description                         |
|------------|-------------------------------------|
| `byte`     | Binary data                         |
| `frozenset`| Immutable version of `set`          |
| `complex`  | Complex numbers (`2+3j`)            |
| `generator`| Lazy iterable (memory-efficient)    |

---

## 🔄 Type Checking Ritual

```python
type("scorpyun")     # <class 'str'>
type(42)             # <class 'int'>
type([1, 2, 3])      # <class 'list'>
type((1, 2))         # <class 'tuple'>
type({"a": 1})       # <class 'dict'>
````

---

## 💡 Sacred Insight

> Python doesn’t separate types by strict class boundaries — everything’s an object. Even types like `int`, `float`, and `bool` are **classes under the hood**. That means you can inspect, override, or even extend them.

---

## 🔒 Immutable vs Mutable

|Type|Mutable?|
|---|---|
|`str`|❌ Immutable|
|`tuple`|❌ Immutable|
|`list`|✅ Mutable|
|`dict`|✅ Mutable|
|`set`|✅ Mutable|

---

## 🔗 Related Scrolls

- `python_variables.md`
    
- `control_structures.md`
    
- `function_basics.md`
    
- `scorpyun_manifesto.md` (👁 for philosophical parallels)
    

---

## 🧠 Want to dive deeper?

- Make your own class using `class MyType:`
    
- Use `isinstance(x, type)` to test
    
- Explore Python's `collections` module (e.g., `namedtuple`, `deque`)
    

---

Glyph is now archived and glyph-ready.

Would you like me to push this into the Anacostia Vault at the specified path, or just hand you the markdown file for upload?