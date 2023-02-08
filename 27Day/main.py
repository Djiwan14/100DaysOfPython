from tkinter import *

window = Tk()
window.title("First Gui program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am Label", font=("Arial", 24, "bold"))
my_label.pack()

# my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button


def button_clicked():
    print("I got clicked")


def challenge_click():
    my_label.config(text=input.get())
    # Challenge 2 to pu inputted text into the label
    # my_label.config(text="Button got clicked")


button = Button(text="Click me", command=challenge_click)
button.pack()

# Input
input = Entry(width=10)
input.pack()
my_label.config(text=input.get())

window.mainloop()
