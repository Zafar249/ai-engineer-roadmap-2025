# ## Exercise: Sets and Frozen Sets
# Sets are unordered collections of unique elements

numbers = set([1, 2, 3, 4, 2, 1])
numbers.add(5)
print(numbers)

# 1. create any set anf try to use frozenset(setname)
numbers = [1, 2, 3, 2, 2]
frozen = frozenset(numbers)
print(frozen)
# The contents of a frozen set cannot be changed

# 2. Find the elements in a given set that are not in another set

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

#     diffrence between set1 and set2 is {1,2,3}

print(set1 | set2)  # Union of two sets
print(set1 & set2)  # Intersection of two sets
print(set1 - set2)  # Difference between two sets
print(set1 < set2)  # Whether Set1 is a subset of set 2



