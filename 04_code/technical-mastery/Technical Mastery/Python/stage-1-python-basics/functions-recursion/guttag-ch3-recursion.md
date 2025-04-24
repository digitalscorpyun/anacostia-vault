# Guttag - Chapter 3 (Recursion)  

## Key Concept  
- **Recursive Functions**: Functions that call themselves.  

## Code Example  
```python  
def factorial(n):  
    if n == 1:  
        return 1  
    else:  
        return n * factorial(n-1) 
