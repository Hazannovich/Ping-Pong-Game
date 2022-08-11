from turtle import Turtle

LEFT_POSITION = -380
RIGHT_POSITION = 370


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()

    def setup_left(self):
        self.setx(LEFT_POSITION)

    def setup_right(self):
        self.setx(RIGHT_POSITION)

    def go_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)
