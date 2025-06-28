# Creating a dictionary
my_dict = {
    "Name": "Saad",
    "Age:": 19,
    "City": "Pune"
}

# Printing and Accessing a value
print(my_dict)
print(my_dict["Name"])

# Add or Update a key element 
my_dict["College"] = "Pune University"
print(my_dict)
print(my_dict["College"])

# Remover a key element 
my_dict.pop("City")
print(my_dict)

# Getting Key, Values and items in the dictionary
print(my_dict.keys())     
print(my_dict.values())   
print(my_dict.items())    
