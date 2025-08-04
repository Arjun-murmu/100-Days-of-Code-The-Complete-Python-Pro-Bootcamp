from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def click_forward():
    tim.forward(20)

screen.listen()
screen.onkey(key="space", fun=click_forward)   #"space" space key s most be small letter
# tim.forward(10)

def up():
    tim.fd(20)
    tim.rt(20)
screen.onkey(up,"Up")

def down():
    tim.fd(20)
    tim.lt(30)
screen.onkey(down,"Down")

screen.exitonclick()