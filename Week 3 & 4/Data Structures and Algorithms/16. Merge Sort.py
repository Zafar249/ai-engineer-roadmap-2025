# In merge sort you recursively divide an array in 2.
# Then you sort the divided arrays and re-combine them.
# Time Complexity: O(n log n)
# Space Complexity: O(n)

# A helper method is a method that helps another method
import random

def merge(left_array, right_array, array): # helper method
    leftsize = int(len(array) / 2)
    rightsize = len(array) - leftsize
    i = 0 # Indices
    l = 0
    r = 0

    # Check conditions for merging
    while l < leftsize and r < rightsize:
        if left_array[l] < right_array[r]:
            array[i] = left_array[l]
            i += 1
            l += 1
        else:
            array[i] = right_array[r]
            i += 1
            r += 1
    while (l < leftsize):
        array[i] = left_array[l]
        i += 1
        l += 1
    while (r < rightsize):
        array[i] = right_array[r]
        i += 1
        r += 1

def merge_sort(array):
    length = len(array)
    if length <= 1: # Base Case, if array consists of only one element
        return 0
    else: # General case
        mid = int(length / 2)
        left_array = [0 for i in range(mid)]
        right_array = [0 for i in range(len(array)-mid)]
        i = 0
        j = 0

        for i in range(len(array)):
            if i < mid:
                left_array[i] = array[i]
            else:
                right_array[j] = array[i]
                j += 1

        merge_sort(left_array)
        merge_sort(right_array)
        merge(left_array, right_array, array)

numbers = [random.randint(1,10) for i in range(4)]

print(numbers)

merge_sort(numbers)

print(numbers)