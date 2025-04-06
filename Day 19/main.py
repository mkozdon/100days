from turtle import Turtle, Screen
import random

TURTLE_GAP = 50
screen = Screen()
screen.colormode(255)
turtles = []


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def create_turtles(turtles, num):
    for _ in range(num):
        new_turtle = Turtle()
        new_turtle.speed(0)
        # new_turtle.xcor()
        new_turtle.penup()
        new_turtle.shape("turtle")
        new_turtle.color(random_color())
        turtles.append(new_turtle)


def lineup_turtles(turtles):
    start = 0 - len(turtles) / 2 * TURTLE_GAP
    for n in range(0, len(turtles)):
        turtles[n].sety(start + n * TURTLE_GAP)
        turtles[n].setx(-screen.window_width() / 2 + 20)


def start_race(turtles):
    race_finished = False
    while not race_finished:
        for n in turtles:
            n.speed(0)
            n.forward(random.randint(10, 50))
            if n.xcor() >= screen.window_width() / 2 - 30:
                race_finished = True
                return turtles.index(n)


def get_bet(turtles):
    return screen.textinput(
        f"Make your bet",
        f"Which turtle will win the race? enter number [1-bottom to {len(turtles)}-up]: ",
    )


create_turtles(turtles, 2)
bet = get_bet(turtles)
lineup_turtles(turtles)
winner = start_race(turtles)
if int(bet) == int(winner) + 1:
    print("You've Won!")

screen.exitonclick()
