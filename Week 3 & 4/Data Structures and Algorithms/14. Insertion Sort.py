# In insertion sort after comparing elements to the left of our current element,
# we shift elements to the right to make room to insert a value.
# Time Complexity: O(n^2), Best case is O(n)

import random

def insertion_sort(array):

    for i in range(1, len(array)):
        temp = array[i]
        pointer = i
        while pointer > 0 and array[pointer - 1] > temp:
            array[pointer] = array[pointer-1]
            pointer -= 1
        
        array[pointer] = temp

numbers = [random.randint(1,10) for i in range(10)]

print(numbers)

insertion_sort(numbers)

print(numbers)