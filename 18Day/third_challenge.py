import turtle as t
import random
timmy_turtle = t.Turtle()
colors = ["medium blue", "steel blue", "crimson", "indigo", "red", "yellow", "brown"]


def draw_shapes(num_sides):
    angle = 360 / num_sides
    timmy_turtle.color(random.choice(colors))
    for _ in range(num_sides):
        timmy_turtle.fd(100)
        timmy_turtle.right(angle)


for shape in range(3, 11):
    draw_shapes(shape)


# def many_figures():
#     for _ in range(3):
#         timmy_turtle.lt(120)
#         timmy_turtle.fd(100)
#     for _ in range(4):
#         timmy_turtle.lt(90)
#         timmy_turtle.fd(100)
#     for _ in range(5):
#         timmy_turtle.lt(72)
#         timmy_turtle.fd(100)
#     for i in range(6):
#         timmy_turtle.lt(60)
#         timmy_turtle.fd(100)
#     for _ in range(8):
#         timmy_turtle.lt(45)
#         timmy_turtle.fd(100)
#     for _ in range(9):
#         timmy_turtle.lt(40)
#         timmy_turtle.fd(100)
#     for _ in range(10):
#         timmy_turtle.lt(36)
#         timmy_turtle.fd(100)

# many_figures()


screen = t.Screen()
screen.exitonclick()


def smth(number):
    angle = 360 / number
    timmy_turtle.color(colors[random.randint(0, 6)])
    for _ in range(number):
        timmy_turtle.fd(100)
        timmy_turtle.right(angle)

for shape in range(3, 11):
    smth(shape)
