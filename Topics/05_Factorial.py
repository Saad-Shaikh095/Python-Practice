def factorial(n):
    if n < 0:
        return "Factorial of negative number dose not exist"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

n = int(input("Enter a number: "))
print(factorial(n))