# In bubble sort pairs of adjacent elements in an array are compared.
# If they are not in order, they are swapped with each other.
# Time Complexity: O(n^2)
import random

def bubble_sort(array):
    # # Inefficient bubble sort
    # for i in range(len(array)-1):
    #     for j in range(len(array)-i-1):
    #         if array[j] > array[j+1]: # If number at current index is greater than number at next index
    #             temp = array[j]
    #             array[j] = array[j+1]
    #             array[j+1] = temp

    # Efficient bubble sort
    boundary = len(array) - 1
    no_swap = False
    while boundary > 0 and not no_swap: # While elements in Array are being swapped
        no_swap = True
        for i in range(boundary):
            if array[i] > array[i+1]: # If number at current index is greater than number at next index
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                no_swap = False
        boundary -=1


numbers = [random.randint(1,10) for i in range(10)]
print(numbers)

bubble_sort(numbers)

print(numbers)