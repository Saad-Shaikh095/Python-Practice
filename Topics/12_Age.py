def age(n):
    if n < 0:
        return "Invalid Input"
    elif n < 18:
        return "Minor"
    elif n > 18 and n < 60:
        return "Adult"
    elif n >= 60:
        return "Senior Citizen"
    else:
        return "Invalid Input"

n = int(input("Enter your age: "))
print(age(n))