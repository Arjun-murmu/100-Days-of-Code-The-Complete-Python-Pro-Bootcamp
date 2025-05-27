student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
def check_grade(score):
    if score < 100 and score > 90:
        return "Outstanding"
    elif score <= 90 and score > 80:
        return "Exceeds Expectations"
    elif score <= 80 and score > 70:
        return "Acceptable"
    else:
        return "Fail"
        
for key in student_scores:
    student_grades[key] = check_grade(student_scores[key])
    print(student_grades[key])
