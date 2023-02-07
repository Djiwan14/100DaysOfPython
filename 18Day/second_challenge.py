import turtle as t
timmy_turtle = t.Turtle()


def dashed_line(num):
    for _ in range(num):
        timmy_turtle.pendown()
        timmy_turtle.forward(5)
        timmy_turtle.penup()
        timmy_turtle.forward(5)


dashed_line(25)

screen = t.Screen()
screen.exitonclick()
