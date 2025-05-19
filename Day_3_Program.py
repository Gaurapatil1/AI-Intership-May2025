# Day 3: Conditional Statements & Loops

# 1. Check if number is even or odd
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2. Print numbers from 1 to 100
for i in range(1, 101):
    print(i, end=' ')

print("\n")

# 3. Sum of even numbers up to N
N = 10
sum_even = 0
for i in range(2, N+1, 2):
    sum_even += i
print("Sum of even numbers:", sum_even)

# 4. Check if a number is prime
n = 17
is_prime = True
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not Prime")

# 5. Print a triangle pattern
rows = 5
for i in range(1, rows + 1):
    print("*" * i)