# From Day 16 onwards, you will be creating your own PyCharm projects from scratch.
# Instead of using templates that I have created for you.
# It will be another step in your journey as a developer!
# But don't worry, I will explain how to do everything in the video tutorials on Udemy.
import turtle

from arjun import name
# print(name)

from turtle import Turtle,Screen
# print(Turtle)

# timmy = turtle.Turtle()  # attributes
# print(timmy)

# Object and attributes

# my_screen = turtle.Screen()  #when not import screen
# print(my_screen)

my_screen = Screen()
# print(my_screen.canvwidth)  #(Weight of the board)

#Object Method    #car.speed()

timmy = Turtle()
timmy.shape("turtle")
# timmy.color("red")  #color give the image
timmy.color("#285078")
# timmy.forward(100)
# timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.right(120)
timmy.forward(100)

# for steps in range(50):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)

my_screen.exitonclick()  # create white board and when click off the board and code run stop


