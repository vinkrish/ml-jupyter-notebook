for i in range(5):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

#range is iterable
print(range(10))

#range suitable as a target for functions
# and constructs that expect something
# from which they can obtain successive items until the supply is exhausted 
print(list(range(5)))
