def my_function():
    for i in range(1, 20):  # i ranges from 1 to 19 (20 is excluded)
        if i == 20:
            print("You got it")  # This will never execute

my_function()

def my_functions():
    for i in range(1, 20 + 1):  # i ranges from 1 to 20 (inclusive)
        if i == 20:
            print("You got it.")  # This will execute when i == 20

my_functions()

# Describe the Problem - Write your answers as comments:

# 1. What is the for loop doing?
"""The for loop iterates over numbers starting from 1 up to (but not including) 20 in the first function.
In the second function, it iterates from 1 to 20 inclusive by using range(1, 21)."""

# 2. When is the function meant to print "You got it"?
"""It is meant to print "You got it" when the variable `i` becomes 20 inside the loop."""

# 3. What are your assumptions about the value of i?
"""In the first function, i will never be 20, so the condition (i == 20) is never true.
In the second function, i will be 20 in the final iteration, so the message will be printed."""
