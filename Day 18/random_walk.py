from turtle import Turtle,Screen
import random

jaga = Turtle()
direction = [0,90,180,270]  # North, East, South, West
color_list = ["deep pink","black","#1E90FF","#0000CD","navy","lime green","orange red","purple","blue violet","indigo"]
jaga.pensize(8)  # current pensize is

for _ in range(200):
    jaga.speed(9)
    """“fastest”: 0

    “fast”: 10

    “normal”: 6

    “slow”: 3

    “slowest”: 1

    Speeds from 1 to 10 enforce increasingly faster animation of line drawing and turtle turning."""

    jaga.setheading(random.choice(direction)) # setheading use for the angle
    jaga.color(random.choice(color_list))  # random color choice

    distance = random.randint(20,30) #distanc between this

    jaga.forward(distance)


screen = Screen()
screen.exitonclick()