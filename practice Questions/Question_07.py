#  Write a function that takes a student’s marks dictionary and checks if any subject mark is less than 40. If yes, print ‘Fail’, else ‘Pass’.

def check_pass_fail(marks_dict):
    for subject, mark in marks_dict.items():
        if mark < 40:
            return "Fail"
    return "Pass"

student_marks = {
    "Math": 75,
    "English": 85,
    "Science": 39   # Example fail
}

print(check_pass_fail(student_marks))
