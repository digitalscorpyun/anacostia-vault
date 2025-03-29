---
Title: Science - Computer Science - Python Notes - Lists.md
Date Created: 2025-01-18
Last Updated: 2025-01-18 21:37:33
aliases:
---
#Python #programming 

### **Python Lists**

A **list** in Python is a built-in data structure used to store multiple items in a single variable. It is **ordered**, **mutable** (modifiable), and allows **duplicate elements**.

---

### **Key Features**

1. **Ordered**: Elements maintain their insertion order.
2. **Mutable**: You can change elements after the list is created.
3. **Heterogeneous**: A list can store different data types, e.g., integers, strings, floats, or even other lists.
4. **Indexing**: Elements can be accessed using their position (index starts at 0).

---

### **Creating a List**

```python
# Empty list
my_list = []

# List with elements
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["text", 42, 3.14, True]
```

---

### **Accessing Elements**

- **By Index**:
    
    ```python
    print(fruits[0])  # Output: apple
    print(numbers[-1])  # Output: 5 (negative indexing starts from the end)
    ```
    
- **Slicing**:
    
    ```python
    print(fruits[1:3])  # Output: ['banana', 'cherry']
    print(numbers[:3])  # Output: [1, 2, 3]
    ```
    

---

### **Modifying Lists**

1. **Change Elements**:
    
    ```python
    fruits[1] = "blueberry"
    print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
    ```
    
2. **Add Elements**:
    
    - **Append** (add to the end):
        
        ```python
        fruits.append("orange")
        ```
        
    - **Insert** (add at a specific index):
        
        ```python
        fruits.insert(1, "mango")
        ```
        
3. **Remove Elements**:
    
    - **Remove by value**:
        
        ```python
        fruits.remove("apple")
        ```
        
    - **Pop by index**:
        
        ```python
        fruits.pop(1)  # Removes the element at index 1
        ```
        
    - **Clear the list**:
        
        ```python
        fruits.clear()
        ```
        

---

### **Useful List Methods**

```python
# Length of a list
print(len(fruits))

# Count occurrences of an element
print(fruits.count("banana"))

# Extend a list
fruits.extend(["grape", "melon"])

# Reverse the list
fruits.reverse()

# Sort the list
numbers.sort()  # Ascending
numbers.sort(reverse=True)  # Descending
```

---

### **Iteration**

```python
# Using a for loop
for fruit in fruits:
    print(fruit)

# Using list comprehension
squared = [x**2 for x in numbers if x > 2]
print(squared)
```

---

### **Nested Lists**

Lists can contain other lists.

```python
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[0])  # Output: [1, 2]
print(nested_list[0][1])  # Output: 2
```

---

### **Common Use Cases**

- Storing a sequence of elements.
- Using as a stack or queue.
- Building multi-dimensional data structures (e.g., matrices).

---

Would you like examples of advanced list operations, such as filtering or mapping?