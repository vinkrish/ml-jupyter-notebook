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

#nest list
a = ['a', 'b', 'c']
n = [1, 2 ,3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])