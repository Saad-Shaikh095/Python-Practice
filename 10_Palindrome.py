def palindrome(n):
    original = n 
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit 
        n = n // 10 

    return reversed_num == original 

n = int(input("Enter a number: "))
print(palindrome(n))