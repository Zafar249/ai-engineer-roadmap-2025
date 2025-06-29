import numpy as np

# Slicing in numpy array is similar to python lists
# For 2D arrays [row, column]
# For slicing [x:y], x is inclusive but y is exclusive

# arr = np.array([6,7,8])
# print(arr[0:2])
# print(arr[-1])

# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr[1,2])
# print(arr[0:2,1])
# print(arr[:,-1])  # Returns last column

# # Iteration
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# for row in arr:
#     print(row)  # Prints each row in array

# for cell in arr.flat:  # Flattens the 2D array to a 1D array
#     print(cell)  # Prints individual elements

# # Stacking
# arr = np.arange(6).reshape(3,2)
# arr2 = np.arange(6,12).reshape(3,2)
# print(arr)
# print(arr2)

# print(np.vstack((arr, arr2)))  # Vertically stacks arr on top of arr2
# print(np.hstack((arr, arr2)))  # Horizontally stacks arr with arr2

# Splitting
arr = np.arange(30).reshape(2,15)
print(arr)
result = np.hsplit(arr, 3)  # Vertically slices arr into 3 different equally sized arrays
print(result[0])

result = np.vsplit(arr, 2)  # Horizontally slices arr into 2 different equally sized arrays
print(result[0])

# Indexing
arr = np.arange(12).reshape(3,4)
print(arr)

arr2 = arr > 5  # Compares whether each element in arr is greater than 5
print(arr2)

# Returns all elements from the original array where the comparison in the indexed array is true
print(arr[arr2])  

# All elements in the original array where the comparison in the indexed array is true 
# are assigned a value of -1
arr[arr2] = -1  # All elements greater than 5
print(arr)  