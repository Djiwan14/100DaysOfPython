import turtle as t
import random
timmy_turtle = t.Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("chartreuse")


# Challenge 1
def turn_right(num):
    for h in range(num):
        timmy_turtle.forward(100)
        timmy_turtle.right(90)


turn_right(4)


screen = t.Screen()
screen.exitonclick()
