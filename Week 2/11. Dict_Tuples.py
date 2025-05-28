import math
import statistics

# 1. We have following information on countries and their population (population is in crores),

#     |Country|Population|
#     |-------|----------|
#     |China|143|
#     |India|136|
#     |USA|32|
#     |Pakistan|21|
#     1. Using above create a dictionary of countries and its population

information = {
    "China" : 143,
    "India": 136,
    "USA" : 32,
    "Pakistan" : 21
}

#     2. Write a program that asks user for three type of inputs,
#         1. print: if user enter print then it should print all countries 
#                   with their population in this format,
#             china==>143
#             india==>136
#             usa==>32
#             pakistan==>21

def print_dict(info):
    for key, value in info.items():
        print(f"{key}==>{value}")

#         1. add: if user input add then it should further ask for a country name to add. 
#                 If country already exist in our dataset then it should print that it exist and
#                 do nothing. If it doesn't then it asks for population and add that new 
#                 country/population in our dictionary and print it

def add_dict(info):
    name = input("Please enter a country name to add: ")
    if name in info:
        print(f"{name} already exists")
    else:
        population = int(input("Please enter the population: "))
        info.update({name: population})
        # print(f"The country {name} has a population of {info[name]}")
    print_dict(info)
    return info

#         2. remove: when user inputs remove it should ask for a country to remove. 
#                    If country exist in our dictionary then remove it and print new dictionary using 
#                    format shown above in (a). Else print that country doesn't exist!

def remove_dict(info):
    country = input("Please enter a country's name to delete: ")
    if country in info:
        info.pop(country)
        print_dict(info)
    else:
        print("That country doesn't exist.")
    return info

#         3. query: on this again ask user for which country he or she wants to query. 
#                   When user inputs that country it will print population of that country.

def query(info):
    country = input("Please enter the country you want to query: ")
    print(f"The population of {country} is {info.get(country)}")

# while True:
#     user = input("What function would you like to do?\n" \
#     "1. Print\n" \
#     "2. Add\n" \
#     "3. Query\n" \
#     "4. Remove\n" \
#     "5. Exit: ")
#     match user:
#         case "Print": print_dict(information)
#         case "Add" : information = add_dict(information)
#         case "Query": query(information)
#         case "Remove" : information = remove_dict(information)
#         case "Exit" : break



# 2. You are given following list of stocks and their prices in last 3 days,

#     |Stock|Prices|
#     |-------|----------|
#     |info|[600,630,620]|
#     |ril|[1430,1490,1567]|
#     |mtl|[234,180,160]|

stocks = dict(info = [600,630,620], ril = [1430, 1490, 1567], mtl=[234, 180, 160])
#     1. Write a program that asks user for operation. Value of operations could be,
#         1. print: When user enters print it should print following,

#             info ==> [600, 630, 620] ==> avg:  616.67
#             ril ==> [1430, 1490, 1567] ==> avg:  1495.67
#             mtl ==> [234, 180, 160] ==> avg:  191.33

def print_dict2(info):
    for key, value in info.items():
        avg = statistics.mean(value)
        print(f"{key}==>{value}==>avg: {round(avg, 2)}")

#         2. add: When user enters 'add', it asks for stock ticker and price.
#                 If stock already exist in your list (like info, ril etc) then it will append the price
#                 to the list. Otherwise it will create new entry in your dictionary.
#                 For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

def add_dict2(info):
    stock = input("Please enter a stock name to add: ")
    price = int(input("Please enter a price to add: "))
    if stock in info:
        info[stock].append(price)
    else:

        info[stock] = [price]
    print_dict2(info)
    return info

while True:
    user = input("What function would you like to do?\n" \
    "1. Print\n" \
    "2. Add\n" \
    "3. Exit: ")
    match user:
        case "Print": print_dict2(stocks)
        case "Add" : stocks = add_dict2(stocks)
        case "Exit" : break

# 3. Write circle_calc() function that takes radius of a circle as an input from user and then 
#    it calculates and returns area, circumference and diameter. You should get these values in your main
#    program by calling circle_calc function and then print them

def circle_calc(radius):
    diameter = 2 * radius
    circumference = diameter * math.pi
    area = math.pi * (radius ** 2)
    return diameter, circumference, area

if __name__ == "__main__":
    radius = 5
    dia, circum, area_circle = circle_calc(5)
    print(f"diameter: {dia}, circumference: {circum}, area: {area_circle}")

