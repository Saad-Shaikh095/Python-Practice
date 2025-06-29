'''
Given a tuple my_tuple = (10, 20, 30, 40, 50), write Python code to:
    1.  Print the first and last elements.
    2. Convert it into a list and add the number 60.   
'''

my_tupple = (10, 20, 30, 40, 50)

# 1.
print("First: ", my_tupple[0])
print("Last: ", my_tupple[4])

# 2. 
my_list = list(my_tupple)
my_list.append(60)
print(my_list)
