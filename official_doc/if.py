x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# Using if not to Check for Falsy Values
name = ""

if not name:
    print("The name is empty.")

# Using if not with Boolean Conditions
is_raining = False

if not is_raining:
    print("You can go outside without an umbrella.")

# Using if not with Membership Test (not in)
fruits = ["apple", "banana", "cherry"]

if "orange" not in fruits:
    print("Orange is not in the list of fruits.")

# Using if not with Functions
def is_even(number):
    return number % 2 == 0

number = 5

if not is_even(number):
    print(f"{number} is odd.")

# Using if not with None
value = None

if not value:
    print("The value is None or falsy.")
