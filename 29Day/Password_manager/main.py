from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_number = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_letters + password_number + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    if len(email_entry.get()) == 0 or len(password_entry.get()) == 0 or len(website_input.get()) == 0:
        messagebox.showinfo(title="Error", message="You left some spaces empty")
    else:
        is_ok = messagebox.askokcancel(title="Data", message=f"These are your entered details: "
                                                             f"\nWebsite : {website_input.get()}"
                                                             f"\n Email : {email_entry.get()}"
                                                             f"\n Password : {password_entry.get()}"
                                                             f"\nAre you ready to save it?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website_input.get()} | {email_entry.get()} | {password_entry.get()}\n")
                entries = [website_input, password_entry]
                for entry in entries:
                    entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text="Website")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "shoha020930@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2)

# Buttons
password_button = Button(text="Generate password", command=generate_password)
password_button.grid(row=3, column=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
