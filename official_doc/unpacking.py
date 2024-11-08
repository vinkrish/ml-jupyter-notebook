# Unpacking a tuple
coordinates = (10, 20)
x, y = coordinates

print(x)  # Output: 10
print(y)  # Output: 20

# Using * for Extended Unpacking
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)   # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)    # Output: 5

# Unpacking with Function Arguments (*args and **kwargs)
def add(a, b, c):
    return a + b + c

# Using a list or tuple
numbers = [1, 2, 3]
result = add(*numbers)  # Unpacks the list as arguments
print(result)  # Output: 6

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Using a tuple with *
person_info = ("Alice", 30)
greet(*person_info)  # Equivalent to greet("Alice", 30)

# Using a dictionary with **
person_details = {"name": "Bob", "age": 25}
greet(**person_details)  # Equivalent to greet(name="Bob", age=25)

# Unpacking a Dictionary
person = {"name": "Charlie", "age": 28}
name, age = person.values()

print(name)  # Output: Charlie
print(age)   # Output: 28

# Using ** for merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}

print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Swapping Variables Using Unpacking
a = 5
b = 10

a, b = b, a

print(a)  # Output: 10
print(b)  # Output: 5

# Unpacking Nested Structures
nested = [(1, (2, 3)), (4, (5, 6))]

for a, (b, c) in nested:
    print(f"a: {a}, b: {b}, c: {c}")

# Defining Functions with *args and **kwargs
def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Calling the function
my_function(1, 2, 3, name="Bob", age=25)
