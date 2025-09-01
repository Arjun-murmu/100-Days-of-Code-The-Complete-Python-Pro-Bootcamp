import turtle as t

# ----- helpers -----
def jump(x, y, heading=40):
    # t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()

def heart(x, y, size=1.0, color="red"):
    """Draw a heart centered at (x,y)."""
    jump(x, y)
    t.color(color, color)
    t.begin_fill()
    t.setheading(110) # start angle
    t.right(80)
    t.forward(11 * size)            # left side
    t.circle(56 * size, 200)         # left curve
    t.right(110)                     # FIXED (was 110)
    t.circle(56 * size, 200)         # right curve
    t.forward(112 * size)            # right side
    t.end_fill()
    t.setheading(0)                  # reset orientation

def leaf(size=26, fill="green"):
    t.color(fill, fill)
    t.begin_fill()
    t.circle(size, 70)
    t.left(110)
    t.circle(size, 70)
    t.end_fill()

def rose_bloom(radius=18, petals=7, fill="darkred"):
    """Stylized rose using petals around a circle."""
    t.color(fill, fill)
    for i in range(petals):
        t.begin_fill()
        t.circle(radius, 70)
        t.left(110)
        t.circle(radius, 70)
        t.end_fill()
        t.left(360 / petals)

def stem_path(points, width=6, color="green"):
    t.color(color)
    t.pensize(width)
    t.penup()
    t.goto(points[0])
    t.pendown()
    for p in points[1:]:
        t.goto(p)
    t.pensize(1)

# ----- canvas -----
t.setup(800, 700)
t.title("I Love You with Rose")
t.bgcolor("white")
t.speed(0)
t.hideturtle()

# ----- draw single heart -----
heart(120, 0, size=2.0, color="red")  # y change

# ----- text -----
jump(-40, 40)
t.color("white")
t.write("I Love You", align="center", font=("Arial", 40, "bold"))

# ----- roses -----
jump(-120, 30)
rose_bloom(radius=18, petals=8, fill="darkred")

# ----- stem -----
stem_points = [(-120, 30), (80, -80), (0, 140)]
stem_path(stem_points, width=6)

# ----- leaves -----
jump(-40, -100, heading=20)
leaf(size=20, fill="green")

jump(-10, 130, heading=200)
leaf(size=20, fill="green")

t.done()
