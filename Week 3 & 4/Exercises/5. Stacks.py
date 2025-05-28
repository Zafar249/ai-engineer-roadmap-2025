from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

# ## Data structure tutorial exercise: Stack
# 1. Write a function in python that can reverse a string using stack data structure. 
# Use [Stack class] from the tutorial.

stack = Stack()

string = input("Please enter a string to reverse: ")
for char in string:
    stack.push(char)

output = ""
while not stack.is_empty(): # While stack isn't empty
    output += stack.pop()

print(output)



# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

# 2. Write a function in python that checks if paranthesis in the string are balanced or not.
#  Possible parantheses are "{}',"()" or "[]".
#  Use [Stack class] from the tutorial.

#     is_balanced("({a+b})")     --> True
#     is_balanced("))((a+b}{")   --> False
#     is_balanced("((a+b))")     --> True
#     is_balanced("))")          --> False
#     is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

stack = Stack()
string = input("Please enter a string: ")
count_square = 0
count_round = 0
count_curvy = 0
for char in string:
    match char:
        case "{": count_curvy += 1
        case "}": count_curvy -= 1
        case "(": count_round += 1
        case ")": count_round -= 1
        case "[": count_square += 1
        case "]": count_square -= 1

    stack.push(string)

if count_square or count_curvy or count_round:
    print("False")
else:
    print("True")