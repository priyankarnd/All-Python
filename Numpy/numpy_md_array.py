import numpy as np

a = np.array([[1,2], [3,4], [5,6]])

# Dimensions of array
print(a.ndim)

# Datatype
print(a.dtype)

# Itemsize in bytes
print(a.itemsize)

# Change dtype to float
a = np.array([[1,2], [3,4], [5,6]], dtype=np.float64)
print("Float")
print(a)
print(a.dtype)
print(a.itemsize)

# Total no. of elements
print(a.size)

# Shape of the dimensions : #Rows, #Columns
print(a.shape)

# Reshaping array
b = a.reshape(2,3)
print(b)

b = a.reshape(6,1)
print(b)

# Flatten to 1 dimension
c = b.ravel()
print(c)

# Declare a numpy array with complex no.
a = np.array([[1,2], [3,4], [5,6]], dtype=complex)
print(a)

# Declare a numpy array with placeholders
a = np.zeros((3,4))
print(a)

a = np.ones((3,4))
print(a)