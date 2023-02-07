import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)  # entering dimensions of screen
user_bet = screen.textinput(title="Make a bet", prompt="Who will win the race? Enter a color: ")  # additional window
colors = ["red", "orange", "green", "yellow", "blue", "purple"]
y_positions = [-80, -40, 0, 40, 80, 120]
all_turtles = []

if user_bet:
    is_race_on = True

for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y_positions[turtle_index])  # goto method lets turtle to go any point in the map
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)


screen.exitonclick()
