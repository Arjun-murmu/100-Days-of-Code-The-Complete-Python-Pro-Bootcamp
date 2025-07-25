from itertools import accumulate
from random import choice

import art
def add(n1, n2):
    return n1 + n2

#TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
#TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

#TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

# print(operator["*"](4,8))

# first_number = float(input("What is the first number?:  "))
# for symbol in operators:
#     print(symbol)
# pick_symbol = input("Pick an operators: ")
# second_number = float(input("What is the second number?: "))
# result = operators[pick_symbol](first_number,second_number)
#
# print(f"{first_number} {pick_symbol} {second_number} = {result.round(2)}")


def calculator():
    print(art.logo)
    should_accumulate = True
    first_number = float(input("What is the first number?:  "))

    while should_accumulate:
        for symbol in operators:
            print(symbol)
        pick_symbol = input("Pick an operators: ")
        second_number = float(input("What is the second number?: "))
        result = operators[pick_symbol](first_number,second_number)

        print(f"{first_number} {pick_symbol} {second_number} = {result}")

        choice = input(f"""Type "y" to continue calculating with {result}, or type "n" to start a new calculation :  """).lower()

        if choice == "y":
            first_number = result
        else:
            should_accumulate = False
            print("/n" *20)
            calculator()

# print(add(2, multiply(5, divide(8, 4))))
calculator()
