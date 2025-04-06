import colorgram
from turtle import Turtle, Screen
import random

rgb = []
colors = colorgram.extract("day 18\image.jpg", 30)
for color in colors:
    rgb.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(rgb)


screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.penup()
timmy.speed(0)
timmy.pencolor(random.choice(rgb))
for n in range(int(screen.window_height() / 50)):
    timmy.sety((-screen.window_height() / 2) + n * 50 + 30)
    timmy.setx((-screen.window_width() / 2) + 28)
    for n in range(int(screen.window_width() / 50)):
        timmy.color(random.choice(rgb))
        timmy.dot(20)
        timmy.forward(50)
screen.exitonclick()
