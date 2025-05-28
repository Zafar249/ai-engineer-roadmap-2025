# Binary Search is a searching algorithm that finds the 
# position/index of a target value within a sorted array
# Half of the array is disregarded with each step
# Time complexity : O(log n)

def binary_search(array, target):
    lower = 0
    upper = len(array) - 1

    while lower <= upper:
        mid = int((upper + lower )/ 2) # Finding middle index of array
        print(f"Mid element: {mid}")
        val = array[mid]
        if target > val: 
            lower = mid + 1
        elif target < val:
            upper = mid-1
        else:
            return mid # Number found 
    
    return -1 # Number not found

numbers = [i for i in range(1,101)]
value = int(input("Please enter value to search: "))

index = binary_search(numbers, value)

if index != -1:
    print(f"{value} found at index {index}")
else:
    print("Value not found!")