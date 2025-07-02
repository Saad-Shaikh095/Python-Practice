# Write a function that takes a list of numbers and returns the sum of all positive numbers in the list.

def sum(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total 

print(sum([1, 2, 3, 4, 5, 6]))