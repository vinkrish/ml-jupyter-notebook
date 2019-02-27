# import statements for the classification algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

import pandas
import numpy

# Read the data
data = pandas.read_csv('sklearn-data.csv')

# Split the data into X and y
X = numpy.array(data[['x1', 'x2']])
y = numpy.array(data['y'])

"""
Note:The capitalization may look strange, as X is capitalized whereas y is lowercase, but this is standard notation, as X represents a matrix of (maybe) several columns, and y a single column vector.
"""

# Logistic Regression Classifier
classifier = LogisticRegression()
classifier.fit(X,y)

# Decision Tree Classifier
classifier = DecisionTreeClassifier()
classifier.fit(X,y)

# Support Vector Machine Classifier
classifier = SVC()
classifier.fit(X,y)

# Neural Networks
from sklearn.neural_network import MLPClassifier
classifier = MLPClassifier()

# classifier = SVC(kernel = 'poly', degree = 2)
# classifier = SVC(kernel = 'rbf', degree = None, gamma = 200, C = None)
"""
kernel (string): 'linear', 'poly', 'rbf'.
degree (integer): This is the degree of the polynomial kernel, if that's the kernel you picked (goes with poly kernel).
gamma (float): The gamma parameter (goes with rbf kernel).
C (float): The C parameter.
"""
