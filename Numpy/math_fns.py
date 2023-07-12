import numpy as np

a = np.array([[1,2], [3,4], [5,6]])

# Finding min max
print(a.min())
print(a.max())

# Finding out sum
print(a.sum())

# Axes, axis 0: columns, axis 1: rows
print(a.sum(axis=0))
print(a.sum(axis=1))

# Square root
print(np.sqrt(a))

# Standard deviation
print(np.std(a))