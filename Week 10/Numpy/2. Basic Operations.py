import numpy as np

# In numpy, axis 0 is the columns, and axis 1 is the rows

# arr = np.array([1,3,6])
# print(arr[2])

# arr = np.array([[1,2], [3,4], [5,6]])  # Create a 2D array object
# print(arr.ndim)  # Returns the number of dimensions in an array
# print(arr.itemsize)  # Returns the size (in bytes) of an element
# print(arr.dtype)  # Returns the datatype of an array

# arr = np.array([[1,2], [3,4], [5,6]], dtype=np.float64)
# print(arr.size)  # Returns the length of an array
# print(arr.shape)  # Returns the dimensions of an array
# print(arr)

# arr = np.array([[1,2], [3,4], [5,6]], dtype = complex)  # Datatype can be complex numbers as well
# print(arr)

# # Creates an array with a shape of 3 rows and 4 columns where every element is a zero.
# print(np.zeros((3,4)))

# # Creates an array with a shape of 4 rows and 5 columns where every element is a one.
# print(np.ones((4,5)))

# print(np.arange(1,8, 2))  # Array range, similar to python's range function.

# print(np.linspace(1,10,5))  # Generate 5 numbers between 1 and 10 which are linearly spaced

arr = np.array([[1,2], [3,4], [5,6]])

print(arr.reshape(2,3))  # Changes the dimensions of an array
print(arr.reshape(6,1))

print(arr.ravel())  # Flattens the array i.e Converts it into a 1D array

print(arr.min())  # Returns the minimum element
print(arr.max())  # Returns the maximum element
print(arr.sum())  # Returns the sum of all the elements in the array
print(arr.sum(axis=1))

print(np.sqrt(arr))  # Returns the square root of each element in the array
print(np.std(arr))  # Returns the standard deviation of the array
