import numpy as np

a = np.array([1,2,3])
print(a[0])
print(a[1])
print(a[2])

print(a[0:2])

print(a[-1])

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(a)

print(a[1])
print(a[1,2])

print(a[0:2])
print(a[0:2,2])

print(a[-1])
print(a[-1,1:3])
print(a[:,1:3])

for row in a:
    print(row)

for cell in a.flat:
    print(cell)