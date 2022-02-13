from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

with open("data.txt") as file:
    up_score = int(file.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.high_score = up_score
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.points} High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.points += 1
        self.update_scoreboard()

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
        self.points = 0
        self.update_scoreboard()
        with open("data.txt", "w") as file1:
            file1.write(str(self.high_score))
