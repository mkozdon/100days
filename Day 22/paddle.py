from turtle import Turtle

STEP = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        if position == "right":
            self.setx(280)
        elif position == "left":
            self.setx(-280)
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        if self.ycor() < 240:
            self.sety(self.ycor() + STEP)

    def move_down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - STEP)

    def track_ball(self, ball_ycor):
        if ball_ycor > self.ycor() + 20:
            self.move_up()
        if ball_ycor < self.ycor() + 20:
            self.move_down()
