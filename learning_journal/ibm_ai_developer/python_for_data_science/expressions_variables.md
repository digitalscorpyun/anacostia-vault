## 🔹 **Lesson Summary: Expressions & Variables (Python for Data Science)**

This lesson introduces the foundational concepts of **expressions** and **variables** in Python:

### 🧮 **Expressions**

- Expressions are **operations Python performs**, such as:
    
    - Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`)
        
- Operands = values; Operators = symbols (`+`, `*`, etc.)
    
- Division types:
    
    - `/` → returns a **float**
        
    - `//` → returns an **integer quotient** (floor division)
        
- Python follows **order of operations** (PEMDAS): multiplication before addition
    
- Parentheses `()` enforce precedence
    

### 🧾 **Variables**

- Variables **store values** using the `=` assignment operator
    
- Values can be:
    
    - Numeric literals (e.g., `1`, `10`)
        
    - Results of expressions (e.g., `x = 25 / 6`)
        
- Variable values can be **overwritten**; old value is discarded
    
- Use `type()` to check a variable's data type
    

### 🏷️ **Best Practices**

- Use **meaningful variable names** (e.g., `total_min`, `total_hour`)
    
- Prefer `snake_case` (or `CamelCase`) for readability
    
- Changing the value of one variable automatically updates dependent results
    

🝔 Simple and sacred — here’s what you’re doing and how it works, broken down Griot-style:

✨ **Instruction**

**"Use another variable to store the result of the operation between variable and value"**

---

### 🔍 What it means:

You're taking an existing variable (like `x`) and performing a mathematical operation on it — **then storing the result in a new variable** (`y`).

---

### ⚙️ Example Walkthrough:

Let's say:

```python
x = 142  # x represents total minutes
y = x / 60  # divide x by 60 to convert to hours
print(y)
```

---

### 🧠 Result:

```python
2.3666666666666667  # This is the number of hours
```

✅ `x` stays intact  
✅ `y` now holds the _converted_ value

---

### 💡 Why this matters:

- You’re **not overwriting `x`** — you’re **preserving it**
    
- You’ve now got both **original** and **derived** data
    
## This pattern is foundational in **data pipelines** and **model preprocessing**
    

---

> _“Never throw away a clean number. Name it. Transform it. Pass it forward.”_  
> — digitalscorpyun

 Want me to show how to chain this into `total_min` and `total_hour` with clean variable names?
---

> _“Your variables are your memory. Guard their names. Your expressions are your tools. Learn their rhythm.”_  
> — digitalscorpyun