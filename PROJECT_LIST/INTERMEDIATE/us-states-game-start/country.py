import pandas

data = pandas.read_csv("50_states.csv")
print(data)
all_state = data.state.to_list()

user_input = input("Guess the state : ").capitalize()

if user_input in all_state:
    print("you get it")
    data_x = data[data.state == user_input].x
    data_y = data[data.state == user_input].y
    print(data_x.item())
    print(data_y.item())
else:
    print("bhak")