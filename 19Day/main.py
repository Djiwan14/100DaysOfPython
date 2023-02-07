import turtle
tim = turtle.Turtle()
screen = turtle.Screen()

def move_forwards():
    tim.fd(10)


tim.shape("turtle")
screen.listen() #will act only if we press smth on keyboard
screen.onkey(key="space", fun=move_forwards) # once it listened signal ("key") in this case, do smth (fun = "move_fd))
screen.exitonclick()
