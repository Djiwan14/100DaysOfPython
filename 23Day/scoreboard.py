from turtle import Turtle
FONT = ("Courier", 24, "normal")
LEVEL = 1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = LEVEL
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += LEVEL
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write("Game is over!", align="Center", font=("Courier", 8, "normal"))
