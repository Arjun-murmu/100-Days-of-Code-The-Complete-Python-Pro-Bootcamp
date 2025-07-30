from operator import index
from turtle import Turtle,Screen
import random

tim = Turtle()
tim.color("red")

color_list = ["deep pink","black","#1E90FF","#0000CD","navy","lime green","orange red","purple","blue violet","indigo"]
# print(color_list[0])
for _ in range(4):
    tim.pensize(4)
    tim.speed(0)
    tim.left(90)
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

    tim.right(180)



screen = Screen()
screen.exitonclick()