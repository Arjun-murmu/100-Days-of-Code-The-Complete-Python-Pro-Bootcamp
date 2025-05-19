def three_time_r():
    turn_left()
    turn_left()
    turn_left()
def move_continue():
    turn_left()
    move()
    three_time_r()
    move()
    three_time_r()
    move()
    three_time_r()
    turn_left()
    turn_left()

while not at_goal():
    if wall_in_front():
        move_continue()
    else:
        move()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
