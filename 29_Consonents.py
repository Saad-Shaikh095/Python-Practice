def count_consonants(s):
    vowels = 'aeiou'
    count = 0

    for char in s.lower():
        if char.isalpha() and char not in vowels:
            count += 1

    return count

s = input("Enter a string: ")
print(count_consonants(s))
