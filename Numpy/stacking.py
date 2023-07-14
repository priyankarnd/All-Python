import numpy as np

a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)

print(a)
print(b)

c = np.vstack((a,b))
print(c)

c = np.hstack((a,b))
print(c)