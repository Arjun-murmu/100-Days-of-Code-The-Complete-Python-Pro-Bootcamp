import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy level
#Letter.symbol.number
# password = " "

#nr_letter = 4
# 4 0, 1, 2, 3 range(0,4)
# for char in range(1,nr_letters + 1):
#     random_char = random.choice(letters)
#     print(random_char)
#     password = password + random_char
#     password += random.choice(letters)
#     print(password)
#
# for sys in range(1,nr_symbols + 1):
#     random_sys = random.choice(symbols)
#     password += random_sys
#     print(password)
#
# for num in range(1,nr_numbers + 1):
#     password += random.choice(numbers)
#     print(password)
#############
# for char in range(0,nr_letters):
#     random_char = random.choice(letters)
#     #print(random_char)
#     password = password + random_char
#     password += random.choice(letters)
#     #print(password)
#
# for sys in range(0,nr_symbols):
#     random_sys = random.choice(symbols)
#     password += random_sys
#     #print(password)
#
# for num in range(0,nr_numbers):
#     password += random.choice(numbers)
    # print(password)

# print(password)


#Hard Level Password :

#letter.symbol.number.letter.symbol.number...
password_list = []
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))

for sys in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

for num in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

# print(password_list)
random.shuffle(password_list)  #shuffle use for random place
# print(password_list)

password = " "
for char in password_list:
    password += char
print(f"Your password is : {password}")
#unpredictible
