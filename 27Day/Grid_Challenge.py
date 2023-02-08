import tkinter
window = tkinter.Tk()
window.title("Challenge")
window.minsize(width=500, height=500)

label = tkinter.Label(text="New one", font=("Aqua", 20, "italic"))
label.grid(column=0, row=0)

button = tkinter.Button(text="Click me")
button.grid(column=1, row=1)

button_2 = tkinter.Button(text="Don't touch")
button_2.grid(column=2, row=0)

input = tkinter.Entry(width=20)
input.grid(column=4, row=3)


window.mainloop()
