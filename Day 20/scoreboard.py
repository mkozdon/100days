from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.sety(265)
        self.hideturtle()
        self.write(
            f"Score: {self.score}",
            move=False,
            align="center",
            font=("Courier", 15, "normal"),
        )

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(
            f"Score: {self.score}",
            move=False,
            align="center",
            font=("Courier", 15, "normal"),
        )

    def game_over(self):
        self.sety(0)
        self.write(
            "Game Over!",
            move=False,
            align="center",
            font=("Courier", 30, "normal"),
        )
