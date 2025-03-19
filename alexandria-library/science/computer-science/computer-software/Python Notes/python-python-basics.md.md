---
tags: Python
category: Python Notes
---
# 🏛 **Python - Python Basics**

> _“Programs must be written for people to read, and only incidentally for machines to execute.”_ — Harold Abelson

---

## 📌 **Overview**

**Python** is a high-level, interpreted programming language known for its **simplicity, readability, and versatility**. It is widely used in **web development, data science, automation, AI, and cybersecurity**. Python emphasizes **clean syntax and efficient programming**, making it a favorite for beginners and professionals alike.

This note covers the **fundamentals of Python**, including syntax, variables, control flow, functions, and error handling.

---

## 🏷️ **Key Details**

- **Language Type:** Interpreted, High-Level
- **Paradigm:** Multi-paradigm (Procedural, Object-Oriented, Functional)
- **Creator:** Guido van Rossum (1991)
- **Current Version:** `python --version` (Check Installed Version)
- **Installation:** [Download Python](https://www.python.org/downloads/)

🗂 **Related Notes:**

- [[Python - Data Types & Variables]] 🔢
- [[Python - Control Flow (Loops & Conditionals)]] 🔄
- [[Python - Functions & Scope]] 🔧

---

## 📜 **Getting Started with Python**

### **1️⃣ Installing & Running Python**

```bash
# Install Python (Windows/macOS/Linux)
pip install python

# Check Python version
python --version

# Run Python in interactive mode
python
```

### **2️⃣ Writing & Running Python Scripts**

```python
# Example: hello.py
print("Hello, Python!")
```

Run the script:

```bash
python hello.py
```

✅ **Python scripts can be executed via the terminal or an IDE (VS Code, PyCharm, Jupyter Notebook).**

---

## 🔤 **Basic Syntax & Structure**

### **3️⃣ Variables & Data Types**

```python
# Numbers
x = 10  # Integer
y = 3.14  # Float

# Strings
name = "Python"

# Boolean
is_active = True

# Lists
fruits = ["Apple", "Banana", "Cherry"]

# Dictionaries (Key-Value Pairs)
person = {"name": "Alice", "age": 25}
```

✅ **Python is dynamically typed – no need to declare variable types explicitly.**

---

### **4️⃣ Control Flow (If-Else & Loops)**

```python
# If-Else
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")

# For Loop
for i in range(5):
    print(i)

# While Loop
x = 0
while x < 3:
    print(x)
    x += 1
```

✅ **Loops and conditionals help automate repetitive tasks.**

---

### **5️⃣ Functions & Scope**

```python
# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))
```

✅ **Functions promote code reuse and modularity.**

---

### **6️⃣ Lists & Tuples**

```python
# Lists (Mutable)
numbers = [1, 2, 3, 4]
numbers.append(5)  # Add an element

# Tuples (Immutable)
coordinates = (10, 20)
```

✅ **Use lists when data needs to change, and tuples when it should remain constant.**

---

### **7️⃣ Dictionaries & Sets**

```python
# Dictionary (Key-Value Pairs)
user = {"name": "Alice", "age": 25}
print(user["name"])  # Access value

# Set (Unique Values)
colors = {"red", "blue", "green"}
colors.add("yellow")
```

✅ **Dictionaries store key-value pairs, while sets store unique elements.**

---

### **8️⃣ List Comprehensions (Pythonic Way)**

```python
# Create a list of squares
squares = [x ** 2 for x in range(5)]
```

✅ **List comprehensions are more efficient than loops.**

---

### **9️⃣ Exception Handling**

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
finally:
    print("Execution complete.")
```

✅ **Always handle exceptions to avoid program crashes.**

---

## ⚡ **Python Performance Optimization**

### **🔹 Using Generators Instead of Lists**

```python
# Generator (Efficient Memory Usage)
def squares_gen(n):
    for i in range(n):
        yield i ** 2

gen = squares_gen(5)
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
```

✅ **Generators improve memory efficiency by lazily evaluating elements.**

---

## 🌟 **Real-World Applications of Python**

📌 **Use Cases:**  
✔ **Web Development** – Flask, Django.  
✔ **Data Science & AI** – Pandas, NumPy, TensorFlow.  
✔ **Cybersecurity** – Ethical hacking, malware analysis.  
✔ **Automation & Scripting** – Web scraping, task scheduling.  
✔ **Game Development** – Pygame, Unity scripting.

🔗 **Related Notes:**

- [[Python - Web Development with Flask]] 🌐
- [[Python - Data Science with Pandas]] 📊
- [[Python - Automation & Scripting]] ⚙️

---

## 📚 **Key Readings & Resources**

📖 **Books:**

- _Python Crash Course_ – Eric Matthes
- _Automate the Boring Stuff with Python_ – Al Sweigart
- _Fluent Python_ – Luciano Ramalho

🌍 **Online Resources:**

- [Python Official Docs](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)

---

## 🔗 **Connections in My Zettelkasten**

🔗 [[Python - Data Types & Variables]]  
🔗 [[Python - Control Flow (Loops & Conditionals)]]  
🔗 [[Python - Functions & Scope]]  
🔗 [[Python - Web Development with Flask]]  
🔗 [[00_Index.md]] | [[africana-studies-overview]]

---

**🔖 Tags:**  
#Python #PythonBasics #Programming #SoftwareDevelopment #Automation #DataScience

🚀 **Now Obsidian-ready!** Copy, paste, and integrate this into your **Python vault**. Let me know if you need refinements! 🔥