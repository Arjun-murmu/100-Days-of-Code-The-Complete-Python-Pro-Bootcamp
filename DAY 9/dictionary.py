programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "loop": "The action of doing something over and over again."}
# print(programming_dictionary)
# print(programming_dictionary["Bug"])
#Don't used original data type

colors = {
    "apple":"red",
    "pear" : "Green",
    "banana" : "yellow"
}

# print(colors["pear"])
# colors["loop"] = "The action of doing something over and over again.ll"  #Add the dictionaries
# print(programming_dictionary["loop"])
# print(colors["loop"])

# empty_dictionaries = {}
#
# print(empty_dictionaries)
#
# programming_dictionary = {}
# print(programming_dictionary)

#edit an item in a dictionary

# print(programming_dictionary["Bug"])

programming_dictionary["Bug"] = "a month in your computer."
# print(programming_dictionary["Bug"])

#loop through a dictionary

for key in programming_dictionary:
    # print(key)
    print(programming_dictionary[key])

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
