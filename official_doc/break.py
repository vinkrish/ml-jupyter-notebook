#loop can have else, executed when loop terminates
#but not when the loop is terminated by a break statement
for n in range(2, 10):
    print('current number:', n)
    for x in range(2, n):
        print('x value = ', x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

