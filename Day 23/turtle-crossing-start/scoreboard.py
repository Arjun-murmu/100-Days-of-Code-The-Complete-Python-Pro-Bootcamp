from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        # self.update_scoreboard()
        self.write(f"Level {self.level} ",align=ALIGNMENT,font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level} ", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        # self.update_scoreboard()
        self.clear()
        self.write(f"Level {self.level} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)