import turtle as t
tim = t.Turtle()
screen = t.Screen()
screen.listen()


def move_fd():
    tim.fd(10)


def move_back():
    tim.back(10)


def move_clockwise():
    # tim.rt(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def move_cc():
    tim.lt(10)


def clean_space():
    tim.home()
    tim.penup()
    tim.clear()
    tim.pendown()


screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_cc)
screen.onkey(key="c", fun=clean_space)
screen.exitonclick()


