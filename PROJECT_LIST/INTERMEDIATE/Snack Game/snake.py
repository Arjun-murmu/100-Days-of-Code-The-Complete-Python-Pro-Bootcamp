from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Create a Snack
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        # new_segment.shapesize(stretch_len=1,stretch_wid=1)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        # Move Forward snack
        for new_seg in range(len(self.segments) - 1, 0, -1):
            position_x = self.segments[new_seg - 1].xcor()
            position_y = self.segments[new_seg - 1].ycor()
            self.segments[new_seg].goto(position_x, position_y)

        self.head.forward(MOVE_DISTANCE)
        # self.segments[0].forward(MOVE_DISTANCE)
        # self.segments[0].left(90)

    def up(self):
        # if self.segments[0].heading() != DOWN:
        #     self.segments[0].setheading(UP)
        # self.head.setheading(90)
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

        # if self.segments[0].heading() != UP:
        #     self.segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

        # if self.segments[0].heading() != RIGHT:
        #     self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

        # if self.segments[0].heading() != LEFT:
        #     self.segments[0].setheading(RIGHT)

