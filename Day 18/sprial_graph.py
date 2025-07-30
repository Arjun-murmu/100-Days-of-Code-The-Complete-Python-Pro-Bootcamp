import turtle as t
import random

screen = t.Screen()
mu = t.Turtle()
t.colormode(255)
mu.speed(0)
# mu.pensize(2)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color

# print(mu.heading())
# for _ in range(200):
#     mu.color(random_color())
#     mu.circle(100)
#     current_heading = mu.heading()
#     mu.setheading(current_heading + 10)
#     mu.circle(100)

def draw_sprial_graph(sizeof_gap):
    for _ in range(int(360 / sizeof_gap)):
        mu.color(random_color())
        mu.circle(100)
        mu.setheading(mu.heading() + sizeof_gap)

draw_sprial_graph(5)


# mu.circle(120, 180)  # Semi circle
mu.heading()

screen.exitonclick()