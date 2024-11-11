from itertools import chain
from collections import ChainMap

#extend
list1 = [1,2,3]
list2 = [4,5,6]

#append
list2.append(7)
print(list2)

#insert
list1.insert(0, 0)
print(list1)

#extend
list1.extend(list2)
print(list1)

list2 += list1
print(list2)

#concatenation
list3 = list1+list2
print(list3)

# search for element existance
exist = 0 in list1
print(exist)

#index
index = list1.index(0)
print(index)

#remove
list2.remove(7)
list2.remove(7)
print(list2)
print(list3)

#sort
list3.sort()
print(list3)

#count
count = list3.count(7)
print(count)

#pop
list3.pop()
print(list3)

list3.pop(0)
print(list3)

#length
length = len(list3)
print(length)

#lists
squares = [1, 4, 9, 16, 25]
print(squares)

#index
print(squares[0])

#slicing
print(squares[-3:])

#concat
print(squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]
print(cubes)
print(4**3)

#mutable
cubes[3] = 64
print(cubes)

#append
cubes.append(216)
#insert is same as append here
cubes.insert(len(cubes), 216)
cubes.append(7 ** 3)
print(cubes)

#Assignment to slices
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C', 'D', 'E']
print(letters)

#remove
letters[2:5] = []
print(letters)

#empty list
letters[:] = []
print(letters)

# Check if value exist in a list
my_list = [1, 2, 3, 4, 5]

if 3 in my_list:
    print("3 is in the list!")  # Output: 3 is in the list!

if 6 not in my_list:
    print("6 is not in the list!")  # Output: 6 is not in the list!

# Check if 3 is in the list using __contains__()
if my_list.__contains__(3):
    print("3 is in the list!")  # Output: 3 is in the list!

values = [0, 3, 7]
# Check if any value in the list is in my_list
if any(value in my_list for value in values):
    print("At least one value is in the list!")  # Output: At least one value is in the list!

values = [2, 3]
# Check if all values in the list are in my_list
if all(value in my_list for value in values):
    print("All values are in the list!")  # Output: All values are in the list!

# Using set for Faster Lookup
my_set = set(my_list)
# Check if 3 is in the set (faster lookup)
if 3 in my_set:
    print("3 is in the list!")  # Output: 3 is in the list!

#nest list
a = ['a', 'b', 'c']
n = [1, 2 ,3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

# inserting list elements at some index of another list
list1 = [1, 2, 3, 7, 8]
list2 = ['a', 'b', 'c']
index = 3

# Create a new list using itertools.chain
result = list(chain(list1[:index], list2, list1[index:]))
print(result)  # Output: [1, 2, 3, 'a', 'b', 'c', 7, 8]

# Merge using dict() with zip()
keys = ['a', 'b', 'c']
values = [1, 2, 3]

merged_dict = dict(zip(keys, values))
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Merge using collections.ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = dict(ChainMap(dict2, dict1))
print(merged_dict)  # Output: {'b': 3, 'c': 4, 'a': 1}
