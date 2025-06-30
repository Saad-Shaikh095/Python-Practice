# Write a function to accept 5 student names and store them in a list.

def students():
    names = []
    for i in range(5):
        name = input(f"Enter student name: {i + 1} ")
        names.append(name)
    return names

print(students())