import turtle as t
import random

screen = t.Screen()
jaga = t.Turtle()

t.colormode(255)
direction = [0,90,180,270]  # North, East, South, West
# color_list = ["deep pink","black","#1E90FF","#0000CD","navy","lime green","orange red","purple","blue violet","indigo"]

jaga.pensize(7)  # current pensize is
jaga.speed(9)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color

for _ in range(200):
    jaga.color(random_color())

    jaga.setheading(random.choice(direction))  # setheading use for the angle
    distance = random.randint(20,30) #distanc between this

    jaga.forward(distance)


screen.exitonclick()