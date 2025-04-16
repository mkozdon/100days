from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=snake.go_left, key="Left")
screen.onkey(fun=snake.go_right, key="Right")
screen.onkey(fun=snake.go_up, key="Up")
screen.onkey(fun=snake.go_down, key="Down")

game_running = True

while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.body[0].distance(food) < 15:
        snake.add_segment()
        food.refresh()
        scoreboard.increase_score()

    if (
        snake.body[0].xcor() > 280
        or snake.body[0].xcor() < -280
        or snake.body[0].ycor() > 280
        or snake.body[0].ycor() < -280
    ):
        scoreboard.reset()
        snake.reset()
        # scoreboard.game_over()
        # game_running = False

    if snake.is_self_collision():
        # scoreboard.game_over()
        # game_running = False
        scoreboard.reset()
        snake.reset()
screen.exitonclick()
