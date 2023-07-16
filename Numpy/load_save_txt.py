import numpy as np

'''
# Save
a = np.array([[1,2,3], [4,5,6], [7,8,9]], np.int32)

np.savetxt("test.txt", a)
'''

# Load
x = np.loadtxt("test.txt")
print(x)

'''
Options:
Delimiter
Skiprow
'''
