# Recursion is when a function is defined in terms of itself.
# A recursive function calls itself.
# It has a base case to stop the recursion
# There is a general case where the recursive call takes place.
# With each call the recursive function is pushed into a Call Stack

def iterative_walk(steps):
    for i in range(steps):
        print("You took a step!")

def recursive_walk(steps):
    if steps == 0: # base case
        return -1
    else: # general case
        print("You took a step!")
        recursive_walk(steps - 1)

recursive_walk(5)

def factorial(num):
    if num < 1:
        return 1
    else:
        return factorial(num-1) * num
    
print(factorial(5))

def power(base, exp):
    if exp < 1:
        return 1
    else:
        return base * power(base,exp-1)
    
print(power(2,4))