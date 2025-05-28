# In selection sort you search through an array.
# During each iteration you keep track of the minimum value.
# At the end of each iteration we swap variables.
# Time Complexity: O(n^2)

import random

def selection_sort(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
        
        temp = array[min]
        array[min] = array[i]
        array[i] = temp

numbers = [random.randint(1,10) for i in range(10)]

print(numbers)

selection_sort(numbers)

print(numbers)