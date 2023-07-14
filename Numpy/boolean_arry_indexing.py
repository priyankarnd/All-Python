import numpy as np

a = np.arange(12).reshape(3,4)
print(a)

# Conditions
b = a > 4
print(b)

print(a[b])

# Replacing values
a[b] = -1
print(a)
