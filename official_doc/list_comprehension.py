friends = ["Angel", "Everest", "Kailani", "Moda"]
starts_a = [friend for friend in friends if friend.startswith('A')]
print(starts_a)
print(friends is starts_a)
print("friends:", id(friends), "starts_a:", id(starts_a))

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
