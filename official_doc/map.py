# map(function, iterable)

# Define a list of numbers
numbers = [1, 2, 3, 4]

# Use map to apply a lambda function that doubles each number
doubled = map(lambda x: x * 2, numbers)

# Convert the map object to a list to see the results
print(list(doubled))  # Output: [2, 4, 6, 8]

# 1. Using a Regular Function with map()
# Define a function
def square(x):
    return x * x

# Use map to apply the square function to each number
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16]

# 2. Applying map() to Multiple Iterables
# Define two lists of numbers
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

# Use map to add corresponding elements
added_numbers = map(lambda x, y: x + y, numbers1, numbers2)
print(list(added_numbers))  # Output: [5, 7, 9]

# 3. Transforming a List of Strings
words = ["apple", "banana", "cherry"]
uppercase_words = map(lambda word: word.upper(), words)
print(list(uppercase_words))  # Output: ['APPLE', 'BANANA', 'CHERRY']

# 4. Using map() with Built-In Functions
# Convert a list of strings to integers
str_numbers = ["1", "2", "3", "4"]
int_numbers = map(int, str_numbers)
print(list(int_numbers))  # Output: [1, 2, 3, 4]

# Convert the map object to a list
result = list(map(lambda x: x * 3, [1, 2, 3]))
print(result)  # Output: [3, 6, 9]

# Convert the map object to a tuple
result = tuple(map(lambda x: x * 3, [1, 2, 3]))
print(result)  # Output: (3, 6, 9)
