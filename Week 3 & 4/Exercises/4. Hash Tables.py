# class HashTable:  
#     def __init__(self):
#         self.MAX = 100
#         self.arr = [None for i in range(self.MAX)]
        
#     def get_hash(self, key):
#         hash = 0
#         for char in key:
#             hash += ord(char)
#         return hash % self.MAX
    
#     def __getitem__(self, index):
#         h = self.get_hash(index)
#         return self.arr[h]
    
#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         self.arr[h] = val    

# # # Exercise: Hash Table

# # 1. [nyc_weather.csv] contains new york city weather for first few days in the month of January.
# #  Write a program that can answer following,

# hash_table = HashTable()
# file = open("D:\\Codes\\ai-engineer-roadmap-2025\\Week 3 & 4\\Exercises\\nyc_weather.csv","r")
# file.readline()
# for line in file:
#     date, temp = line.strip().split(",")
#     temp = float(temp)
#     hash_table.__setitem__(date, temp)

# file.close()

# #     1. What was the average temperature in first week of Jan

# for i in range(1,8):
#     date = "Jan "+str(i)
#     print(hash_table.__getitem__(date))

# #     1. What was the maximum temperature in first 10 days of Jan
# max_temp = 0
# for i in range(1,11):
#     date = "Jan "+str(i)
#     temp = hash_table.__getitem__(date)
#     if temp > max_temp:
#         max_temp = temp

# print(max_temp)

# # Figure out data structure that is best for this problem

# # 2. [nyc_weather.csv] contains new york city weather for first few days in the month of January.
# #  Write a program that can answer following,

# #     1. What was the temperature on Jan 9?
# print(hash_table.__getitem__("Jan 9"))
# #     1. What was the temperature on Jan 4?
# print(hash_table.__getitem__("Jan 4"))


# # Figure out data structure that is best for this problem

# # 3. [poem.txt] Contains famous poem "Road not taken" by poet Robert Frost.
# #  You have to read this file in python and print every word and its count as show below.
# #  Think about the best data structure that you can use to solve this problem and 
# # figure out why you selected that specific data structure.
# # I used a hash table because it can store unique occurunces of key value pairs.

# #  'diverged': 2,
# #  'in': 3,
# #  'I': 8

# file = open("D:\\Codes\\ai-engineer-roadmap-2025\\Week 3 & 4\\Exercises\\poem.txt","r")
# words = file.read().split(" ")
# hash_table = HashTable()
# for word in words:
#     count = hash_table.__getitem__(word)
#     if count:
#         hash_table.__setitem__(word, count+1) 
#     else:
#         hash_table.__setitem__(word,1)
# done = []
# for word in words:
#     if word not in done:
#         done.append(word)
#         print(word,":", hash_table.__getitem__(word))

# class HashTable:  
#     def __init__(self):
#         self.MAX = 10
#         self.arr = [[] for i in range(self.MAX)]
        
#     def get_hash(self, key):
#         hash = 0
#         for char in key:
#             hash += ord(char)
#         return hash % self.MAX
    
#     def __getitem__(self, key):
#         arr_index = self.get_hash(key) # get the hash of the key 
#         for kv in self.arr[arr_index]: # For each element(key,value) in the hash row
#             if kv[0] == key: # If the key in the array matches the parameter passed
#                 return kv[1] # return value
            
#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         found = False
#         for idx, element in enumerate(self.arr[h]):
#             # Iterate over each element(key,value) in the hash row of the array
#             # Each element is assigned an index
#             if len(element)==2 and element[0] == key: # If the key in the element matches the parameter
#                 self.arr[h][idx] = (key,val) # Assign the value to the idx element of the row
#                 found = True
#         if not found: # If element was not found
#             self.arr[h].append((key,val))
        
#     def __delitem__(self, key):
#         arr_index = self.get_hash(key) # get the hash of the key
#         for index, kv in enumerate(self.arr[arr_index]): 
#             # Iterate over each element(key,value) in the hash row of the array
#             # Each element is assigned an index
#             if kv[0] == key: # If the key in the element matches the parameter passed
#                 print("del",index)
#                 del self.arr[arr_index][index] # delete the element
        

# 4. Implement hash table where collisions are handled using linear probing. 
# We learnt about linear probing in the video tutorial. 
# Take the hash table implementation that uses chaining and modify methods to use **linear probing**.
#  Keep MAX size of arr in hashtable as 10.

# class HashTable:  
#     Linear Probing
#     def __init__(self):
#         self.MAX = 10
#         self.arr = [None for i in range(self.MAX)]
        
#     def get_hash(self, key):
#         hash = 0
#         for char in key:
#             hash += ord(char)
#         return hash % self.MAX
    
#     def __getitem__(self, index):
#         h = self.get_hash(index)
#         while self.arr[h][0] != index:
#             h = (h+1) % self.MAX # Change the hash to a new index
#         return self.arr[h]
    
#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         while self.arr[h] != None: # If an element already exists at that hash
#             if self.arr[h][0] == key: # Element found
#                 self.arr[h] = (key,val)
#                 return None
#             h = (h+1) % self.MAX # Change the hash to a new index

#         self.arr[h] = (key,val)
        
            
    
#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         while self.arr[h][0] != key: # While the key of the current element is not equal to the parameter
#             h += (h+1) % self.MAX
#         del self.arr[h]



class HashTable:  
    def __init__(self):
        self.MAX = 10 # I am keeping size very low to demonstrate linear probing easily but usually the size should be high
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key) # get the hash of the key
        if self.arr[h] is None: # if the element at the hash is empty
            return
        prob_range = self.get_prob_range(h) # returns the range of the possible probes
        for prob_index in prob_range: # iterates over the range
            element = self.arr[prob_index]
            if element is None: # if there is an empty element present
                return
            if element[0] == key: # Element found
                return element[1]
           
    def __setitem__(self, key, val):
        h = self.get_hash(key) # get the hash of the key
        if self.arr[h] is None: # if there is an empty element at the hash
            self.arr[h] = (key,val)
        else:  # if no empty space
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key,val) # assign the key, value to the array the the new_hash index
        print(self.arr)
        
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]
        # returns the range of possible probes from index until the final index and from 0 till index
        # e.g for index = 5 returns [5,6,7,8,9]+[0,1,2,3]
    
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index) # returns the range of possible probes
        for prob_index in prob_range: # iterates over the probes
            if self.arr[prob_index] is None: # if an empty element is found
                return prob_index
            if self.arr[prob_index][0] == key: # if an existing element with the matching hash is found
                return prob_index
        raise Exception("Hashmap full") # if no element found
        
    def __delitem__(self, key):
        h = self.get_hash(key) # get the hash of the key
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None: # if element not found
                return # item not found so return nothing. You can also throw exception
            if self.arr[prob_index][0] == key: # if element found
                self.arr[prob_index]=None
        print(self.arr)


hash_table = HashTable()
file = open("D:\\Codes\\ai-engineer-roadmap-2025\\Week 3 & 4\\Exercises\\nyc_weather.csv","r")
file.readline()
for line in file:
    date, temp = line.strip().split(",")
    temp = float(temp)
    print(hash_table.get_hash(date))
    hash_table.__setitem__(date, temp)

print(hash_table.__getitem__("Jan 9"))
print(hash_table.__getitem__("Jan 10"))
hash_table.__setitem__("Jan 10", 36.0)
print(hash_table.__getitem__("Jan 10"))
hash_table.__delitem__("Jan 10")