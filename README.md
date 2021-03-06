# Python

To install package:

`python3 -m pip install package`

To install all dependencies listed in requirements.txt:

`pip3 install -r requirements.txt`

Virtual Environment:

```python
pip3 install virtualenv # installing
python3 -m venv env # creating virtual python installation in the env folder
virtualenv -p python3 env # another way to create
source env/bin/activate # activate
which python # confirm virtual environment
deactivate # leave virtual environment
```

|Data Structures|Ordered|Mutable|Constructor|
|---------------|-------|-------|-----------|
|int|NA|NA|int()|
|float|NA|NA|float()|
|string|Yes|No|' ' or " " or str()|
|bool|NA|NA|NA|
|list|Yes|Yes|[] or list()|
|tuple|Yes|No|( ) or tuple()|
|set|No|Yes|{ } or set()|
|dictionary|No|Keys:No|{ } or dict()|

**Class Attributes** belong to the class itself they will be shared by all the instances. Such attributes are defined in the class body parts usually at the top, for legibility.

**Instance Attributes** are not shared by objects. Every object has its own copy of the instance attribute.

## String

### Here are some common string methods

|Method|Description|
|------|-----------|
|s.lower(), s.upper()|returns the lowercase or uppercase version of the string|
|s.strip()|returns a string with whitespace removed from the start and end|
|s.isalpha() / s.isdigit() / s.isspace()|tests if all the string chars are in the various character classes|
|s.startswith('other'), s.endswith('other')|tests if the string starts or ends with the given other string|
|s.find('other')|searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found|
|s.replace('old', 'new')|returns a string where all occurrences of 'old' have been replaced by 'new'|
|s.split('delim')|returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text|
|'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']|As a convenient special case s.split() (with no arguments) splits on all whitespace chars|
|s.join(list)| opposite of split(), joins the elements in the given list together using the string as the delimiter e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc|

## List

### Here are some common list methods

|Method|Description|
|------|-----------|
|list.append(elem)|adds a single element to the end of the list. Common error: does not return the new list, just modifies the original|
|list.insert(index, elem)|inserts the element at the given index, shifting elements to the right|
|list.extend(list2)|adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend()|
|list.index(elem)|searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear - (use "in" to check without a ValueError)|
|list.remove(elem)|searches for the first instance of the given element and removes it (throws ValueError if not present)|
|list.sort()|sorts the list in place (does not return it). (The sorted() function shown later is preferred.)|
|list.reverse()|reverses the list in place (does not return it)|
|list.pop(index)|removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append())|
|list.count(elem)|returns count of how many times elem occurs in list|
|list.extend(seq)|Appends the contents of seq to list|
|list(seq)|converts a tuple into list|
|len(list)|gives the total length of the list|
|concatenation|[1, 2, 3] + [4, 5, 6] => [1,2,3,4,5,6]|
|Membership|3 in [1,2,3] => True|
|Slicing|list[-1]=>last element, list[1:]=>elements from index 1|

## Dictionary

### Here are some common dictionary methods

|Method|Description|
|------|-----------|
|dict['key'] = 'value'|add one new key value pair|
|dict['key']|Get value of the key|
|dict['key'] = 'updated-value'|update key value pair|
|del dict['key']|Remove the key|
|dict.update({'key1': 'val', 'key2': 'val'})|Adds dictionary key-values pairs to dict|
|dict.get('key')|For key key, returns value|
|dict.get('key', 0)|default value for key|
|dict.pop('key')|pop method removes a key and returns the value|
|dict.keys()|returns the keys of the dictionary as a list|
|dict.values()|returns the values in the dictionary as a list|
|dict.items()|returns a list of tuples where each tuple is of the form (key, value)|
|dict.clear()|Removes all elements of dictionary dict|
|dict.copy()|Returns a shallow copy of dictionary dict|
|dict.has_key(key)|Returns true if key in dictionary dict, false otherwise|
|str(dict)|Produces a printable string representation of a dictionary|
|len(dict)|number of items in the dictionary|

## Tuple

### Here are some common tuple methods

|Method|Description|
|------|-----------|
|len(tuple)|Gives the total length of the tuple|
|max(tuple)|Returns item from the tuple with max value|
|min(tuple)|Returns item from the tuple with min valueReturns item from the tuple with min value|
|tuple(seq)|Converts a list into tuple|
|tuple[0]|Return the item in position 1|
|tuple.count('value')|Returns the number of times a specified value occurs in a tuple|
|tuple.index('value')|Searches the tuple for a specified value and returns the position of where it was found|
|del tuple|delete the tuple completely|

## Set

### Here are some common tuple methods

|Method|Description|
|------|-----------|
|set.add(item)|add an item to a set|
|set.update(["orange", "mango", "grapes"])|Add multiple items to a set|
|set.remove("banana")|raises error if item doesn't exist|
|set.discard("banana")|will not raise an error|
|set.clear()|empties the set|
|del set|deletes the set completely|
|set1.union(set2)|returns a set by joining two sets|
|set1.update(set2)|inserts the items in set2 into set1|
|set.copy()|returns a copy of the set|
|set1.difference(set2)|returns a set containing the difference between two or more sets|
|set1.difference_update(set2)|removes the items in this set that are also included in another, specified set|
|set1.intersection(set1)|returns a set, that is the intersection of two other sets|
|set1.intersection_update(set2)|removes the items in this set that are not present in other, specified set(s)|
|issubset()|returns whether another set contains this set or not|
|issuperset()|returns whether this set contains another set or not|

## File Path Manipulation

```
import os.path

# Get the path of current working directory
dirpath = os.getcwd()
foldername = os.path.basename(dirpath)

# Get the path of script file
scriptpath = os.path.realpath(__file__)

# get dir part of path
print(os.path.dirname("/home/aa/bb/ff.html"))
# /home/aa/bb

# get file name part of a path
print(os.path.basename("/home/aa/bb/ff.html"))
# ff.html

# split path into dir part, file part
fp = "/home/aa/bb/ff.html"

print(os.path.split(fp))
# ('/home/aa/bb', 'ff.html')

# Get File Extension
x = os.path.splitext("/home/aa/bb/ff.html")

print(x)
# ('/home/aa/bb/ff', '.html')

# get file extension
print(x[1])
# .html

# check if file exists
print(os.path.exists("/home/"))
# True

# compute relative path
print(os.path.relpath("/home/aa/bb/ff.html", "/home/aa/"))
# bb/ff.html

# get absolute path
fp = "/usr/bin/../bin/vi"

# remove redundant ../
print(os.path.normpath(fp))
# /usr/bin/vi

# similar to os.path.normpath(fp) but does a bit more
print(os.path.abspath(fp))
# /usr/bin/vi

# resolve symbolic link
print(os.path.realpath("/usr/bin/vi"))
# /usr/bin/vim
```

## Functional Programming Principles

- **First Class Functions** : Passing functions as arguments to other functions, returning them as the values from other functions, and assigning them to variables or storing them in data structures.
- **Pure Functions** : Thus a pure function is a computational analogue of a mathematical function
    1. Its return value is the same for the same arguments (no variation with local static variables, non-local variables, mutable reference arguments or input streams from I/O devices).
    2. Its evaluation has no side effects (no mutation of local static variables, non-local variables, mutable reference arguments or I/O streams).
- **Lazy Evaluation** : It is an evaluation strategy which delays the evaluation of an expression until its value is needed (non-strict evaluation) and which also avoids repeated evaluations.
- **Immutable variables & Objects**
- **Recursion**
- **Pattern Matching**

## Useful Third-Party Packages

- IPython - A better interactive Python interpreter
- requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
- Flask - a lightweight framework for making web applications and APIs.
- Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
- Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
- pytest - extends Python's builtin assertions and unittest module.
- PyYAML - For reading and writing YAML files.
- NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful    linear algebra capabilities.
- pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
- matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
- ggplot - Another 2D plotting library, based on R's ggplot2 library.
- Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
- pyglet - A cross-platform application framework intended for game development.
- Pygame - A set of Python modules designed for writing games.
- pytz - World Timezone Definitions for Python

## NumPy

NumPy stands for Numerical Python and it's a fundamental package for scientific computing in Python. NumPy provides Python with an extensive math library capable of performing numerical computations effectively and efficiently. In the following lessons you will learn:

- How to import NumPy
- How to create multidimensional NumPy ndarrays using various methods
- How to access and change elements in ndarrays
- How to load and save ndarrays
- How to use slicing to select or change subsets of an ndarray
- Understand the difference between a view and a copy an of ndarray
- How to use Boolean indexing and set operations to select or change subsets of an ndarray
- How to sort ndarrays
- How to perform element-wise operations on ndarrays
- Understand how NumPy uses broadcasting to perform operations on ndarrays of different sizes.

## Pandas

One very important step in machine learning is to look at your data first and make sure it is well suited for your training algorithm by doing some basic data analysis. This is where Pandas come in. Pandas Series and DataFrames are designed for fast data analysis and manipulation, as well as being flexible and easy to use. Below are just a few features that makes Pandas an excellent package for data analysis:

- Allows the use of labels for rows and columns
- Can calculate rolling statistics on time series data
- Easy handling of NaN values
- Is able to load data of different formats into DataFrames
- Can join and merge different datasets together
- It integrates with NumPy and Matplotlib

## PySpark functions

- select(): returns a new dataframe with the selected columns
- filter(): filters rows using the given condition
- where(): is just an alias for filter()
- groupBy(): groups the DataFrame using the specified columns, so we can run aggregation on them
- sort(): returns a new DataFrame sorted by the specified column(s). By default the second parameter 'ascending' is True
- dropDuplicates(): returns a new dataframe with unique rows based on all or just a subset of columns
- withColumn(): returns a new DataFrame by adding a column or replacing the existing column that has the same name. The first parameter is the name of the new column, the second is an expression of how to compute it

Spark SQL provides built-in methods for the most common aggregations such as count(), countDistinct(), avg(), max(), min(), etc. in the pyspark.sql.functions module.

In Spark SQL we can define our own functions with the User defined functions (UDF) method from the pyspark.sql.functions module.

Window functions are a way of combining the values of ranges of rows in a dataframe. When defining the window we can choose how to sort and group (with the partitionBy method) the rows and how wide of a window we'd like to use (described by rangeBetween or rowsBetween).

## NLTK

Language processing tasks and corresponding NLTK modules with examples of functionality:

| Language processing task | NLTK modules |	Functionality |
|--------------------------|--------------|---------------|
| Accessing corpora | corpus | standardized interfaces to corpora and lexicons |
| String processing | tokenize, stem | tokenizers, sentence tokenizers, stemmers |
| Collocation discovery | collocations | t-test, chi-squared, point-wise mutual information |
| Part-of-speech tagging | tag | n-gram, backoff, Brill, HMM, TnT |
| Machine learning | classify, cluster, tbl | decision tree, maximum entropy, naive Bayes, EM, k-means |
| Chunking | chunk | regular expression, n-gram, named-entity |
| Parsing |	parse, ccg | chart, feature-based, unification, probabilistic, dependency |
| Semantic interpretation | sem, inference | lambda calculus, first-order logic, model checking |
| Evaluation metrics | metric | precision, recall, agreement coefficients |
| Probability and estimation | probability | frequency distributions, smoothed probability distributions |
| Applications | app, chat | graphical concordancer, parsers, WordNet browser, chatbots |
| Linguistic fieldwork | toolbox | manipulate data in SIL Toolbox format |
