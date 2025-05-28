#Create 3 variables to store street, city and country, 
# now create address variable to store entire address. 
# Use two ways of creating this variable, one using + operator and the other using f-string. 
# Now Print the address in such a way that the street, city and country prints in a separate line
# street = "94-Q"
# city = "Lahore"
# country = "Pakistan"
# address = street + "\n" + city + "\n" + country
# address = f"{street}\n{city}\n{country}"
# print(address)

#Create a variable to store the string "Earth revolves around the sun"
#    Print "revolves" using slice operator
#    Print "sun" using negative index
fact = "The Earth revolves around the sun."
print(fact[10:18])
print(fact[-4:-1])

#Create two variables to store how many fruits and vegetables you eat in a day.
#  Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits
#  that you eat everyday. Use python f string for this.'
fruits = 5
vegetables = 3
print("I eat {x} veggies and {y} fruits daily".format(x=vegetables, y=fruits))

#I have a string variable called s='maine 200 banana khaye'.
#  This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
#  Replace incorrect words in original strong with new ones and print the new string.
#  Also try to do this in one line.
string = "maine 200 banana khaye"
string = string.replace("200 banana","10 samosa")
print(string)
