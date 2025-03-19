Here’s a structured **Markdown note** for Python dictionary methods, formatted for easy import into **Obsidian**.

---

### **python-dictionary-methods.md**

````markdown
# Python Dictionary Methods

## 📝 Overview
Dictionaries in Python are key-value pairs that allow efficient data retrieval. This note covers essential dictionary methods for creating, modifying, and managing dictionaries.

---

## 🏗️ Creating Dictionaries
```python
# Empty dictionary
my_dict = {}

# Dictionary with initial values
person = {"name": "John", "age": 30, "city": "New York"}
````

---

## 🔍 Accessing Dictionary Values

```python
# Using keys
print(person["name"])  # Output: John

# Using get() (avoids KeyError)
print(person.get("age"))  # Output: 30
print(person.get("gender", "Not Found"))  # Output: Not Found
```

---

## ✏️ Adding & Updating Values

```python
# Adding a new key-value pair
person["gender"] = "Male"

# Updating an existing value
person["age"] = 31

# Using update() to merge dictionaries
person.update({"city": "Los Angeles", "job": "Engineer"})
```

---

## ❌ Removing Items

```python
# Using del
del person["job"]

# Using pop() (removes and returns value)
age = person.pop("age")

# Using popitem() (removes last inserted item)
last_item = person.popitem()

# Using clear() (removes all items)
person.clear()
```

---

## 🔄 Dictionary Methods Reference

|Method|Description|
|---|---|
|`.get(key, default)`|Returns value for `key`, else returns `default`|
|`.keys()`|Returns all keys as a view object|
|`.values()`|Returns all values as a view object|
|`.items()`|Returns key-value pairs as tuples|
|`.update(dict2)`|Merges `dict2` into the current dictionary|
|`.pop(key, default)`|Removes `key` and returns value (or `default` if missing)|
|`.popitem()`|Removes and returns the last inserted key-value pair|
|`.clear()`|Empties the dictionary|
|`.setdefault(key, default)`|Returns value of `key`, else sets it to `default`|

---

## 🔍 Iterating Through a Dictionary

```python
# Loop through keys
for key in person.keys():
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 🎯 Dictionary Comprehensions

```python
# Squaring numbers using dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## 🔗 Connections in My Zettelkasten

- [[python-basics.md]]
- [[python-data-structures.md]]
- [[python-advanced-topics.md]]
- [Accessing Dictionary Items in Python](https://www.youtube.com/watch?v=6RAWUwWmlOg)

---

```

Would you like any adjustments before saving? 🚀
```