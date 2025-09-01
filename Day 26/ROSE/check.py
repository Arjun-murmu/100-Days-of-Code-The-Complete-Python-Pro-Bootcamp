import turtle as t
#
# ---------- Helpers ----------
def jump(x, y, heading=40):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()

def heart(x, y, size=1.0, color="red"):
    """Draw a heart centered at (x,y)."""
    jump(x, y)
    t.color(color, color)
    t.begin_fill()
    t.setheading(110)  # start angle
    t.right(80)
    t.forward(11 * size)            # left side
    t.circle(56 * size, 200)        # left curve
    t.right(110)
    t.circle(56 * size, 200)        # right curve
    t.forward(112 * size)           # right side
    t.end_fill()
    t.setheading(0)                 # reset orientation

def leaf(size=26, fill="green"):
    """Draw a leaf shape"""
    t.color(fill, fill)
    t.begin_fill()
    t.circle(size, 70)
    t.left(110)
    t.circle(size, 70)
    t.end_fill()

# # ---------- Roses ----------
def rose_bloom_layered(x, y, size=1.0):
    """Draw a simple rose bloom with layered petals (from 1st code)."""
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Outer petals
    t.color("darkred", "darkred")
    for angle in range(0, 360, 45):
        t.begin_fill()
        t.circle(20 * size, 90)
        t.left(90)
        t.circle(20 * size, 90)
        t.end_fill()
        t.setheading(angle)

    # Inner swirl (darker center)
    t.color("firebrick", "firebrick")
    for angle in range(0, 360, 90):
        t.begin_fill()
        t.circle(10 * size, 90)
        t.left(90)
        t.circle(10 * size, 90)
        t.end_fill()
        t.setheading(angle)

def rose_bloom_stylized(x, y, radius=18, petals=7, fill="darkred"):    # 2nd flower drawing
    """Stylized rose using petals around a circle (from 2nd code)."""
    jump(x, y)
    t.color(fill, fill)
    for i in range(petals):
        t.begin_fill()
        t.circle(radius, 70)
        t.left(110)
        t.circle(radius, 70)
        t.end_fill()
        t.left(360 / petals)

# # ---------- Stems ----------
def draw_stem_with_leaves(x, y, length=200):
    """Draw a green stem with two leaves attached (from 1st code)."""
    t.penup()
    t.goto(x, y)
    t.setheading(-60)
    t.pendown()
    t.color("green")
    t.pensize(5)
    t.forward(length)

    # First leaf
    t.fillcolor("green")
    t.begin_fill()
    t.left(45)
    t.circle(20, 180)
    t.left(90)
    t.circle(20, 90)
    t.end_fill()

    # Move down a bit
    # t.right(135)
    # t.forward(60)

    # Second leaf
    t.begin_fill()
    t.left(45)
    t.circle(20, 90)
    t.left(90)
    t.circle(20, 90)
    t.end_fill()

    t.pensize(1)

# def stem_path(points, width=6, color="green"):
#     """Draw a curved stem path (from 2nd code)."""
#     t.color(color)
#     t.pensize(width)
#     t.penup()
#     t.goto(points[0])
#     t.pendown()
#     for p in points[1:]:
#         t.goto(p)
#     t.pensize(1)
#
# ---------- Canvas ----------
t.setup(900, 700)
t.title("I Love You with Roses")
t.bgcolor("white")
t.speed(0)
t.hideturtle()

# ---------- Draw Heart ----------
heart(120, 0, size=2.0, color="red")

# ---------- Text ----------
jump(-40, 40)
t.color("white")
t.write("I Love You", align="center", font=("Arial", 40, "bold"))

# # ---------- Roses ----------
rose_bloom_layered(-150, 20, size=1.2)   # layered rose
rose_bloom_stylized(190, 150, radius=18, petals=8, fill="darkred")  # stylized rose
#
# # ---------- Stems ----------
# draw_stem_with_leaves(-145, 20, length=200)  # simple stem with leaves
# stem_points = [(-100, 20), (80, -80), (0, 140)]
# stem_path(stem_points, width=6)
#
# # ---------- Leaves ----------
# jump(-40, -100, heading=20)
# leaf(size=20, fill="green")

# jump(-40, -100, heading=40)
# leaf(size=40, fill="green")

t.done()
