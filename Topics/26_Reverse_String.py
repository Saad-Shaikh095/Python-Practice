def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

s = input("Enter a string: ")
print(reverse_string(s))
