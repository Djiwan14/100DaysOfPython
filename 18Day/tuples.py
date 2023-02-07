import turtle as t
import random

timmy_turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


directions = [0, 90, 180, 270]
timmy_turtle.pensize(15)
timmy_turtle.speed("fastest")

for _ in range(200):
    timmy_turtle.color(random_color())
    timmy_turtle.forward(30)
    timmy_turtle.setheading(random.choice(directions))

my_screen = t.Screen()
my_screen.exitonclick()
