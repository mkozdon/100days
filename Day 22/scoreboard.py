from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.color("white")
        self.sety(225)
        self.hideturtle()
        self.write(
            f"{self.left_score}:{self.right_score}",
            move=False,
            align="center",
            font=("Courier", 40, "normal"),
        )

    def refresh_score(self):
        self.clear()
        self.write(
            f"{self.left_score}:{self.right_score}",
            move=False,
            align="center",
            font=("Courier", 40, "normal"),
        )
