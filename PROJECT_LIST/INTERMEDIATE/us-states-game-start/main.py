import turtle
from turtle import Turtle,Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# print(answer_state)

data = pandas.read_csv("50_states.csv")
# print(data)
all_state = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 State Correct", prompt="What's another state's name ?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        # print(missing_state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_learn.csv")
        break
    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        data_x = data[data.state == answer_state].x
        data_y = data[data.state == answer_state].y
        t.goto(data_x.item(), data_y.item())
        # t.write(state_data.state.item())
        t.write(answer_state)


# def get_mouse_click_cool(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cool)

# turtle.mainloop()

# screen.exitonclick()