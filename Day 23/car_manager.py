from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars: list[Turtle] = []
        self.speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT

    def create_car(self, x=320, y=None):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.setheading(0)
        new_car.shapesize(stretch_wid=1, stretch_len=3)
        new_car.penup()
        if y == None:
            y = random.randint(-260, 280)
        new_car.goto(x, y)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.setx(car.xcor() - self.speed)

    def generate_starting_cars(self, count):
        for _ in range(count):
            self.create_car(random.randint(-200, 300))

    def generate_random_car(self):
        if random.randint(1, 3) == 1:
            self.create_car()

    def check_collisions(self, turtle: Turtle):
        for car in self.cars:
            if (
                -20 < car.ycor() - turtle.ycor() < 30
                and -40 < car.xcor() - turtle.xcor() < 40
            ):
                return True
        return False
