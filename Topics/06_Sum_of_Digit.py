def sum_of_digit(n):
    total = 0
    while n > 0:
        digit = n % 10 
        total += digit 
        n = n // 10
    return total 

n = int(input("Enter a number: "))
print(sum_of_digit(n))