from itertools import chain

# A tuple consists of a number of values separated by commas
t = 12345, 54321, 'hello!'
print(t)

# destructuring
x, y, z = t
print(x, y, z)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
# t[0] = 88888
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
'''

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
([1, 2, 3], [3, 2, 1])

# Initialize a tuple
tuple1 = (1, 2, 3, 4, 5)

# 1. Access element by index
print(tuple1[0])  # Output: 1
print(tuple1[2])  # Output: 3

# 2. Slicing a tuple
print(tuple1[1:4])  # Output: (2, 3, 4)

# 3. Concatenate tuples
tuple2 = (6, 7)

# Merging tuples using +
merged_tuple = tuple1 + tuple2
print(merged_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)

# Merging tuples using unpacking
merged_tuple = (*tuple1, *tuple2)
print(merged_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)

# Merging tuples using itertools.chain
# merged_tuple = tuple(chain(tuple1, tuple2))

# 4. Repeat elements in a tuple
repeated = tuple2 * 3
print(repeated)  # Output: (6, 7, 6, 7, 6, 7)

# 5. Check if an element exists in the tuple
print(3 in tuple1)  # Output: True
print(10 in tuple1)  # Output: False

# 6. Get the length of the tuple
print(len(tuple1))  # Output: 5

# 7. Count occurrences of an element in the tuple
tuple3 = (1, 2, 2, 3, 4, 4, 4)
print(tuple3.count(4))  # Output: 3

# 8. Get the index of an element
print(tuple3.index(2))  # Output: 1 (first occurrence of 2)

# 9. Convert a list to a tuple
list1 = [10, 20, 30]
tuple_from_list = tuple(list1)
print(tuple_from_list)  # Output: (10, 20, 30)

# 10. Unpacking a tuple
a, b, c = tuple_from_list
print(a, b, c)  # Output: 10 20 30

# 11. Nesting tuples
nested_tuple = (tuple1, tuple2)
print(nested_tuple)  # Output: ((1, 2, 3, 4, 5), (6, 7))

# 12. Convert a tuple to a string (join operation for a tuple of strings)
tuple_strings = ("apple", "banana", "cherry")
joined_string = " ".join(tuple_strings)
print(joined_string)  # Output: "apple banana cherry"

# 13. Max and min values in a tuple (for numeric values)
print(max(tuple1))  # Output: 5
print(min(tuple1))  # Output: 1

# 14. Sorting a tuple (returns a sorted list, as tuples are immutable)
sorted_tuple = sorted(tuple1)
print(sorted_tuple)  # Output: [1, 2, 3, 4, 5]

tuples = [(1, 2), (0, 5), (3, 1), (1, 2, 0)]
sorted_tuples = sorted(tuples)

print(sorted_tuples)  # Output: [(0, 5), (1, 2), (1, 2, 0), (3, 1)]

# 15. Deleting a tuple (tuples are immutable, so you delete the whole tuple, not elements)
del tuple1  # tuple1 is now deleted

# Attempting to print tuple1 now would raise an error since it has been deleted
# print(tuple1) # NameError: name 'tuple1' is not defined

# Iterating Over a list of tuple
people = [("Alice", 30, "New York"), ("Bob", 25, "Los Angeles"), ("Charlie", 35, "Chicago")]

for name, age, city in people:
    print(f"Name: {name}, Age: {age}, City: {city}")


for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}")

for index, (name, age, city) in enumerate(people):
    print(f"Person {index + 1}: Name: {name}, Age: {age}, City: {city}")

# Sorting Dictionary
my_dict = {'banana': 3, 'apple': 5, 'cherry': 2}
sorted_dict = dict((key, my_dict[key]) for key in sorted(my_dict))
print(sorted_dict) # {'apple': 5, 'banana': 3, 'cherry': 2}

# Sort by value
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict) # {'cherry': 2, 'banana': 3, 'apple': 5}

# Get sorted items as a list of tuples
sorted_items = sorted(my_dict.items(), key=lambda item: item[1])
print(sorted_items) # [('cherry', 2), ('banana', 3), ('apple', 5)]