a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

[1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a)

[1, 66.25, 1234.5]
del a[:]
print(a)

a = []
del a

# dictionary
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
print(basket_items['apples'])

print(list(basket_items.items())
# [('apples', 4), ('oranges', 19), ('kites', 3), ('sandwiches', 8)]

for key in basket_items:
    print(basket_items[key])

for custom_name in basket_items.values():
    print(custom_name)

for key, value in basket_items.items():
    print(key, value)

fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
for fruit, fruit_count in basket_items.items():
    if fruit in fruits:
        result += fruit_count
print(result)

# tuple
tuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

if "apple" in tuple:
    print("Yes, 'apple' is in the fruits tuple")
    
# set
set = {"apple", "banana", "cherry"} or thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
for x in thisset:
  print(x)
  
print("banana" in thisset)

set.add("orange")

# loop
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]
news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break
print(news_ticker)

# zip
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points = []
for label, x, y, z in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(label, x, y, z))
for point in points:
    print(point)

# zip list to dictionary
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
cast = dict(zip(cast_names, cast_heights))
print(cast)

# unzip
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
names, heights = zip(*cast)
print(names)
print(heights)

# transpose matrix
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
data_transpose = tuple(zip(*data))
print(data_transpose)

# enumerate
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
for i, cas in enumerate(cast):
    cast[i] = "{} {}".format(cas, str(heights[i]))
print(cast)

# list comprehension
multiples_3 = [num*3 for num in range(1,21)]
print(multiples_3)

[x*2 for x in range(9) if x%2==0]

a = [1, 0, 0, 2, 3, 0]
a_out = [1 if  i == 0 else i for i in a]
print(a_out)

a = [1, 0, 0, 2, 3, 0]
a_out = all(i == 0 for i in a)
print(a_out)

# dictionary comprehension

users = [
    (0, "user", "password"),
    (1, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}
userid_mapping = {user[0]: user for user in users}

print(username_mapping)

print(username_mapping["user"])  # (0, "user", "password")

# -- Collecting values --

head, *tail = [1, 2, 3, 4, 5]
print(head)  # 1
print(tail)  # [2, 3, 4, 5]


*head, tail = [1, 2, 3, 4, 5]
print(head)  # [1, 2, 3, 4]
print(tail)  # 5

# map
def addition(n):
    return n+n

numbers = [1,2,3,4]
map(addition, numbers)

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

# lambda

add = lambda x, y: x + y
print(add(1,2)) # (lambda x, y: x + y)(1,2)

def multiply(num):
    return num * 3
    
sequence = [1,2,3]
res = [(lambda x: x * 3)(x) for x in sequence]

res = [multiply(num) for num in sequence] # use this for complicated list comprehension

res = list(map(multiply, sequence))

res = list(map(lambda x: x * 3, sequence))

# lambda with map
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(lambda num_list: sum(num_list) / len(num_list), numbers))
print(averages)

# lambda with filter
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(lambda name: len(name) < 10, cities))
print(short_cities)

# generator function
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    index = start
    for value in iterable:
        yield index, value
        index += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

# generator chunker solution 1
def chunker(iterable, size):
    chunk_size = size
    chunk_pointer = 0;

    while chunk_pointer < len(iterable):
        yield iterable[chunk_pointer: chunk_pointer + chunk_size]
        chunk_pointer += chunk_size

for chunk in chunker(range(25), 4):
    print(list(chunk))

# generator chunker solution 2
def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))

# generator sequence
sq_list = [x**2 for x in range(10)]  # this produces a list of squares
sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares

# unpacking

# The asterisk takes all the arguments and packs them into a tuple.
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(3, 5))
print(multiply(-1))

def add(x, y):
    return x + y
    
# The asterisk can be used to unpack sequences into arguments too!
nums = [3, 5]
print(add(*nums))  # instead of add(nums[0], nums[1])

# Double asterisk packs or unpacks keyword arguments
def named(**kwargs):
    print(kwargs) # {'name': 'Bob', 'age': 25}
    
named(name="Bob", age=25)
# or
details = {"name": "Bob", "age": 25}
named(**details)

def named(name, age):
    print(name, age)
    
# Unpack dict into arguments. This is OK, but slightly more confusing. Good when working with variables though.
named(**{"name": "Bob", "age": 25}) 
# or 
details = {"name": "Bob", "age": 25}
named(**details)

# file open
with open('C:/Users/Vinay/Python Workspace/Nanodegree/README.md', 'r') as f:
    content = f.read()
print(content)

# looping in file
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())
print(camelot_lines)

# csv
import unicodecsv
def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

daily_engagement = read_csv('data/daily_engagement.csv')

def get_unique_students(data):
    unique_students = set()
    for data_point in data:
        unique_students.add(data_point['account_key'])
    return unique_students

unique_engagement_students = get_unique_student(daily_engagement)
len(unique_engagement_students)

# csv with Pandas
import pandas as pd
daily_engagement = pd.read_csv('data/daily_engagement.csv')
len(daily_engagement['account_key'].unique())

# Filling missing values
import pandas as pd

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])

s = s1 + s2
print(s).dropna()

s_fill = s1.sum(s2, fill_value=0)
print(s_fill)

# If we want to extract column A from dataframe
df['A']
# more coloumns
df[['B', 'D']]

# Turn pandas DataFrames into NumPy arrays
numpy.array(df)

# To display image
%pylab inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('ml_map.png')
imgplot = plt.imshow(img)
plt.show()