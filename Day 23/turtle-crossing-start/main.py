import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manage = CarManager()
scoreboard =Scoreboard()


screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manage.create_car()
    car_manage.car_move()

    #Detect collision with car
    for car in car_manage.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.at_a_end():
        player.go_to_start()
        car_manage.level_increase()
        scoreboard.increase_level()
        # scoreboard.update_scoreboard()

screen.exitonclick()