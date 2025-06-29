import numpy as np
import time
import sys

# numpy arrays store data contiguously and each element takes 8 bytes of memory.
# Python lists store an array of pointers contiguously and each pointer points to an array object in
# memory which takes 28 bytes of memory.

# arr = np.array([1,2,3])  # Create an array object

# # Numpy arrays require less memory, are faster and more convinient than python lists.

# list = range(1000)  # Create an array from 0 to 999
# print(sys.getsizeof(1) * len(list))  # Returns memory size of list

# arr = np.arange(1000)  # Similar to range function
# print(arr.size * arr.itemsize)

# SIZE = 100000

# list1 = range(SIZE)
# list2 = range(SIZE)

# arr1 = np.arange(SIZE)
# arr2 = np.arange(SIZE)

# start = time.time()
# result = [ (x + y) for x, y in zip(list1, list2)]  # Add each element of list1 to list2
# print("Python list took:", (time.time() - start) * 1000)  # Calculate execution time in miliseconds

# start = time.time()
# result = arr1 + arr2
# print("Numpy array took:", (time.time() - start) * 1000)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(arr1 + arr2)  # Add arr1 to arr2
print(arr2 - arr1)  # Subtract arr1 from arr2
print(arr1 * arr2)  # Multiply arr1 with arr2
print(arr2 / arr1)  # Divide arr2 by arr1

print(arr1.dot(arr2))  # Takes the matrix product of arr1 and arr2