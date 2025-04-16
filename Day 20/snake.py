from turtle import Turtle

STEP = 20


def create_segment():
    segment = Turtle()
    segment.color("white")
    segment.shape("square")
    segment.penup()
    return segment


class Snake:
    def __init__(self):
        self.body = []
        for n in range(3):
            segment = create_segment()
            segment.setx(segment.xcor() - n * STEP)
            self.body.append(segment)

    def add_segment(self):
        segment = create_segment()
        segment.goto(self.body[-1].xcor(), self.body[-1].ycor())
        self.body.append(segment)

    def move(self):
        for segment_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment_num - 1].xcor()
            new_y = self.body[segment_num - 1].ycor()
            self.body[segment_num].goto(new_x, new_y)
        self.body[0].forward(STEP)

    def go_right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def go_up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def go_left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def go_down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def is_self_collision(self):
        for segment_num in range(len(self.body) - 1, 0, -1):
            if self.body[0].distance(self.body[segment_num]) < 15:
                return True
        return False

    def reset(self):
        for segment in self.body:
            segment.goto(1000, 1000)
        self.body.clear()
        self.__init__()
