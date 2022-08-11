from turtle import Turtle

FONT = ('Arial', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(position)
        self.write(f"{self.score}", False, "center", FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, "center", FONT)
