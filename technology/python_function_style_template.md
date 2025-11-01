Here’s a **Function Style Template** you can drop into _any_ Python project to keep your functions clean, readable, and PEP 8-compliant.

---

## **📜 Python Function Style Template**

```python
# --------------------------------------
# Module: example_module.py
# Author: Your Name
# Description: Brief one-liner about what this file does.
# --------------------------------------

# 1. IMPORTS (always at the top)
import math
import sys

# 2. CONSTANTS (optional)
PI = 3.14159

# 3. FUNCTION DEFINITIONS
def example_function(param1, param2='default'):
    """
    Brief one-line summary of what the function does.

    Args:
        param1 (type): Short description of param1.
        param2 (type, optional): Short description of param2.
            Defaults to 'default'.

    Returns:
        type: Description of what the function returns.
    """
    # Function body starts here
    result = f"Processed {param1} with {param2}"
    return result


def calculate_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return PI * radius ** 2


# 4. MAIN EXECUTION (optional)
if __name__ == "__main__":
    # Example usage
    print(example_function("pizza", "extra cheese"))
    print(f"Area: {calculate_area(5):.2f}")
```

---

## **🔑 Key Rules Embedded Here**

- **Imports at the top** (Section 1).
    
- **Constants in ALL_CAPS** right after imports (Section 2).
    
- **Two blank lines between functions**.
    
- **Docstrings in triple quotes** with:
    
    - One-line summary.
        
    - `Args:` section for parameters.
        
    - `Returns:` section for the output.
        
- **No spaces around `=`** in default parameters.
    
- **Main execution block** (`if __name__ == "__main__":`) lets the file run standalone _or_ be imported as a module without running example code.
    

---
