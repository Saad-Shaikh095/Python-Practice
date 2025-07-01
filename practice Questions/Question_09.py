# Write a program that prints all numbers from 1 to 20, but only those divisible by 3.

def divisible():
    
    for i in range(1, 21):
        if i % 2 != 0:
            print(i)  
divisible()