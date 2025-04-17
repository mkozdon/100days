from turtle import Screen
import pandas
from game import Game

DATA_PATH = "Day 25/50_states.csv"
BG_PATH = "Day 25\\blank_states_img.gif"

data = pandas.read_csv(DATA_PATH)
data_dict = dict(zip(data.state, zip(data.x, data.y)))
screen = Screen()
screen.title("U.S. States Game")
screen.setup(width=750, height=450)
screen.bgpic(BG_PATH)
screen.tracer(0)

game_engine = Game(data_dict)
game_is_on = True
while game_is_on:
    game_is_on = game_engine.guess_state()
    screen.update()
screen.exitonclick()
