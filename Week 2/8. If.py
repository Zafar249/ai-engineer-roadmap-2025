# ## Exercise: Python If Condition
# 1. Using following list of cities per country,

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

#     1. Write a program that asks user to enter a city name and 
#        it should tell which country the city belongs to
city = input("Please enter a city name: ")
if city in india:
    print(f"{city} is in India.")
elif city in pakistan:
    print(f"{city} is in Pakistan.")
elif city in bangladesh:
    print(f"{city} is in Bangladesh.")
else:
    print("City not found")

#     2. Write a program that asks user to enter two cities and it tells you
#        if they both are in same country or not. For example if I enter mumbai and chennai,
#        it will print "Both cities are in India" but if I enter mumbai and dhaka it should print
#       "They don't belong to same country"

city1 = input("Please enter in first city: ")
city2 = input("Please enter in second city: ")

if city1 in india and city2 in india:
    print("Both cities are in India.")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in Pakistan.")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in Bangladesh.")
else:
    print("They don't belong to same country")

#     2. Write a python program that can tell you if your sugar is normal or not. 
#        Normal fasting level sugar range is 80 to 100.

#     1. Ask user to enter his fasting sugar level

sugar_level = int(input("Please enter your sugar level: "))

#     2. If it is below 80 to 100 range then print that sugar is low

if sugar_level < 80:
    print("Low sugar level.")
#     3. If it is above 100 then print that it is high otherwise print that it is normal

elif sugar_level > 100:
    print("High sugar level.")
else:
    print("Normal sugar level.")
