def check_number(n):
    if n < 0:
        return "Negative"
    elif n == 0:
        return "Zero"
    elif n > 0:
        return "Positive"
    else:
        return "Invalid Input"
    
n = int(input("Enter a number: "))
print(check_number(n))