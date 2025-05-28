# In quick sort we move smaller elements to the left of the pivot
# We recursively divide the array into 2 partitions
# Time Complexity: O(n log(n))
#      Worst Case: O(n^2) if array is already sorted
# Space Complexity: O(log (n)) due to recursion

import random

def partition(array, start, end):

    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        if array[j] < pivot:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    i += 1
    temp = array[i]
    array[i] = array[end]
    array[end] = temp
    return i # The location of our pivot

def quick_sort(array, start, end):
    if start >= end: # base case, we cannot divide the array any further
        return 0
    else: # general case
        pivot = partition(array, start, end)
        quick_sort(array, start, pivot-1)
        quick_sort(array, pivot+1, end)


numbers = [2,4,3,5]

print(numbers)

quick_sort(numbers, 0, len(numbers)-1)

print(numbers)