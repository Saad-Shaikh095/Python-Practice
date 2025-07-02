# Write a function that takes a number n and prints all even numbers from 1 to n (inclusive).

def print_even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

n = int(input("Enter a number: "))            
print_even_numbers(n)