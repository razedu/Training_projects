from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.show_score()

    def show_score(self):
        self.goto(-230, 270)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def score_up(self):
        self.clear()
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align="center", font=FONT)
