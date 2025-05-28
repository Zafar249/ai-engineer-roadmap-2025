# Hash Tables are called dictionaries in python.
# Hash table is a data structure that stores unqiue key : value pairs.
# Each Key/value pair is known as an Entry.
# Hashing takes a key and computes an integer (formula will vary based on key and data type)
# index = key.hashCode() %(modulus) capacity(length)
# Bucket is an indexed storage location for one or more Entries.
# A bucket can store multiple entries in case of a collision (using a linked list)
# A Collision occurs when a hash functions generates the same index for more than one key.
# Time Complexity : Best Case O(1)
#                   Worst Case O(n)

table = {1:"Maarij",
         2:"Soman",
         3:"Ashmal"}

table.pop(2)
for key,value in table.items():
    print(value)