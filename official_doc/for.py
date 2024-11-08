words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

#modify sequence
for w in words[:]:
    if len(w) > 5:
        words.insert(0, w)
print(words)

# 3. Looping with Start, Stop, and Step in range()
for i in range(1, 10, 2):
    print(i)
# Output:
# 1
# 3
# 5
# 7
# 9

# 4. Iterating Over a String
text = "hello"
for char in text:
    print(char)

# 5. Iterating Over a Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 25
# city: New York

for p in person:
    print(f"{p}: {person[p]}")

# 6. Using enumerate() to Get Index and Value
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"Index {index}: {name}")
# Output:
# Index 0: Alice
# Index 1: Bob
# Index 2: Charlie

# 7. Using zip() to Loop Over Multiple Iterables
names = ["Alice", "Bob", "Charlie", "Random"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
# Output:
# Alice is 25 years old.
# Bob is 30 years old.
# Charlie is 35 years old.

# 8. for Loop with break
for i in range(10):
    if i == 5:
        break
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# 9. for Loop with continue
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output:
# 0
# 1
# 3
# 4

# 10. for Loop with else - The else block runs when the loop completes normally
for i in range(5):
    print(i)
else:
    print("Loop completed without a break.")
# Output:
# 0
# 1
# 2
# 3
# 4
# Loop completed without a break.

# 11. Nested for Loop
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
# Output:
# 1 2 3
# 4 5 6
# 7 8 9

# 12. List Comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)
# Output: [1, 4, 9, 16, 25]

# 13. Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num**2 for num in numbers}
print(squared_dict)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 14. for Loop for Flattening a List of Lists
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [item for sublist in list_of_lists for item in sublist]
print(flattened)
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

# filter with list comprehension
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
passed = [name for name, score in scores.items() if score>=65]
print(passed)