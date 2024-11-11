from itertools import chain
from functools import reduce
import operator

# if condition
friends = ["Angel", "Everest", "Kailani", "Moda"]
starts_a = [friend for friend in friends if friend.startswith('A')]
print(starts_a)
print(friends is starts_a)
print("friends:", id(friends), "starts_a:", id(starts_a))

# if-else condition
numbers = [1, 2, 3, 4, 5]
result = [num * 2 if num % 2 == 0 else num for num in numbers]
print(result)  # Output: [1, 4, 3, 8, 5]

# list of list 

# Flatten the list using list comprehension
list_of_lists = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in list_of_lists for item in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]

# Flatten the list using itertools.chain
flattened_list = list(chain(*list_of_lists))
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]

# Flatten the list using reduce
flattened_list = reduce(operator.concat, list_of_lists)
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]

value = [[row[i] for row in matrix] for i in range(4)]
print(value)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

# transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print(transposed)

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

# Creating a Dictionary from a List of Tuples
pairs = [("apple", 3), ("banana", 2), ("orange", 5)]
dictionary = dict([(key, value) for key, value in pairs])
print(dictionary)

# Using dictionary comprehension
dictionary = {key: value for key, value in pairs}
print(dictionary)
