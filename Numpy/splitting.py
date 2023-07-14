import numpy as np

a = np.arange(30).reshape(2,15)
print(a)

# Splitting into three equal sized arrays horizontally
result = np.hsplit(a,3)

print(result[0])
print(result[1])
print(result[2])

# Splitting into three equal sized arrays vertically
result = np.vsplit(a,2)

print(result[0])
print(result[1])