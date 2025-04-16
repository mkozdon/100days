from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.goto(-280, 260)
        self.hideturtle()
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(
            f"Level: {self.level}",
            move=False,
            align="left",
            font=FONT,
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "Game Over",
            move=False,
            align="center",
            font=FONT,
        )
