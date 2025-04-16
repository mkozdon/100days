from turtle import Turtle

DATA_FILE = "Day 20\data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.load_highscore()
        self.penup()
        self.color("white")
        self.sety(265)
        self.hideturtle()
        self.update_scoreboard()
        # self.write(
        #     f"Score: {self.score}",
        #     move=False,
        #     align="center",
        #     font=("Courier", 15, "normal"),
        # )

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.highscore}",
            move=False,
            align="center",
            font=("Courier", 15, "normal"),
        )

    def load_highscore(self):
        with open(DATA_FILE, "r") as data:
            return int(data.read())

    def save_highscore(self):
        with open(DATA_FILE, "w") as data:
            data.write(str(self.highscore))

    def game_over(self):
        self.sety(0)
        self.write(
            "Game Over!",
            move=False,
            align="center",
            font=("Courier", 30, "normal"),
        )

    def reset(self):
        self.score = 0
        self.update_scoreboard()
