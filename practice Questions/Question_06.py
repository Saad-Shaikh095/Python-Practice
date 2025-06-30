# Write a function to find the average of marks [85, 90, 78, 92, 88].

def average_marks():
    marks = [85, 90, 78, 92, 88]
    avg = sum(marks) / len(marks)
    return avg

print(average_marks())