import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
speed = 0.2

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
car_manager.generate_starting_cars(20)
screen.listen()
screen.onkey(fun=player.move, key="Up")
game_is_on = True


while game_is_on:
    time.sleep(speed)
    car_manager.generate_random_car()
    car_manager.move_cars()
    if car_manager.check_collisions(player):
        print("over")
        scoreboard.game_over()
        game_is_on = False
    if player.level_up():
        player.reset_position()
        scoreboard.increase_level()
        speed *= 0.8
    screen.update()
screen.exitonclick()
