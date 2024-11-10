import math
import random

# 1. Basic Arithmetic Operations
a = 10
b = 3

# Basic operations
print(a + b)   # Output: 13 (Addition)
print(a - b)   # Output: 7 (Subtraction)
print(a * b)   # Output: 30 (Multiplication)
print(a / b)   # Output: 3.3333333333333335 (Division)
print(a // b)  # Output: 3 (Floor Division)
print(a % b)   # Output: 1 (Modulus)
print(a ** b)  # Output: 1000 (Exponentiation)

# 2. Using the math Module
x = 25

# Square root
print(math.sqrt(x))  # Output: 5.0

# Rounding up and down
print(math.ceil(4.3))  # Output: 5
print(math.floor(4.7)) # Output: 4

# Trigonometric functions
print(math.sin(math.pi / 2))  # Output: 1.0
print(math.cos(math.pi))      # Output: -1.0

# Logarithmic functions
print(math.log(100, 10))      # Output: 2.0

# 3. Random Number Manipulation

# Generate a random integer between 1 and 10
random_int = random.randint(1, 10)
print(random_int)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print(random_float)

# Round a random number
rounded_number = round(random_float * 100, 2)
print(rounded_number)  # Output: A number rounded to 2 decimal places

# 4. Number Formatting
num = 1234.56789

# Round to 2 decimal places
print(round(num, 2))  # Output: 1234.57

# Format as a string with commas
print(f"{num:,.2f}")  # Output: 1,234.57

# Display as a percentage
percentage = 0.12345
print(f"{percentage:.2%}")  # Output: 12.35%

# 5. Type Conversion
x = 10
y = "20.5"

# Convert integer to float
x_float = float(x)
print(x_float)  # Output: 10.0

# Convert string to float
y_float = float(y)
print(y_float)  # Output: 20.5

# Convert float to integer (truncation)
print(int(y_float))  # Output: 20

# Convert number to string
print(str(x))  # Output: '10'

# 6. Using divmod() Function
a = 17
b = 4

quotient, remainder = divmod(a, b)
print(f"Quotient: {quotient}, Remainder: {remainder}")
# Output: Quotient: 4, Remainder: 1

# 7. Manipulating Digits of a Number
num = 12345

# Extract digits as a list
digits = [int(digit) for digit in str(num)]
print(digits)  # Output: [1, 2, 3, 4, 5]

# Reverse the number
reversed_num = int(str(num)[::-1])
print(reversed_num)  # Output: 54321
