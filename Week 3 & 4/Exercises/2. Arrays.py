# Already done in Week 2: 5.Lists
# 3.Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function

num = int(input("Please enter the maximum number of the array: "))
odd_numbers = []
for i in range(1,num+1,2):
    odd_numbers.append(i)

print(odd_numbers)