# Initialize an empty dictionary
dict = {}

# 1. Add one new key-value pair
dict['key'] = 'value'
print(dict)  # Output: {'key': 'value'}

# 2. Get value of the key
print(dict['key'])  # Output: 'value'

# 3. Update key-value pair
dict['key'] = 'updated-value'
print(dict)  # Output: {'key': 'updated-value'}

# 4. Remove the key
del dict['key']
print(dict)  # Output: {}

# Re-initialize with multiple entries for further operations
dict = {'key1': 'val1', 'key2': 'val2'}

# 5. Adds dictionary key-value pairs to dict
dict.update({'key3': 'val3', 'key4': 'val4'})
print(dict)  # Output: {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}

# 6. Get value of key (returns None if key not present)
print(dict.get('key1'))  # Output: 'val1'
print(dict.get('key5'))  # Output: None

# 7. Default value for a key (if key doesn't exist)
print(dict.get('key5', 0))  # Output: 0

# 8. Pop method removes a key and returns the value
value = dict.pop('key1')
print(value)  # Output: 'val1'
print(dict)   # Output: {'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}

# 9. Returns the keys of the dictionary as a list
keys = list(dict.keys())
print(keys)  # Output: ['key2', 'key3', 'key4']

# 10. Returns the values in the dictionary as a list
values = list(dict.values())
print(values)  # Output: ['val2', 'val3', 'val4']

# 11. Returns a list of tuples where each tuple is of the form (key, value)
items = list(dict.items())
print(items)  # Output: [('key2', 'val2'), ('key3', 'val3'), ('key4', 'val4')]

# 12. Removes all elements of dictionary dict
dict.clear()
print(dict)  # Output: {}

# Re-initialize for copy example
dict = {'key1': 'val1', 'key2': 'val2'}

# 13. Returns a shallow copy of dictionary dict
dict_copy = dict.copy()
print(dict_copy)  # Output: {'key1': 'val1', 'key2': 'val2'}

# 14. Check if dictionary has a specific key (has_key is deprecated in Python 3; use 'in' instead)
print('key1' in dict)  # Output: True
print('key3' in dict)  # Output: False

# 15. Produces a printable string representation of a dictionary
print(str(dict))  # Output: "{'key1': 'val1', 'key2': 'val2'}"

# 16. Number of items in the dictionary
print(len(dict))  # Output: 2

# List of Dictionaries
employees = [
    {"name": "Alice", "age": 30, "department": "HR"},
    {"name": "Bob", "age": 24, "department": "IT"},
    {"name": "Charlie", "age": 29, "department": "Finance"}
]
for employee in employees:
    print(employee)

for employee in employees:
    print(f"Name: {employee['name']}, Department: {employee['department']}")

for employee in employees:
    for key, value in employee.items():
        print(f"{key}: {value}")
    print("---")  # Separator for each employee

for index, employee in enumerate(employees):
    print(f"Employee {index + 1}: {employee['name']}, Age: {employee['age']}")

# Using List Comprehension to Create a New List from the Dictionaries
names = [employee["name"] for employee in employees]
print(names)
