# -*- coding: utf-8 -*-
"""Exp-04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aL3dcOovV1_p1H2GbRXMJZvCG_obuiY1
"""

# importing dependencies
import numpy as np
import matplotlib.pyplot as plt

# creating data
mean = np.array([5.0, 6.0])
cov = np.array([[1.0, 0.95], [0.95, 1.2]])
data = np.random.multivariate_normal(mean, cov, 8000)

# visualising data
plt.scatter(data[:500, 0], data[:500, 1], marker='.')
plt.show()

# train-test-split
data = np.hstack((np.ones((data.shape[0], 1)), data))

split_factor = 0.90
split = int(split_factor * data.shape[0])

X_train = data[:split, :-1]

y_train = data[:split, -1].reshape((-1, 1))

X_test = data[split:, :-1]

y_test = data[split:, -1].reshape((-1, 1))

print("Number of examples in training set =", X_train.shape[0])
print("Number of examples in testing set =", X_test.shape[0])