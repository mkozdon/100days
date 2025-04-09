from turtle import Screen
from paddle import Paddle
from time import sleep
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
scoreboard = Scoreboard()
paddle = Paddle("left")
cpu_paddle = Paddle("right")
ball = Ball()
screen.listen()
screen.onkey(fun=paddle.move_up, key="Up")
screen.onkeypress(fun=paddle.move_up, key="Up")
screen.onkeypress(fun=paddle.move_down, key="Down")
screen.onkey(fun=paddle.move_down, key="Down")

game_running = True

while game_running:
    screen.update()
    sleep(0.05)
    ball.move()
    ball.check_border_collision()
    ball.check_paddle_collision(paddle, cpu_paddle)
    cpu_paddle.track_ball(ball.ycor())
    result = ball.is_outside()
    if result == 1:
        scoreboard.left_score += 1
        scoreboard.refresh_score()
        ball.restart_position()
    if result == -1:
        scoreboard.right_score += 1
        scoreboard.refresh_score()
        ball.restart_position()
screen.exitonclick()
