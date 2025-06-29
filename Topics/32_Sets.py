# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Adding element in a set
my_set.add(100)
print(my_set)

# Removing an element from a set
my_set.remove(5)
print(my_set)

# Checking length of the set 
print(len(my_set))

print("----------------------------------------------------------------------")

# Basic Set Operations:-
A = {2, 3, 4, 6, 7, 8, 10}
B = {1, 2, 3, 5, 6, 7, 9}

# 1. Union: Combines elements
print("Union: ", A | B)

# 2. Intersection: Common elements
print("Intersection: ", A & B)

# 3. Difference: Elements in A but not in B
print("Difference: ", A - B)