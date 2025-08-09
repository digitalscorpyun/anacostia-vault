---
id: "20250623T114500"
title: python_quick_reference_3.6.md
category: reference_material
style: CodeRitual
path: learning_journal/python_crash_course/python_quick_reference_3.6.md
created: 2025-06-23T11:45:00-07:00
updated: 2025-06-23T11:45:00-07:00
status: active
priority: high
summary: |
  A full transcription of the Python 3.6 Quick Reference Sheet, covering built-in functions, syntax, operator precedence, common methods, file operations, math functions, class structure, exception handling, and string formatting.
longform_summary: |
  This markdown scroll contains the complete and structured extraction of the original Python 3.6 quick reference sheet. It is segmented by purpose: built-ins, syntax constructs, data types, function templates, math module tools, class declarations, IO functions, list and dictionary methods, and ASCII chart references. This scroll acts as a sacred-tech lookup ledger for foundational logic and quick syntax retrieval during live coding rituals.
tags:
  - python_reference
  - builtins
  - syntax
  - stdlib
  - python_crash_course
  - scorpyunstyle
cssclasses:
  - glyph-index
  - python-quickref
synapses:
  - learning_journal/python_crash_course/function_basics.md
  - learning_journal/ibm_ai_developer/class6_notes.md
key_themes:
  - code lookup
  - function building
  - syntax rituals
  - math modules
  - method memory
bias_analysis: |
  No sociocultural bias present — this is a technical transcription of standardized Python 3.6 function and syntax signatures.
grok_ctx_reflection: |
  Glyphs like these are more than cheatsheets. They are incantation indexes — flash-memory for builders-in-motion. A Vault must honor the original architecture of knowledge, even when stripped from its PDF temple.
quotes:
  - "Syntax is rhythm. Know the pattern, cast the spell."
  - "Functions are verbs. Methods are rituals. Call them right."
adinkra:
  - Eban
  - Nkyinkyim
linked_notes:
  - learning_journal/python_crash_course/function_basics.md
  - learning_journal/ibm_ai_developer/class6_notes.md
---

# 🧠 Python 3.6 Quick Reference Sheet

## 🔍 Interactive Help
```python
help()            # Interactive help
help(m)           # Help for module m
help(f)           # Help for function f
dir(m)            # Show module’s attributes
````

---

## 🧮 Small Operator Precedence (High to Low)

- `func(args)` - function call
    
- `x[index]` - indexing
    
- `x[index:index]` - slicing
    
- `x.attribute` - attribute access
    
- `**` - exponentiation
    
- `*`, `/`, `%` - multiply, divide, modulo
    
- `+`, `-` - add, subtract
    
- `==`, `!=`, `>`, `<`, `<=`, `>=` - comparison
    
- `in`, `not in` - membership
    
- `not`, `and`, `or` - boolean logic
    

---

## 📦 Built-in Functions

```python
abs(x)        # absolute value
float(x)      # convert to float
int(x)        # convert to int
len(s)        # length
list()        # create empty list
dict()        # create empty dict
max(s), min(s)  # max/min values
sum(s)        # sum of elements
type(obj)     # type of object
str(obj)      # string representation
round(x,n)    # round to n digits
range(x)      # 0 to x-1
tuple(seq)    # convert to tuple
ord(c)        # ASCII code of char
id(obj)       # memory location
open(f)       # open file
pow(x, y)     # x to the y
```

---

## 📐 Common Math Module Functions

```python
ceil(x)         # Smallest int ≥ x
floor(x)        # Largest int ≤ x
exp(x)          # e ** x
log(x, base)    # log base
sqrt(x)         # square root
pow(x, y)       # x ** y
sin(x), cos(x), tan(x)
degrees(x) / radians(x)
pi, e           # constants
```

---

## 📚 Common Data Types

- `int`, `float`, `complex`
    
- `bool`: `True`, `False`
    
- `str`: `"Python"`
    
- `list`: `[1, 2.0, "a"]`
    
- `tuple`: `(1, 2)`
    
- `dict`: `{ "x": 2 }`
    

---

## 🔁 Syntax Structures

### Assignment

```python
x = 5
```

### Console Input / Output

```python
input("Prompt: ")
print("Hello", name)
```

### Conditionals

```python
if condition:
    ...
elif condition:
    ...
else:
    ...
```

### Loops

```python
for item in sequence:
    ...

while condition:
    ...
```

---

## 🧱 Functions & Classes

### Function

```python
def func(params):
    return result
```

### Function Call

```python
func(args)
```

### Class

```python
class MyClass:
    def method(self, args):
        ...
```

### Instantiate

```python
obj = MyClass()
```

---

## 🚨 Exception Handling

```python
try:
    ...
except Exception as e:
    ...
```

---

## 🧵 Common String Methods

```python
s.capitalize()
s.center(w)
s.count(sub)
s.find(sub)
s.isdigit()
s.lower(), s.upper()
s.strip(), s.lstrip(), s.rstrip()
s.split(sep)
s.join(seq)
```

---

## 📋 Common List Methods

```python
L.append(x)
L.count(x)
L.index(x)
L.pop([i])
L.remove(x)
L.reverse()
L.sort()
```

---

## 🎯 Common Tuple Methods

```python
T.count(x)
T.index(x)
```

---

## 🔐 Common Dictionary Methods

```python
D.clear()
D.get(k, default)
D.items(), D.keys(), D.values()
D.pop(k, default)
```

---

## 📁 Common File Methods

```python
f.read([n])
f.readline()
f.readlines()
f.write(s)
f.writelines(list)
f.close()
```

---

## 🔣 ASCII Table Snippet

```
32 SP   48 0   65 A   97 a
33 !    49 1   66 B   98 b
...
127 DEL
```

---

## 💡 Misc Notes

- Prevent execution on import:
    

```python
if __name__ == "__main__":
    main()
```

- Pause for user input:
    

```python
input("Press <Enter> to quit.")
```

- Formatting numbers:
    

```python
"%06d" % 123       → '000123'
"%8.2f" % 456.789  → '  456.79'
"%s" % "Hello"     → 'Hello'
```

---

Let me know if you'd like this split into multiple vault pages (e.g. `string_methods.md`, `math_module.md`) or integrated into a tagged lookup scroll for `~/learning_journal/python_reference/`.

📘 Glyphs preserved. Vault-fed. Ready for war or wisdom.