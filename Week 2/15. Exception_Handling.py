#     Safe Number Input
#     Ask the user for a number. Handle cases where they enter non-numeric values.
#     Print "Invalid input" for non-numbers.

try:
    num = float(input("Please enter a number: "))
    print(num)
except ValueError:
    print("Invalid Input")

#     List Element Access
#     Create a list of 5 items. Ask for an index. Handle IndexError if the index is out of range, 
#     and print "Index doesn't exist".

numbers = [1,2,3,4,5]
index = int(input("Please enter an index: "))
try:
        print(numbers[index])
except IndexError:
    print("Index doesn't exist")

# Intermediate:
# 3. File Reader
# Ask for a filename. Handle FileNotFoundError if the file doesn't exist. Print a custom message instead of crashing.
try:
    file_name = input("Please enter a file name: ")
    file = open(file_name,"r")
    file.close()
except FileNotFoundError:
    print("File could not be found.")

# Advanced:
# 5. Bank Account Withdrawal
# Simulate a bank account with balance $1000. If withdrawal amount exceeds balance, raise InsufficientFundsError. Handle it gracefully.

class InsufficientFundsError(Exception):
    pass

amount = 1000
withdraw = int(input("Please enter amount to withdraw: "))
try:
    if withdraw > amount:
        raise InsufficientFundsError("Insufficient Funds")
except InsufficientFundsError as e:
    print(e)
#     Dictionary Key Check
#     Create a dictionary of student grades. Ask for a student name. Handle KeyError if the name isn't found, and suggest checking the spelling.
students = {"Maarij": "A",
            "Soman": "B",
            "Ashmal": "A-"}
try:
    name = input("Please enter a student name: ")
    print(students[name])
except KeyError:
    print("Could not find student.")

# Challenge Problems:
# 7. Nested Exceptions
# Write code that could throw both ValueError and ZeroDivisionError in the same operation. Handle them with a single except block.

try:
    num = input("Please enter a number: ")
    reciprocal = 1 / int(num)
    print(reciprocal)
except (ValueError, ZeroDivisionError):
    print("Please enter a non zero integer")

