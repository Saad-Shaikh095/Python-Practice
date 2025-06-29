'''
Create a dictionary student with keys Name, Age, and Marks.
    1. Update Marks to a higher value.
    2. Add a new key Passed with value True if Marks ≥ 40.
'''

student = {
    "Name": "Saad",
    "Age": 20,
    "Marks": 35
}

student["Marks"] = 85  # Update marks

if student["Marks"] >= 40:
    student["Passed"] = True
else:
    student["Passed"] = False

print(student)
