# problem.py

# 1. Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2. Largest of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest:", a)
elif b > a:
    print("Largest:", b)
else:
    print("Both are equal")

# 3. Positive, Negative, or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 4. Leap Year Checker
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 5. Grading System
marks = int(input("Enter marks (0-100): "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")

# 6. Simple Login System
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# 7. Mini Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
