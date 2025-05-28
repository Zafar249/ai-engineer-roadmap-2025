# ## Exercise: Iterators

students = ["Maarij", "Soman", "Ashmal"]
itr = iter(students)  # Creates an iterable object of the array
print(itr.__next__()) # Iterates over the first element
print(itr.__next__())

itr = reversed(students)  # Creates an iterable object of the array in reverse order
print(itr.__next__())  # Iterates over the last element
print(itr.__next__())

# 1. Create an iterator for fibonacci series in such a way that each next returns
#  the next element from fibonacci series.

# class Fibonacci:
#     def __init__(self):
#         self.sequence = [1,1,2,3,5,8,13]
#         self.index = -1
#         self.limit = 5

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.index += 1
#         if self.index < self.limit:
#             return self.sequence[self.index]


# 2. The iterator should stop when it reaches a `limit` defined in the constructor.

# fibonacci = Fibonacci()
# itr = iter(fibonacci)
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())


class Fibonacci:
    def __init__(self):
        self.limit = 5
        self.current = 1
        self.previous = 0
        self.n = 0
    
    def __iter__(self):  # Returns self as an iterator object to iterate over
        return self
    
    def __next__(self):
        if self.n < self.limit:
            result = self.previous + self.current
            self.previous = self.current
            self.current = result 
            self.n += 1
            return result
        
        else:
            raise StopIteration

fibonacci = Fibonacci()
itr = iter(fibonacci)  # Assigns an iterator object
while True:
    try:
        print(itr.__next__())
    except StopIteration:
        break