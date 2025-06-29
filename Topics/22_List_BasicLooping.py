list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in list:
    print(n)

even = [n for n in list if n % 2 == 0]
print(even)

odd = [n for n in list if n % 2 != 0]
print(odd)