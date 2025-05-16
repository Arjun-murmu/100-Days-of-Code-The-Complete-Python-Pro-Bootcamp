# 1. Nesting if and else

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("Enter your age : "))
#     if age >= 18:
#         print("You pay $12.")
#     else:
#         print("You pay $7.")
# else:
#     print("Sorry you have to grow taller before you can ride.")

#2. if/elif/else
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("Enter your age : "))
#     if age <= 12:
#         print("You give $5.")
#     elif age <= 18:
#         print("You give $7")
#     else:
#         print("you give $12.")
# else:
#     print("Sorry you have to grow taller before you can ride.")

#3. BMI Calculator with Interpretations . Body mass index (BMI)
weight = 85
height = 2.15
bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")


