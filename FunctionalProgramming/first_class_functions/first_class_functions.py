# Composition
def f(x):
    return x * 2

def g(h, x):
    return h(x) * 2

print(g(f, 4))

# Closure : It occurs when a function has access to a local variable from an enclosing scope that has finished its execution.
def add(x):
    def _(y):
        return x + y
    return _

add2 = add(2)
add3 = add(3)

print(add2(2), add3(3))

# Currying : It is the practice of simplifying the execution of a function that takes multiple arguments into executing sequential single-argument functions.
def f1(x, y):
    return x * y

def f2(x):
    def _(y):
        return f1(x, y)
    return _

print(f2(2))
print(f2(2)(3))


# Currying - Many to Single Argument 
def change(a):
    def w(b):
        def x(c):
            def y(d):
                def z(e):
                    print(a, b, c, d, e)
                return z
            return y
        return x
    return w
   
change(10)(20)(30)(40)(50)
temp_change = change(10)(20)(30)(40)
temp_change(50)