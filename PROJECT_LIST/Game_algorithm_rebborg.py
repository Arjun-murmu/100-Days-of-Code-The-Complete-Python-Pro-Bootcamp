#link of implement: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
#link of reborg's : https://reeborg.ca/docs/en/#
def move_forw():
    for col in range(0,9):
        move()

def turn_around():
    turn_left()
    turn_left()
    turn_left()

def one_move():
    turn_left()
    move()
    turn_left()

turn_left()
move_forw()
turn_around()
move_forw()
turn_around()
move()
turn_around()
move_forw()
one_move()
move_forw()
turn_around()
move()
turn_around()
move_forw()
one_move()
move_forw()
turn_around()
move()
turn_around()
move_forw()
one_move()
move_forw()
turn_around()
move()
turn_around()
move_forw()
one_move()
move_forw()
turn_around()
move()
turn_around()
move_forw()
