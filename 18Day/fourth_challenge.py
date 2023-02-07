import turtle as t
import random
timmy_turtle = t.Turtle()

colors = ["medium blue", "steel blue", "crimson", "indigo", "red", "yellow", "brown"]
directions = [0, 90, 180, 270]
timmy_turtle.pensize(15)
timmy_turtle.speed("fastest")

for _ in range(200):
    timmy_turtle.color(random.choice(colors))
    timmy_turtle.forward(30)
    timmy_turtle.setheading((random.choice(directions)))


# def random_steps(num):
#     timmy_turtle.color(random.choice(colors))
#     timmy_turtle.pensize(15)
#     timmy_turtle.speed('fastest')
#     for _ in range(num):
#         number = random.randint(0, 3)
#         if number == 0:
#             timmy_turtle.color(random.choice(colors))
#             timmy_turtle.forward(30)
#         elif number == 1:
#             timmy_turtle.color(random.choice(colors))
#             timmy_turtle.back(30)
#         elif number == 2:
#             timmy_turtle.color(random.choice(colors))
#             timmy_turtle.right(90)
#             timmy_turtle.fd(30)
#         elif number == 3:
#             timmy_turtle.color(random.choice(colors))
#             timmy_turtle.left(90)
#             timmy_turtle.fd(30)
# random_steps(100)

screen = t.Screen()
screen.exitonclick()
