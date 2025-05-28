# You have a football field that is 92 meter long and 48.8 meter wide. 
# Find out total area using python and print it.
length = 92
width = 48.8
area = length * width
print(f"Area is: {area} m^2")


# You bought 9 packets of potato chips from a store.
# Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar.
#  Find out using python, how many dollars is the shopkeeper going to give you back?
num_packets = 9
packet_price = 1.49
cash_given = 20
total = num_packets * packet_price
change = cash_given - total
print("Your change is:", change)


# You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
#  If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
#  Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
length = 5.5
area = length ** 2
tile_price = 500
price = tile_price * area
print("The total price is: "+str(price))

# Print binary representation of number 17
num = 17
print("The binary representation of 17 is:",format(num,'b'))
