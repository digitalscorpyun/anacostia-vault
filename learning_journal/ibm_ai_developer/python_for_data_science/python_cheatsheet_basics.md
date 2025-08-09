---
id: "20250720050100"
title: python_cheat_sheet_basics_ibm.md
category: learning_journal
style: CodeRitual
path: learning_journal/ibm_ai_developer/python_cheat_sheet_basics_ibm.md
created: 2025-07-20T05:01:00-07:00
updated: 2025-07-20T05:01:00-07:00
status: active
priority: medium
summary: |
  This cheat sheet summarizes foundational Python syntax for data science and web development, including types, collections, loops, conditionals, functions, file I/O, web scraping, and error handling. It reflects IBM's instructional content for Coursera's "Python for Data Science, AI & Development" course.
longform_summary: |
  Extracted from IBM’s Coursera course, this reference guide includes core Python syntax, operator behavior, common method calls for built-in types, and key libraries like `requests` and `BeautifulSoup`. It is designed as a rapid recall sheet for learners mastering Python for applied data work. This version includes slight rewording and formatting adjustments for Vault integration.
tags:
  - python
  - cheat_sheet
  - ibm_course
  - data_science
  - code_reference
  - coursera
  - web_scraping
  - file_handling
cssclasses:
  - code-scroll
  - basics
synapses:
  - Python types, loops, and functions
  - Requests, BeautifulSoup, error types
key_themes:
  - syntax mastery
  - applied programming
  - developer readiness
bias_analysis: |
  Content assumes a linear, technical learning model. It excludes cultural perspectives or alternative epistemologies in programming education.
grok_ctx_reflection: |
  This scroll serves as a rapid onboarding interface for Python tool use within the Anacostia Vault’s learning matrix. It functions as a glyph mirror for agent ritual calibration and baseline syntax fluency.
quotes:
  - "Learn Python for Data Science, AI & Development – IBM"
adinkra: Eban
linked_notes:
  - python_programming_fundamentals_glossary
  - python_programming_fundamentals_cheatsheet
  - ibm_course_index
---

# Python Cheat Sheet: The Basics (IBM / Coursera)

## Data Types

```python
# String
my_string = "Hello"
my_string.upper()
len(my_string)
my_string.find('l')
my_string.replace('H', 'C')

# Integer
my_integer = 12321

# Float
my_decimal = 3.14

# Boolean
a = True
b = False

# Dictionary
my_dictionary = {'banana': 1, 12: 'laptop', (0,0): 'center'}
my_dictionary['banana']
my_dictionary.keys()
my_dictionary.values()

# Tuple
tup = (1, 3.12, False, "Hi")

# List
my_collection = [1, 1, 3.12, False, "Hi"]
len(my_collection)
my_collection.extend(["More", "Items"])
my_collection.append("Single")
del(my_collection[2])
clone = my_collection[:]
my_collection_2 = ["a", "b", "c"]
my_collection_3 = my_collection + my_collection_2
number_collection = [1, 2, 3, 4.5]
sum(number_collection)
item in my_collection
item not in my_collection

# Set
a = {100, 3.12, False, "Bye"}
b = {100, 3.12, "Welcome"}
my_set = set([1,1,2,3])
a.add(4)
a.remove("Bye")
a.difference(b)
a.intersection(b)
a.union(b)
a.issubset(b)
a.issuperset(b)
````

## Indexing & Slicing

```python
my_string[element_number]
my_collection[element_number]
my_tup[element_number]

my_string[start:stop]
my_collection[start:stop]
my_tup[start:stop]
```

## Comparison & Conditional Operators

```python
a == b  # Equal
a != b  # Not equal
a < b   # Less than
a > b   # Greater than
a <= b  # Less than or equal
a >= b  # Greater than or equal

# Logical
a and b
a or b
not a
```

## Loops

```python
# For Loop
for x in range(5):
    # do something

for x in iterable:
    # iterate object

# While Loop
while condition:
    # repeat
```

## Conditional Statements

```python
if condition:
    # execute
elif other_condition:
    # execute alternative
else:
    # fallback
```

## Try / Except

```python
try:
    # risky code
except ValueError:
    # handle ValueError
except:
    # handle any exception
else:
    # if no error
```

## Error Types

- `IndexError`: index out of range
    
- `NameError`: variable not found
    
- `SyntaxError`: code syntax invalid
    
- `ZeroDivisionError`: divide by zero
    

## Range

```python
range(stop)
range(start, stop, step)
```

## Web Scraping (BeautifulSoup + Requests)

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html5lib')
soup.prettify()
soup.find(tag)
soup.find_all(tag)

import requests
response = requests.get(url, parameters)
response.url
response.status_code
response.request.headers
response.request.body
response.headers
response.text
response.json()
requests.post(url, parameters)
```

## Functions

```python
def function_name(param1, param2):
    return something

output = function_name(1, 2)
```

## File Handling

```python
# Reading
file = open("file.txt", "r")
file.name
file.mode
file.read()
file.read(10)
file.readline()
file.readlines()
file.close()

# Writing
file = open("file.txt", "w")
file.write("Hello")
file.append("More")

# Note: append() should be open("file.txt", "a") + write()
```

## Classes & Objects

```python
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def my_method(self, x):
        return x + self.a

obj = MyClass(1, 2)
obj.my_method(5)
```

---

**Source:** [IBM Coursera - Python for Applied Data Science AI](https://www.coursera.org/learn/python-for-applied-data-science-ai)  
**Copyright:** © IBM Corporation 2021

```

---

Would you like this scroll added to a git commit summary or linked to a `python_cheat_index.md` if you're building an index of reference scrolls?
```