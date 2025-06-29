num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))

print(f"Before Swapping: num1 = {num1}, num2 = {num2}")

num1, num2 = num2, num1 # Swapping the values

print(f"After Swapping: num1 = {num1}, num2 = {num2}")