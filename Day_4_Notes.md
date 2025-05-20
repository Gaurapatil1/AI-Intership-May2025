# Day 4: Functions & Recursion – Notes

---

## 1. Functions in Python

A function is a reusable block of code that performs a specific task.

### Syntax:
```python
def function_name(parameters):
    # code block
    return value

def greet(name):
    return f"Hello, {name}"
print(greet("Gaurav"))

## 2. Parameters & Return Values

Functions can accept arguments and return values.

You can also use default parameter values.
def add(a, b=5):
    return a + b

print(add(3))  # Output: 8

## 3. Types of Arguments

Positional arguments
Keyword arguments
Default arguments
Variable-length arguments using:

*args for non-keyword variable arguments

**kwargs for keyword variable arguments


## 4. Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
A recursive function is a function that calls itself.


## 5. Fibonacci Sequence using Recursion
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    seq = fibonacci(n - 1)
    seq.append(seq[-1] + seq[-2])
    return seq

## 6. Palindrome Checker Function
def is_palindrome(text):
    return text == text[::-1]

