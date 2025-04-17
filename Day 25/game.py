from turtle import Turtle
import turtle


class Game:
    def __init__(self, data):
        self.score = 0
        self.states = data

    def guess_state(self):
        guess: str = turtle.textinput(
            f"{self.score}/50 States Correct", "What's another state name?"
        )
        print(guess == None)
        if guess == None:
            return False
        else:
            self.show_state(guess.title())
            return True

    def show_state(self, state_name):
        if state_name in self.states:
            state = Turtle()
            state.hideturtle()
            state.penup()
            state.goto(self.states[state_name])
            state.write(state_name, move=False)
            self.score += 1
