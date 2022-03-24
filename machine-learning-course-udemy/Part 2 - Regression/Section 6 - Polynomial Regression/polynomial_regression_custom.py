# Data Pre-processing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dir = 'C:\\Users\\Bourbon\\machine-learning-course-udemy\\Part 2 - Regression\\Section 6 - Polynomial Regression\\'
dataset = pd.read_csv(dir+'Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Fitting Linear Regression to the Dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting Polynomial Regression to the Dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=3)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Visualizing the actual data
plt.scatter(X, y, color='green')
plt.title('Truth or Bluff - Original Data')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

# Visualizing the Linear Regression results
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('Truth or Bluff - Linear Regression')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

# Visualizing the Polynomial Regression results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color='red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color='blue')
plt.title('Truth or Bluff - Polynomial Regression')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

# Predict a new result with Linear Regression
lin_reg.predict(6.5)

# Predict a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(6.5))