from operator import index
from turtle import Turtle,Screen
import random

tim = Turtle()
tim.color("red")

# #triagnle
# for _ in range(3):
#     tim.forward(100)
#     tim.left(120)
#
# #Square
# for _ in range(4):
#     tim.color("yellow")
#     tim.forward(100)
#     tim.left(90)
#
# #pentagon
# for _ in range(5):
#     tim.color("blue")
#     tim.forward(100)
#     tim.left(72)
#
# #hexagon
# for _ in range(6):
#     tim.color("deep pink")
#     tim.forward(100)
#     tim.left(60)
#
# #heptagon
# for _ in range(7):
#     tim.color("green")
#     tim.forward(100)
#     tim.left(51.43)
#
# #octagon
# for _ in range(8):
#     tim.color("midnight blue")
#     tim.forward(100)
#     tim.left(45)
#
# #nonagon
# for _ in range(9):
#     tim.color("orange red")
#     tim.forward(100)
#     tim.left(40)
#
# #decagon
# for _ in range(10):
#     tim.color("indigo")
#     tim.forward(100)
#     tim.left(36)

color_list = ["deep pink","black","#1E90FF","#0000CD","navy","lime green","orange red","purple","blue violet","indigo"]
# print(color_list[0])

#Print all the using loop
def formula_math(angle):
    form = (angle-2)*180
    formal = form/angle
    angle = 180-formal
    return angle
def print_patten(n):
    for _ in range(n):
        tim.forward(100)
        tim.left(formula_math(n))

# tim.forward(100)
for i in range(3,10):
    tim.color(random.choice(color_list))
    print_patten(i)

#Type 2:
def draw_shape(new_side,color):
    angle = 360/new_side
    tim.color(color)
    for _ in range(new_side):
        tim.forward(100)
        tim.right(angle)


for shape in range(3,10):
    # tim.color(random.choice(color_list))
    draw_shape(shape,color_list[index(shape)])



screen = Screen()
screen.exitonclick()