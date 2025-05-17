import random

#import my_module
# random_integer = random.randint(1,9)
# print(random_integer)
# userno = int(input("Enter a number : "))
# if random_integer == userno:
#     print("tu mor payi heyichu.")

#my_module call
# print(my_module.name) #Arjun Murmu.
# print(my_module.name.lower()) #arjun murmu
# print(my_module.number)
# print(my_module.number.hex()) #0x1.4a8f5c28f5c29p+3
# print(my_module)
# '''Enter your name : Jaga Bhai
# Wow you name is Jaga Bhai
# <module 'my_module' from 'C:\\Users\\murmu\\PycharmProjects\\100 Days of Code -
# The Complete Python Pro Bootcamp\\Day 4\\Random Module\\my_module.py'>'''

#random.random()   0.0 <= X < 1.0
# random_num_0_to_1 = random.random()
# print(random_num_0_to_1)
# print(random_num_0_to_1.__round__(2))

# random_num_0_to_1 = random.random() * 10
# print(random_num_0_to_1)
# print(random_num_0_to_1.__round__(2))

#Random Uniform
#Return a random floating-point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
#expression a + (b-a) * random().
# random_float = random.uniform(1,10)
# print(random_float)
# print(random_float.__round__(4))

#PAUSE 1 (Head and Tail)
toss = random.randint(0,1)
if toss == 1:
    print("Heads")
else:
    print("Tails")
