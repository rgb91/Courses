# Data Pre-processing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = np.array([4,23,2,4,1])
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer   = Imputer(missing_value='NaN', strategy='mean', axis=0)
imputer   = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)
X
# Categorical variable to numeric variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X = LabelEncoder()
X[:, 0] = labelEncoder_X.fit_transform(X[:, 0])
labelEncoder_Y = LabelEncoder()
Y = labelEncoder_Y.fit_transform(Y)

oneHotEncoder = OneHotEncoder(categorical_features=[0])
X = oneHotEncoder.fit_transform(X).toarray()

# from sklearn.cross_validation import train_test_split
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
# print(Y)