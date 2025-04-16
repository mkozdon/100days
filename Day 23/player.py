from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(0, -280)
        self.reset_position()

    def move(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def level_up(self) -> bool:
        return self.ycor() > 290

    def reset_position(self):
        self.goto(0, -280)
