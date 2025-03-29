---
Title: Science - Computer Science - Python Notes - Intermediate Python.md
Date Created: 2025-01-12
Last Updated: 2025-01-12 14:41:57
aliases:
---
#### **Title: Intermediate Python**

---

#### **Content:**

Intermediate Python concepts build on the basics and include topics like:

1. **Advanced Function Arguments**
    
    - **What are `*args` and `**kwargs`?**
    - Use `*args` to pass a variable number of positional arguments:
        
        python
        
        Copy code
        
        `def greet(*names):     for name in names:         print(f"Hello, {name}!") greet("Alice", "Bob", "Charlie")`
        
    - Use `**kwargs` to pass a variable number of keyword arguments:
        
        python
        
        Copy code
        
        `def print_info(**details):     for key, value in details.items():         print(f"{key}: {value}") print_info(name="Alice", age=30)`
        
2. **List Comprehensions**
    
    - A concise way to create or filter lists:
        
        python
        
        Copy code
        
        `squares = [x**2 for x in range(10)] evens = [x for x in range(10) if x % 2 == 0]`
        
3. **Higher-Order Functions**
    
    - Functions like `map`, `filter`, and `reduce`:
        
        python
        
        Copy code
        
        `from functools import reduce  # Using map nums = [1, 2, 3] squared = list(map(lambda x: x**2, nums))  # Using filter even_nums = list(filter(lambda x: x % 2 == 0, nums))  # Using reduce total = reduce(lambda x, y: x + y, nums)`
        
4. **Decorators**
    
    - See the note [[Python Decorators]] for details.
    - Mention why decorators are relevant in Python.

---

#### **Related Notes:**

- [[Python Decorators]]
- [[Useful Python Libraries]]