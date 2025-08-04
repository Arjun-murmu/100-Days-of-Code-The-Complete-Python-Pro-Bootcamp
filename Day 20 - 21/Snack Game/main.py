from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snack Game.")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #Detect collision food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        # snake.extend()
        scoreboard.game_over()
    # Detect collision with the tall
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()




screen.exitonclick()



    #This for loop is only for one segment
    # for seg in segment:
    #     seg.forward(20)

# snack = Turtle("square")
# snack.color("white")
#
# snack = Turtle("square")
# snack.color("white")
# snack.goto(-20,0)
#
# snack = Turtle("square")
# snack.color("white")
# snack.goto(-40,0)
# snack = Turtle("square")
# snack.color("white")
#
