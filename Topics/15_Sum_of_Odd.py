def sum_odd():
    total = 0 
    for i in range(1, 51):
        if i % 2 != 0:
            total += i
    print(total)  
sum_odd()