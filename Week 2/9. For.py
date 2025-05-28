# ## Exercise: Python for loop
# 1. After flipping a coin 10 times you got this result,

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

# Using for loop figure out how many times you got heads

count = 0
for i in range(len(result)):
    if result[i] == "heads":
        count += 1

print(f"The number of heads is {count}.")

# 2. Print square of all numbers between 1 to 10 except even numbers

for i in range(1,10,2):
    square = i ** 2
    print(f"The square is: {square}")

# 3. Your monthly expense list (from Jan to May) looks like this,

expense_list = [2340, 2500, 2100, 3100, 2980]

# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.

expense = int(input("Please enter the expense: "))
for i in range(len(expense_list)):
    if expense == expense_list[i]:
        match i+1:
            case 1: print("The expense occured in January")
            case 2: print("The expense occured in February")
            case 3: print("The expense occured in March")
            case 4: print("The expense occured in April")
            case 5: print("The expense occured in May")
    else:
        print("The expense was not found")
        break

# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message

flag = False
for i in range(5):
    tired = input("Are you tired?")
    if tired == "yes":
        print("You didn't finish the race.")
        flag = True
        break
        
if not flag:
    print("Congratulations, you finished the race.")

# 5. Write a program that prints following shape

# *
# **
# ***
# ****
# *****

for i in range(1,6):
    print('*'*i)

string = ""
for i in range(1,6):
    string += "*"
    print(string)
