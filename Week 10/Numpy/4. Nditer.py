import numpy as np

arr = np.arange(12).reshape(3,4)

# for row in arr:
#     print(row)

# for cell in arr.flatten():  # Flattens the 2D array into a 1D array 
#     print(cell)


# for x in np.nditer(arr, order = "C"):  # Iterates through each row of the array, printing each column
#     print(x)


# for x in np.nditer(arr, order="F"):  # Iterates through each column of the array, printing each row
#     print(x)  # Fortran order

#  # Iterates through each column of the array, printing the whole column
# for x in np.nditer(arr, order="F", flags=["external_loop"]): 
#     print(x)  # Fortran order

for x in np.nditer(arr, op_flags=["readwrite"]):
    x[...] = x ** 2  # Returns the square of each element in the array and modifies the orignal array

print(arr)

arr2 = np.arange(3,15,4).reshape(3,1)

for x, y in np.nditer([arr, arr2]):  # Iterates through both arrays simultaneously
    print(x,y) 
    
# Both arrays should be broadcastable meaning the dimensions should be the same
# or one of the dimensions should be 1
# e.g: arr.shape =  (3,4)
#      arr2.shape = (3,1)
