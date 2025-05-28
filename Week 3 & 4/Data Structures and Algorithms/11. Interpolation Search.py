# Interpolation Search is an improvement over Binary Search.
# It is best used for uniformly distributed data.
# It guesses where a value might be based on calculated probe results.
# If probe is incorrect, search area is narrowed, and a new probe is calculated

# Time complexity: Average case O(log(log n))
#                  Worst case O(n) [values increase exponentially]

def interpolation_search(array, target):
    lower = 0
    upper = len(array) - 1
    
    while (array[lower] <= target <= array[upper] and lower <= upper):
        probe = lower + int( ( (upper - lower) * (target - array[lower]) )
                            /(array[upper] - array[lower]) ) # Calculate Probe
        print(f"Probe: {probe}")
        if array[probe] < target:
            lower = probe + 1
        elif array[probe] > target:
            upper = probe - 1
        else:
            return probe # Number found
        
    return -1 # Number not found

numbers = [i for i in range(1,101)]
value = int(input("Please enter a value to search for: "))

index = interpolation_search(numbers, value)

if index != -1:
    print(f"{value} was found at index {index}")
else:
    print("Value not found!")