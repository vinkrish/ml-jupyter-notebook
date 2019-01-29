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

#pop
print(letters.pop())

#remove
letters[2:5] = []
print(letters)

#empty list
letters[:] = []
print(letters)

#nest list
a = ['a', 'b', 'c']
n = [1, 2 ,3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])
