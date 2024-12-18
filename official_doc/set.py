from itertools import chain

# Initialize a set
set1 = {"apple", "banana", "cherry"}

# 1. Add an item to a set
set1.add("orange")
print(set1)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# 2. Add multiple items to a set
set1.update(["mango", "grapes"])
print(set1)  # Output: {'apple', 'banana', 'cherry', 'orange', 'mango', 'grapes'}

# 3. Remove an item from a set (raises an error if item doesn’t exist)
set1.remove("banana")
print(set1)  # Output: {'apple', 'cherry', 'orange', 'mango', 'grapes'}

# 4. Discard an item (will not raise an error if the item doesn’t exist)
set1.discard("banana")  # No error if 'banana' isn't in the set
print(set1)  # Output remains the same if 'banana' was already removed

# 5. Clear the set (empties the set)
set1.clear()
print(set1)  # Output: set()

# 6. Delete the set completely
set1 = {"apple", "banana", "cherry"}
del set1
# print(set1)  # This would raise a NameError as set1 no longer exists

# Reinitialize sets for further examples
set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "mango", "grapes"}

# 7. Merge two sets
merged_set = set1 | set2
print(merged_set)

# Union of two sets (returns a new set with all unique elements)
set_union = set1.union(set2)
print(set_union)  # Output: {'apple', 'banana', 'cherry', 'mango', 'grapes'}

# Using unpacking operator
merged_set = {*set1, *set2}
print(merged_set) 

# Using itertools.chain
merged_set = set(chain(set1, set2))
print(merged_set)

# 8. Update set1 with elements from set2 (adds elements of set2 to set1)
set1.update(set2)
print(set1)  # Output: {'apple', 'banana', 'cherry', 'mango', 'grapes'}

# 9. Copy a set
set_copy = set1.copy()
print(set_copy)  # Output: {'apple', 'banana', 'cherry', 'mango', 'grapes'}

# Reinitialize sets for difference examples
set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "mango", "grapes"}

# 10. Difference between two sets (elements in set1 but not in set2)
set_diff = set1.difference(set2)
print(set_diff)  # Output: {'apple', 'banana'}

# 11. Difference update (removes elements in set1 that are also in set2)
set1.difference_update(set2)
print(set1)  # Output: {'apple', 'banana'}

# Reinitialize sets for intersection examples
set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "mango", "grapes"}

# 12. Intersection of two sets (common elements between sets)
set_intersection = set1.intersection(set2)
print(set_intersection)  # Output: {'cherry'}

# 13. Intersection update (keeps only elements in set1 that are also in set2)
set1.intersection_update(set2)
print(set1)  # Output: {'cherry'}

# 14. issubset (check if set1 is a subset of set2)
set1 = {"apple"}
set2 = {"apple", "banana", "cherry"}
print(set1.issubset(set2))  # Output: True

# 15. issuperset (check if set2 is a superset of set1)
print(set2.issuperset(set1))  # Output: True

# 16. Creating set from list
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set = {x for x in my_list}
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set = set(dict.fromkeys(my_list))
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set = {*my_list}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# 17. Check if value exist in a set
my_set = {1, 2, 3, 4, 5}

if 3 in my_set:
    print("3 is in the set!")  # Output: 3 is in the set!

if 6 not in my_set:
    print("6 is not in the set!")  # Output: 6 is not in the set!

# Check if 3 is in the set using __contains__()
if my_set.__contains__(3):
    print("3 is in the set!")  # Output: 3 is in the set!

values = [0, 3, 7]
# Check if any value in the list is in the set
if any(value in my_set for value in values):
    print("At least one value is in the set!")  # Output: At least one value is in the set!

values = [2, 3]
# Check if all values in the list are in the set
if all(value in my_set for value in values):
    print("All values are in the set!")  # Output: All values are in the set!