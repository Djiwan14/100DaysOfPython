import tkinter

window = tkinter.Tk()
window.title("Convert it")
window.minsize(width=350, height=200)


def clicked():
    global miles
    miles = int(input.get())
    miles = round(miles * 1.6)
    count_label.config(text=miles)


label = tkinter.Label(text="is equal to")
label.grid(column=0, row=1)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

miles_label = tkinter.Label(text="miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=5)

count_label = tkinter.Label(text="0")
count_label.grid(column=1, row=1)

kilometers_label = tkinter.Label(text="km")
kilometers_label.grid(column=2, row=1)

button = tkinter.Button(text="calculate", command=clicked)
button.grid(column=1, row=2)

window.mainloop()
