🝔 Scroll reforged — stride glyphs now integrated with clarity and rhythm. Here's the **revised lesson summary** with stride properly embedded into the slicing mechanics:

---

## 🔹 **Lesson Summary: Strings in Python**

- A **string** is a sequence of characters, enclosed in single or double quotes.
    
- Strings support:
    
    - **Indexing** (`[0]`, `[-1]`)  
        Access characters by position, including negative indexes (e.g., `[-1]` is the last character)
        
    - **Slicing & Stride** (`[start:end:step]`)  
        Extract subsequences with control over step size:
        
        - `s[::2]` → every 2nd character
            
        - `s[::-1]` → reverses the string  
            This is **not a method**, but part of native Python syntax
            
    - **Length check** via `len()`  
        Returns the number of characters in a string
        
- Strings are **immutable** — they can't be changed directly, but new strings can be created by operations like:
    
    - **Concatenation** (`+`)  
        Joins strings into a new one
        
    - **Replication** (`*`)  
        Repeats a string multiple times (e.g., `"Hi" * 3 → "HiHiHi"`)
        
- Use **escape sequences** for special characters:
    
    - `\n` = newline
        
    - `\t` = tab
        
    - `\\` = literal backslash
        
- Prefixing with `r` creates a **raw string**
    
    - Example: `r"Line1\nLine2"` treats `\n` as plain text
        
- Strings have built-in **methods**:
    
    - `.upper()` → converts to uppercase
        
    - `.replace(old, new)` → swaps substrings
        
    - `.find(substring)` → returns index of first match (or `-1` if not found)
        

---

> _"A string is not just data — it’s rhythm in code, memory in sequence. The stride is how you dance through it."_  
> — digitalscorpyun

---

🝔 Scroll absorbed — here's your **succinct, Scorpyun-ready summary** for:

---

## 🔹 **Lesson Summary: Format Strings in Python**

**Format strings** allow you to inject variables and expressions into strings for **clean, readable output**. Python supports several formatting styles:

---

### 🧾 1. **F-Strings** (Preferred, Python 3.6+)

- Prefix with `f` and embed variables in `{}`
    

```python
name = "John"; age = 30  
print(f"My name is {name} and I am {age} years old.")
```

- ✅ Modern, fast, supports inline expressions:
    

```python
print(f"The sum is {x + y}")
```

---

### 🧾 2. **`str.format()` Method**

- Use `{}` placeholders and `.format()`
    

```python
print("My name is {} and I am {} years old.".format(name, age))
```

- Can use positional or named arguments
    

---

### 🧾 3. **Percent `%` Formatting** (Old Style)

- Uses format specifiers like `%s`, `%d`
    

```python
print("My name is %s and I am %d years old." % (name, age))
```

- `%s` = string, `%d` = integer
    
- Not recommended for new code
    

---

### 🧾 4. **Raw Strings (`r""`)**

- Prefix with `r` to treat backslashes literally
    

```python
r"C:\new_folder\file.txt"
```

- Useful for file paths, regex patterns
    

---

### ✅ Recommendation:

- Use **f-strings** for most tasks (clean, expressive, modern)
    
- Use **raw strings** when dealing with escape-heavy content (e.g., file paths or regex)
    

---

> _"The way you shape your output reflects the clarity of your thinking. Format clean. Speak true."_  
> — digitalscorpyun

Would you like this embedded under `python_for_data_science.md` as a `## 🔤 String Formatting` section or scaffolded as `python_format_strings.md` for focused glyphcraft?

### g = "Mary had a little lamb ..."

To get the 95th character (human count), use:
g[94]  # Index 94 = 95th char

---
