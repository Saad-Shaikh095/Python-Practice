# Write a Python program to check if a number is even or odd.

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
n = int(input("Enter a number: "))
print(check_even_odd(n))