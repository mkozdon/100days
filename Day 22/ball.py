from turtle import Turtle
import random

STEP = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(-20, 0)
        self.y_angle_randomizer = random.randint(3, 30)
        self.dir_x = -1
        self.dir_y = -1

    def move(self):
        new_x = self.xcor() + STEP * self.dir_x
        new_y = self.ycor() + self.y_angle_randomizer * self.dir_y
        self.goto(new_x, new_y)

    def check_paddle_collision(self, paddle, cpu_paddle):
        if self.distance(paddle) < 50 and self.xcor() < -260:
            self.dir_x *= -1
            self.y_angle_randomizer = random.randint(3, 30)
        if self.distance(cpu_paddle) < 50 and self.xcor() > 260:
            self.dir_x *= -1
            self.y_angle_randomizer = random.randint(3, 30)

    def check_border_collision(self):
        if abs(self.ycor()) > 280:
            self.dir_y *= -1

    def is_outside(self):
        if self.xcor() > 300:
            self.dir_x *= -1
            return 1
        if self.xcor() < -300:
            self.dir_x *= -1
            return -1
        return 0

    def restart_position(self):
        self.y_angle_randomizer = random.randint(3, 30)
        self.goto(0, 0)
