# Write a function remove_even_numbers(nums) that takes a list of numbers and returns a new list with only the odd numbers.

def remove_even_number(nums):
    odd_nums = []
    for num in nums:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums

print(remove_even_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

