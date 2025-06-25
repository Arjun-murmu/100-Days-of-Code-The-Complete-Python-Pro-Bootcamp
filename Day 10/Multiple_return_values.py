def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
#Storing output in a variable
# formatted_name = format_name(input("Your first name: "), input("Your last name: "))
# print(formatted_name)
# or printing output directly
# print(format_name(input("What is your first name? "), input("What is your last name? ")))

# #Already used functions with outputs.
# length = len(formatted_name)
# print(length)
# print(formatted_name)

#Return as an early exit
def format_name(f_name, l_name):
  """Take a first and last name and format it
  to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"

print(format_name("AnGEla", "YU"))
print(format_name(f_name="Arjun",l_name="murmu"))
print(format_name(f_name="",l_name=""))


word_to_num = {
    "zero": 0, "one": 1, "two": 2, "three": 3,
    "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9
}

# age = word_to_num.get("nine")  # ✅ Returns: 9

#condition return
def canBuyAlcohol(age):
    if age > 18:
        return True
    else:
        return False

# print(canBuyAlcohol(39))
# print(canBuyAlcohol(15))

#Empty Returns
def canBuyAlcoholl(age):
    if type(age) != int:
        return "This is String"
    if age < 18:
        return  True
    else:
        return False
# print(canBuyAlcoholl("nine"))
# print(canBuyAlcoholl(39))
# print(canBuyAlcoholl(15))

def canBuy_Alcoholl(age):
    try:
        age = int(age)
    except ValueError:
        return "Invalid input: age must be a number."

    if age < 18:
        return False
    else:
        return True

# Testing
# age = word_to_num.get("nine five")
# print(canBuy_Alcoholl(age))
# print(canBuy_Alcoholl("nine"))  # Invalid input
# print(canBuy_Alcoholl("45"))
# print(canBuy_Alcoholl(39))      # True
# print(canBuy_Alcoholl(15))      # False

def canBuy_Alcoho(age):
    if type(age) != int:
        type_convert = int(age)
        if type_convert < 18:
            return False
        else:
            return True

    else:
        if age < 18:
            return False
        else:
            return True
# age = word_to_num.get("nine")
# print(canBuy_Alcoho(age))
# print(canBuy_Alcoho("45"))
# print(canBuy_Alcoho(39))
# print(canBuy_Alcoho(15))
