import numpy as np

a = np.array([[1,2], [3,4]])
print(a)
b = np.array([[5,6], [7,8]])
print(b)

# Mathematical operations
s = a + b
print(s)

m =  a * b
print(m)

su = b - a
print(su)

d = b/a
print(d)

matmul = a.dot(b)
print(matmul)
