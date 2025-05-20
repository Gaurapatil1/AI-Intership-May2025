#  Day 4: Functions & Recursion 

# 1. Simple function with parameters
def greet(name):
    return f"Hello, {name}!"

print(greet("Gaurav"))

# 2. Max of three numbers
def find_max(a, b, c):
    return max(a, b, c)

print("Max value:", find_max(10, 25, 7))

# 3. Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# 4. Fibonacci using recursion
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

print("Fibonacci sequence (7 terms):", fibonacci(7))

# 5. Palindrome checker
def is_palindrome(text):
    return text == text[::-1]

print("Is 'madam' a palindrome?", is_palindrome("madam"))
print("Is 'python' a palindrome?", is_palindrome("python"))