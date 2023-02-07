import turtle as t
import random
timmy = t.Turtle()
t.colormode(255)
timmy.shape("turtle")
timmy.pensize(2)
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


for _ in range(36):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.settiltangle(10)
    timmy.lt(10)

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_nap)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_nap)
#
# draw_spirograph(5)

my_screen = t.Screen()
my_screen.exitonclick()
