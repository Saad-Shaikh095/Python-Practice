# Write a function common_elements(set1, set2) that takes two sets and returns a new set with only elements common to both.

def common_elements(set1, set2):
    return set1 & set2

print(common_elements({1, 2, 3, 4, 5}, {3, 4, 5, 6, 7, 8, 9}))
