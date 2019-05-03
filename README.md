# python-sandbox
## Some description

To install all dependencies listed in requirements.txt
`pip install -r requirements.txt`

## String methods
**Here are some of the most common string methods**
- s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
- s.strip() -- returns a string with whitespace removed from the start and end
- s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
- s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
- s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
- s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
- s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text.
- 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
- s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc

## List Methods
**Here are some common list methods**
- list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
- list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
- list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
- list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear - (use "in" to check without a ValueError).
- list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
- list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
- list.reverse() -- reverses the list in place (does not return it)
- list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append())

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

### NLTK
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