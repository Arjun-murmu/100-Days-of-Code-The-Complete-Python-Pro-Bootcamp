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

#number_of_hurdles = 6
#while number_of_hurdles > 0:
    #move_continue()
    #number_of_hurdles -= 1
    #print(number_of_hurdles)
    #if at_goal():
        
while not at_goal():
    move_continue()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
