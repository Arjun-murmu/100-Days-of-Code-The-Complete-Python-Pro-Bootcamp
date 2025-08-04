from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def w_forward():
    tim.forward(20)
def s_back():
    tim.backward(20)
def left_clock():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def right_clock():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def angle_nine_degree():
    new_heading = tim.heading() + 90
    tim.setheading(new_heading)
def  c_clear():
    tim.clear()
    tim.speed(0)
    tim.penup()
    tim.hideturtle()
    tim.home()
    tim.pendown()
    tim.showturtle()

screen.listen()
screen.onkey(w_forward,"w")  #Forward move
screen.onkey(w_forward,"W")
screen.onkey(s_back,"s")  # Backword move
screen.onkey(left_clock,"a")  #left anti clock wise
screen.onkey(right_clock,"d")  # right clock wise
screen.onkey(angle_nine_degree,"r")
screen.onkey(c_clear,"c")


screen.exitonclick()