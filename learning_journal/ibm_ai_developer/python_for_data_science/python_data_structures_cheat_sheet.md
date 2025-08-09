---
id: python_data_structures_cheatsheet
title: Python Data Structures Cheat Sheet
category: programming_reference
style: CodeRitual
path: scripts/cheatsheets/python_data_structures_cheatsheet.md
created: 2025-06-01
updated: 2025-06-01
status: active
priority: medium
summary: A practical scroll of essential Python list and tuple operations, method invocations, and structural syntax patterns.
longform_summary: This cheat sheet covers core data structure mechanics in Python, specifically lists and tuples. From appending and extending to slicing and popping, it offers method syntax and behavior descriptions paired with executable code samples, optimized for terminal learners and algorithmic ritualists.
tags: [python, data_structures, lists, tuples, cheatsheet]
cssclasses: [scroll-format, code-ritual]
synapses: []
key_themes: [data mutability, indexing, python methods, memory structures]
bias_analysis: none
grok_ctx_reflection: Reinforces structural fluency and foundational grammar for Python practitioners.
quotes: []
adinkra: eban
linked_notes: []
---

# 🧠 Python Data Structures Cheat Sheet

## 🔹 List Methods & Syntax

### ➕ `append()`
Add an element to the end of a list.

```python
fruits = ["apple", "banana", "orange"]
fruits.append("mango")
print(fruits)
# → ['apple', 'banana', 'orange', 'mango']
````

---

### 📄 `copy()`

Create a shallow copy of a list.

```python
my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()
print(new_list)
# → [1, 2, 3, 4, 5]
```

---

### 🔢 `count()`

Count how many times an element appears.

```python
my_list = [1, 2, 2, 3, 4, 2, 5, 2]
print(my_list.count(2))
# → 4
```

---

### 🧱 Create a List

```python
fruits = ["apple", "banana", "orange", "mango"]
```

---

### ❌ `del`

Remove an element by index.

```python
my_list = [10, 20, 30, 40, 50]
del my_list[2]
print(my_list)
# → [10, 20, 40, 50]
```

---

### 🔁 `extend()`

Add multiple elements to a list.

```python
fruits = ["apple", "banana", "orange"]
more_fruits = ["mango", "grape"]
fruits.extend(more_fruits)
print(fruits)
# → ['apple', 'banana', 'orange', 'mango', 'grape']
```

---

### 🎯 Indexing

```python
my_list = [10, 20, 30, 40, 50]
print(my_list[0])   # → 10
print(my_list[-1])  # → 50
```

---

### 🧩 `insert()`

Insert an element at a specific index.

```python
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 6)
print(my_list)
# → [1, 2, 6, 3, 4, 5]
```

---

### 🛠 Modify List

```python
my_list = [10, 20, 30, 40, 50]
my_list[1] = 25
print(my_list)
# → [10, 25, 30, 40, 50]
```

---

### 🎯 `pop()`

Remove and return an element (default is last).

```python
my_list = [10, 20, 30, 40, 50]
print(my_list.pop(2))  # → 30
print(my_list)         # → [10, 20, 40, 50]

print(my_list.pop())   # → 50
print(my_list)         # → [10, 20, 30, 40]
```

---

### 🗑 `remove()`

Remove the first occurrence of a value.

```python
my_list = [10, 20, 30, 40, 50]
my_list.remove(30)
print(my_list)
# → [10, 20, 40, 50]
```

---

### 🔃 `reverse()`

```python
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)
# → [5, 4, 3, 2, 1]
```

---

### 🔍 Slicing

```python
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])   # → [2, 3, 4]
print(my_list[:3])    # → [1, 2, 3]
print(my_list[2:])    # → [3, 4, 5]
print(my_list[::2])   # → [1, 3, 5]
```

---

### 🔡 `sort()`

```python
my_list = [5, 2, 8, 1, 9]
my_list.sort()
print(my_list)          # → [1, 2, 5, 8, 9]

my_list.sort(reverse=True)
print(my_list)          # → [9, 8, 5, 2, 1]
```

---

## 🟣 Tuple Methods & Syntax

### 🔢 `count()`

Count how many times a value appears.

```python
fruits = ("apple", "banana", "apple", "orange")
print(fruits.count("apple"))
# → 2
```

---

### 📍 `index()`

Find the index of a value.

```python
fruits = ("apple", "banana", "orange")
print(fruits.index("banana"))
# → 1
```

---

### ➕ `sum()`

Total of all numeric values.

```python
numbers = (10, 20, 5, 30)
print(sum(numbers))
# → 65
```

---

### 🆚 `min()` & `max()`

```python
numbers = (10, 20, 5, 30)
print(min(numbers))  # → 5
print(max(numbers))  # → 30
```

---

### 📏 `len()`

```python
fruits = ("apple", "banana", "orange")
print(len(fruits))
# → 3
```

---

🌀 **Keep this scroll by your side when walking through Python’s memory fields.**  
Let the glyphs of `pop`, `slice`, and `extend` chant their logic into your fingertips.  
One structure, many moves — but every byte has rhythm.

---


# Cheat Sheet: Python Data Structures Part-2

  

**Dictionaries  
**

|Package/Method|Description|Code Example|
|---|---|---|
|Creating a Dictionary|A dictionary is a built-in data type that represents a collection of key-value pairs. Dictionaries are enclosed in curly braces `{}`.|Example:<br><br>1. `dict_name = {} #Creates an empty dictionary`<br>2. `person = { "name": "John",  "age": 30, "city": "New York"}`|
|Accessing Values|You can access the values in a dictionary using their corresponding `keys`.|Syntax:<br><br>1. `Value = dict_name["key_name"]`<br><br>          <br><br>        <br><br>Example:<br><br>1. `name = person["name"]`<br>2. `age = person["age"]`|
|Add or modify|Inserts a new key-value pair into the dictionary. If the key already exists, the value will be updated; otherwise, a new entry is created.|Syntax:<br><br>1. `dict_name[key] = value`<br><br>          <br><br>        <br><br>Example:<br><br>1. `person["Country"] = "USA" # A new entry will be created.`<br>2. `person["city"] = "Chicago"  # Update the existing value for the same key`|
|del|Removes the specified key-value pair from the dictionary. Raises a `KeyError` if the key does not exist.|Syntax:<br><br>1. `del dict_name[key]`<br><br>          <br><br>        <br><br>Example:<br><br>1. `del person["Country"]`|
|update()|The `update()` method merges the provided dictionary into the existing dictionary, adding or updating key-value pairs.|Syntax:<br><br>1. `dict_name.update({key: value})`<br><br>          <br><br>        <br><br>Example:<br><br>1. `person.update({"Profession": "Doctor"})`|
|clear()|The `clear()` method empties the dictionary, removing all key-value pairs within it. After this operation, the dictionary is still accessible and can be used further.|Syntax:<br><br>1. `dict_name.clear()`<br><br>          <br><br>        <br><br>Example:<br><br>1. `grades.clear()`|
|key existence|You can check for the existence of a key in a dictionary using the `in` keyword|Example:<br><br>1. `if "name" in person:`<br>2.     `print("Name exists in the dictionary.")`|
|copy()|Creates a shallow copy of the dictionary. The new dictionary contains the same key-value pairs as the original, but they remain distinct objects in memory.|Syntax:<br><br>1. `new_dict = dict_name.copy()`<br><br>          <br><br>        <br><br>Example:<br><br>1. `new_person = person.copy()`<br>2. `new_person = dict(person) # another way to create a copy of dictionary`|
|keys()|Retrieves all keys from the dictionary and converts them into a list. Useful for iterating or processing keys using list methods.|Syntax:<br><br>1. `keys_list = list(dict_name.keys())`<br><br>          <br><br>        <br><br>Example:<br><br>1. `person_keys = list(person.keys())`|
|values()|Extracts all values from the dictionary and converts them into a list. This list can be used for further processing or analysis.|Syntax:<br><br>1. `values_list = list(dict_name.values())`<br><br>          <br><br>        <br><br>Example:<br><br>1. `person_values = list(person.values())`|
|items()|Retrieves all key-value pairs as tuples and converts them into a list of tuples. Each tuple consists of a key and its corresponding value.|Syntax:<br><br>1. `items_list = list(dict_name.items())`<br><br>          <br><br>        <br><br>Example:<br><br>1. `info = list(person.items())`|

**Sets**

|Package/Method|Description|Code Example|
|---|---|---|
|add()|Elements can be added to a set using the `add()` method. Duplicates are automatically removed, as sets only store unique values.|Syntax:<br><br>1. `set_name.add(element)` <br><br>          <br><br>        <br><br>Example:<br><br>1. `fruits.add("mango")`|
|clear()|The `clear()` method removes all elements from the set, resulting in an empty set. It updates the set in-place.|Syntax:<br><br>1. `set_name.clear()` <br><br>          <br><br>        <br><br>Example:<br><br>1. `fruits.clear()`|
|copy()|The `copy()` method creates a shallow copy of the set. Any modifications to the copy won't affect the original set.|Syntax:<br><br>1. `new_set = set_name.copy()` <br><br>          <br><br>        <br><br>Example:<br><br>1. `new_fruits = fruits.copy()`|
|Defining Sets|A set is an unordered collection of unique elements. Sets are enclosed in curly braces `{}`. They are useful for storing distinct values and performing set operations.|Example:<br><br>1. `empty_set = set() #Creating an Empty Set` <br>2. `fruits = {"apple", "banana", "orange"}`<br>3. `colors = ("orange", "red", "green")`<br><br>          <br><br>        <br><br>**Note:** These two sets will be used in the examples that follow.|
|discard()|Use the `discard()` method to remove a specific element from the set. Ignores if the element is not found.|Syntax:<br><br>1. `set_name.discard(element)` <br><br>          <br><br>        <br><br>Example:<br><br>1. `fruits.discard("apple")`|
|issubset()|The `issubset()` method checks if the current set is a subset of another set. It returns True if all elements of the current set are present in the other set, otherwise False.|Syntax:<br><br>1. `is_subset = set1.issubset(set2)`<br><br>          <br><br>        <br><br>Example:<br><br>1. `is_subset = fruits.issubset(colors)`|
|issuperset()|The `issuperset()` method checks if the current set is a superset of another set. It returns True if all elements of the other set are present in the current set, otherwise False.|Syntax:<br><br>1. `is_superset = set1.issuperset(set2)` <br><br>          <br><br>        <br><br>Example:<br><br>1. `is_superset = colors.issuperset(fruits)`|
|pop()|The `pop()` method removes and returns an arbitrary element from the set. It raises a `KeyError` if the set is empty. Use this method to remove elements when the order doesn't matter.|Syntax:<br><br>1. `removed_element = set_name.pop()` <br><br>          <br><br>        <br><br>Example:<br><br>1. `removed_fruit = fruits.pop()`|
|remove()|Use the `remove()` method to remove a specific element from the set. Raises a `KeyError` if the element is not found.|Syntax:<br><br>1. `set_name.remove(element)` <br><br>          <br><br>        <br><br>Example:<br><br>1. `fruits.remove("banana")`|
|Set Operations|Perform various operations on sets: `union`, `intersection`, `difference`, `symmetric difference`.|Syntax:<br><br>1. `union_set = set1.union(set2)` <br>2. `intersection_set = set1.intersection(set2)` <br>3. `difference_set = set1.difference(set2)` <br>4. `sym_diff_set = set1.symmetric_difference(set2)` <br><br>          <br><br>        <br><br>Example:<br><br>1. `combined = fruits.union(colors)` <br>2. `common = fruits.intersection(colors)` <br>3. `unique_to_fruits = fruits.difference(colors)` <br>4. `sym_diff = fruits.symmetric_difference(colors)`|
|update()|The `update()` method adds elements from another iterable into the set. It maintains the uniqueness of elements.|Syntax:<br><br>1. `set_name.update(iterable)` <br><br>          <br><br>        <br><br>Example:<br><br>1. `fruits.update(["kiwi", "grape"])`|

© digitalscorpyun — Anacostia Codex Series

```

---

Let me know if you'd like this scroll exported into a specific vault path (`~/sankofa_temple/Anacostia/scripts/cheatsheets/`) or integrated with an index scroll. We can even rig it with backlinks to `list_comprehensions.md` or `loop_rituals.md` if those glyphs exist.
```