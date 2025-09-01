# # This is a sample Python script.
#
# # Press Ctrl+F5 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# import random
# name = ["arjun","beauty","muna","jaga"]
# student_score = {student:random.randint(35,100) for student in name}
# print(student_score)
# # {'arjun': 85, 'beauty': 74, 'muna': 66, 'jaga': 58}
# passed_student = {student:mark for (student,mark) in student_score.items() if mark > 60}
# print(passed_student)
# # {'arjun': 85, 'beauty': 74, 'muna': 66}
#
# # {'arjun': 84, 'beauty': 100, 'muna': 80, 'jaga': 55}
# # {'arjun': 84, 'beauty': 100, 'muna': 80}
#

# student_dict = {
#     'arjun': 84,
#     'beauty': 100,
#     'muna': 80,
#     'jaga': 55
# }
#looping through dict
# for (key,value) in student_dict.items():
#     # print(key)
#     print(value)
#
student_dict = {
    "student" : ["arjun","beauty","muna","jaga"],
    "score" : [84,100,80,55]
}
#
# #looping through dict
# for (key,value) in student_dict.items():
#     if key == "score":  # Check if the current key is "score"
#         print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key,value) in student_data_frame.items():
    # print(key)
    # print(value)

#loop through rows of data frame
for (key,value) in student_data_frame.iterrows():
    # print(key)
    # print(value)
    # print(value.student)
    # print(value.score)
    if value.student == "arjun":
        print(value.score)