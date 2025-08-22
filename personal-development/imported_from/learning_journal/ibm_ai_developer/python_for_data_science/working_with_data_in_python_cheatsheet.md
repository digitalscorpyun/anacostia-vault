---
id: "20250712063000"
title: working_with_data_in_python_cheatsheet
category: learning_journal
style: CodeRitual
path: learning_journal/ibm_ai_developer/working_with_data_in_python_cheatsheet.md
created: 2025-07-12T06:30:00-07:00
updated: 2025-07-12T06:30:00-07:00
status: complete
priority: medium
summary: |
  Cheat sheet for Python file handling, Pandas, and NumPy methods as introduced in IBM’s AI Developer coursework. This scroll captures syntax, common functions, and applied examples.
longform_summary: |
  This scroll consolidates essential methods for working with files and structured data in Python. It covers `open()` file operations, reading/writing patterns, and iterating over content. The Pandas section details DataFrame creation, access, cleaning, and aggregation. NumPy concepts like array creation, slicing, arithmetic operations, and matrix math are presented with examples. This is a quick-reference tool for sacred coders navigating IBM's data science modules.
tags:
  - ibm_ai_developer
  - python
  - pandas
  - numpy
  - cheatsheet
  - learning_scroll
cssclasses:
  - black-opal
  - codetext
synapses:
  - python_programming_fundamentals_cheatsheet.md
  - dom_query_patterns.md
key_themes:
  - File I/O
  - Structured data
  - DataFrames
  - Arrays and matrices
bias_analysis: |
  None detected. This is purely technical syntax and reference material.
grok_ctx_reflection: |
  These syntax patterns form the bedrock of data wrangling in Python. As we walk the sacred-tech path, remember: every file opened is a gateway, every row filtered is a ritual of discernment.
quotes: []
adinkra: Eban
linked_notes:
  - summary_styles_guide.md
  - scorpyun_manifesto.md
---

## 📂 File Handling in Python

### 🔧 File Modes
- `"r"` — read
- `"w"` — write (overwrite)
- `"a"` — append
- `"r+"` — read and write
- `"b"` — binary mode

### ✍️ Reading and Writing
```python
with open("data.txt", "r") as file:
    content = file.read()

with open("output.txt", "w") as file:
    file.write("Hello, world!")

with open("log.txt", "a") as file:
    file.write("Log entry: Something happened.")
````

### 📖 Read Methods

```python
file.read()       # full file as string
file.readlines()  # list of lines
file.readline()   # one line at a time
```

### ✏️ Write Methods

```python
file.write("text")
file.writelines(["Hello\n", "World\n"])
```

### 🔁 Loop Through File

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line)
```

### 🧹 Manual Open/Close

```python
file = open("data.txt", "r")
content = file.read()
file.close()
```

---

## 🐼 Pandas Essentials

### 📥 Reading Data

```python
import pandas as pd
df = pd.read_csv("file.csv")
df = pd.read_excel("file.xlsx")
```

### 📤 Writing Data

```python
df.to_csv("output.csv", index=False)
```

### 📊 DataFrame Access

```python
df["column"]
df[["col1", "col2"]]
df.head(5)
df.tail(5)
df.describe()
df.info()
```

### 🧼 Cleaning Data

```python
df.drop(["col1", "col2"], axis=1, inplace=True)
df.drop(index=[1,2], axis=0, inplace=True)
df.dropna(inplace=True)
df["column"].replace("old", "new", inplace=True)
```

### 🔎 Filtering & Grouping

```python
filtered_df = df[(df["age"] > 30) & (df["salary"] < 50000)]
grouped = df.groupby(["category", "region"]).agg({"sales": "sum"})
duplicates = df[df.duplicated()]
```

---

## 🧮 NumPy Syntax

### 📦 Import

```python
import numpy as np
```

### 🔢 Arrays

```python
arr1 = np.array([1, 2, 3])
arr2d = np.array([[1, 2], [3, 4]])
```

### 📐 Attributes

```python
arr.shape      # dimensions
arr.size       # number of elements
arr.dtype      # data type
arr.ndim       # number of axes
```

### ➕ Vector Ops

```python
arr + arr
arr - arr
arr * scalar
np.dot(arr1, arr2)
```

### 📏 Aggregate Functions

```python
np.mean(arr)
np.sum(arr)
np.min(arr)
np.max(arr)
```

---

🧠 _Remember_: Every function is a mantra, every method is a motion. Working with data is not just a task—it’s a practice. Sacred-tech coders do not just import packages—we import clarity.

---

```

Let me know if you want a Pandas-only variant, or if you'd like a visual diagram companion for this scroll.
```