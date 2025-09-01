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

def rose_bloom(x, y, size=1.0):
    """Draw a simple rose bloom with layered petals."""
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

def draw_stem_with_leaves(x, y, length=200):
    """Draw a green stem with two leaves attached."""
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
    t.circle(20, 90)
    t.left(90)
    t.circle(20, 90)
    t.end_fill()

    # Move down a bit
    t.right(135)
    t.forward(60)

    # Second leaf
    t.begin_fill()
    t.left(45)
    t.circle(20, 90)
    t.left(90)
    t.circle(20, 90)
    t.end_fill()

    t.pensize(1)

# ----- roses -----
rose_bloom(-120, 30, size=1.2)

# ----- stem with leaves -----
draw_stem_with_leaves(-120, 30, length=200)
