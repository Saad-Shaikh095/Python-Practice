def is_amstrong(n):
    original = n
    total = 0 
    while n > 0:
        digit = n % 10 
        total += digit **3
        n = n // 10

    return total == original 
n = int(input("Enter a number: "))

if is_amstrong(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")