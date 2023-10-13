from flask import Flask
import random

app = Flask(__name__)
number = random.randint(0, 9)

@app.route('/')
def home():
    return "<h1>Guess the number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/DhiRqIsofVMi7fWNBQ/giphy.gif' width=350>"

@app.route('/<int:user_number>')
def user_guess(user_number):
    if user_number > number:
        return "<h2 style='text-align: center; background-color: red;'> Too high </h2>" \
               "<img src='https://media.giphy.com/media/XoL32J2NHx0G0tuBsU/giphy.gif' width=350>"
    elif user_number < number:
        return "<h2 style='text-align: center; background-color: purple;'> Too high </h2>" \
               "<img src='https://media.giphy.com/media/o0EqSJC53G7WlnHdDR/giphy.gif' width=350>"
    elif user_number == number:
        return "<h2 style='text-align: center; background-color: green;'> You found it </h2>" \
               "<img src='https://media.giphy.com/media/KtyTa7XH5ueJLYwmaG/giphy-downsized-large.gif' width=350>"

if __name__ == "__main__":
    app.run(debug=True)
