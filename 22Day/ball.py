from turtle import Turtle
import random as r
COLOR = ("red", "blue", "grey", "green", "yellow")


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.width = 20
        self.height = 20
        self.color("white")
        self.shape("circle")
        self.setposition(position)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def change_color(self):
        self.color(r.choice(COLOR))
