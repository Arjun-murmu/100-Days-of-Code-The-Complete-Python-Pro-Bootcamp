# age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.")
try:
    age = int(input("How old are you?"))
except  ValueError:
    print("You have in an invalid number.plz try against with a numberical response such as 15.")
    age = int(input("How old are you ? "))
if age > 18:
    print(f"You can drive at age {age}.")
