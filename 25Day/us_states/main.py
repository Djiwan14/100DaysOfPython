import turtle
from turtle import Turtle, Screen
import pandas
screen = Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                              prompt="What's another state's name?").title()
    if answer == "Exit":
        missings = [names for names in all_states if names not in guessed_states]
        new_data = pandas.DataFrame(missings)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        if answer in all_states:
            guessed_states.append(answer)
            t = Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer)
