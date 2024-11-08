# lambda arguments: expression

# Simple lambda function to add 10 to a number
add_10 = lambda x: x + 10
print(add_10(5))  # Output: 15

# Lambda function to multiply two numbers
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12

# Lambda with map() Function
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8]

# Lambda with filter() Function
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# Lambda with sorted() Function and key Parameter
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
# Sort by age (second item in tuple)
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)  # Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

# Lambda within reduce()
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

# Lambda for Conditional Expressions
# Lambda function that returns "Even" or "Odd"
check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even_odd(5))  # Output: Odd
print(check_even_odd(10)) # Output: Even

# Lambda in Dictionary
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y
}

print(operations["add"](10, 5))       # Output: 15
print(operations["subtract"](10, 5))  # Output: 5
print(operations["multiply"](10, 5))  # Output: 50
