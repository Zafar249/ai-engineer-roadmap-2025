# Functions are first class objects in python. They can be treated like any other variable.
# Functions can be passed as arguments to another function or returned as a return value

## Exercise: Decorators

class NegativeError(Exception):
    pass

class FloatError(Exception):
    pass

# 1. Create a decorator function to check that the argument passed to the function factorial is a 
# non-negative integer:


def decorator(func): # Wrapper function
    def wrapper(*args,  **kargs): # Takes positional arguments and keyword arguments as arguments
        result = None
        if float.is_integer(float(args[0])) == False:
            print("Error, Cannot find factorial of a float")
            raise FloatError
        elif (args[0]) >= 0:
            result = func(*args, **kargs)

        else:
            print("Error, Cannot find factorial of a negative number")
            raise NegativeError
        return result
    return wrapper

# 2. Create a factorial function which finds the factorial of a number.

@decorator  # Wrapped factorial with the decorator function
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
# 3. Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.

# example: 

#     factorial(1.354) : raise Exception or print error message
#     factorial(-1) : raise Exception or print error message
#     factorial(5) : 60

try:
    print(factorial(2))
except NegativeError:
    print("Please enter a positive number")

except FloatError:
    print("Please enter a positive integer")