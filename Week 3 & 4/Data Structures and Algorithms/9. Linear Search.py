# Linear Search iterates through a collection (array) one item at a time.
# Time Complexity : O(n)

numbers = [i for i in range(1,10)] # Makes an array of numbers from 1 to 10

number = int(input("Please enter the number to find: "))
found = False
for i in range(len(numbers)): # Iterate for length of the array numbers
    if number == numbers[i]:
        found = True
        index = i

if found: # If number was found
    print(f"{number} was found at index {index}.")
else:
    print(f"{number} could not be found.")
