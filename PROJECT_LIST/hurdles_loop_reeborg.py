def three_time_r():
    turn_left()
    turn_left()
    turn_left()
def move_continue():
    move()
    turn_left()
    move()
    three_time_r()
    move()
    three_time_r()
    move()
    three_time_r()
    turn_left()
    turn_left()

for step in range(6):
    move_continue()
#move_continue()
#move_continue()
#move_continue()
#move_continue()
#move_continue()
#move_continue()


