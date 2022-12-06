from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_button_clicked():
    window.after_cancel(timer)
    label.config(text="Timer", bg=YELLOW, fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    ticks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_button_clicked():
    # count on the screen
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", bg=YELLOW, fg=RED)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", bg=YELLOW, fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", bg=YELLOW, fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_button_clicked()
        marks = ""
        for i in range(math.floor(reps/2)):
            marks += "✔"
        ticks.config(text=marks, fg=GREEN, bg=YELLOW)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# Label
label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_button_clicked)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_button_clicked)
reset_button.grid(column=2, row=2)

# Label of tick
ticks = Label(fg=GREEN, bg=YELLOW)
ticks.grid(column=1, row=2)
window.mainloop()
