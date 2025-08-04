from turtle import Turtle, Screen
import random


screen = Screen()

#color lisr
color = ["red","orange","yellow","green","blue","purple"]


screen.setup (width=500, height=400)  # Size define
# user_bet = screen.textinput(title="Make your bet ",prompt="which tutle will win the race ? Enter a color : ")

is_race = False
position_t = [-80,-40,0,40,80,120]
all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=position_t[turtle_index])
    all_turtle.append(new_turtle)
# print(all_turtle)

user_bet = screen.textinput(title="Make your bet ",prompt="which tutle will win the race ? Enter a color : ")

if user_bet in color:
    is_race = True
else:
    is_race = False
    print("Wrong color you choice.")

while is_race:
    for turtle in all_turtle:
        if turtle.xcor() > 220:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win ! The {winning_color} turtle is the winner😎.")
            else:
                print(f"You'r lost 😔! The winner is {winning_color}.")

        new_distance = random.randint(0, 10)
        turtle.forward(new_distance)







screen.listen()
screen.exitonclick()


#Turtle list
# red_turtle = Turtle(shape="turtle")
# orange_turtle = Turtle(shape="turtle")
# yellow_turtle = Turtle(shape="turtle")
# green_turtle = Turtle(shape="turtle")
# blue_turtle = Turtle(shape="turtle")
# purple_turtle = Turtle(shape="turtle")
#
# def each_turtle():
#     red_turtle.goto(x=-230,y=-120)
#     orange_turtle.goto(x=-230,y=-80)
#     yellow_turtle.goto(x=-230,y=-40)
#     green_turtle.goto(x=-230,y=0)
#     blue_turtle.goto(x=-230,y=40)
#     purple_turtle.goto(x=-230,y=80)

# each_turtle()
