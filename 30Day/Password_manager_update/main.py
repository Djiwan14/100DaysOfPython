from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json
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
    new_data = {
        website_input.get():{
            "Email": email_entry.get(),
            "Password": password_entry.get()
    }
}

    if len(email_entry.get()) == 0 or len(password_entry.get()) == 0 or len(website_input.get()) == 0:
        messagebox.showinfo(title="Error", message="You left some spaces empty")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_entry.delete(0, END)

#---------------------------Search for password -------------------------#

def find_password():
    website = website_input.get()
    try:
        with open("data.json", mode="r") as json_file:
            content = json.load(json_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        if website in content:
            messagebox.showinfo(title=website, message=f"Email: {content[website]['Email']} \nPassword: {content[website]['Password']}")
        else:
            messagebox.showinfo(title="Error", message="Website details missed")
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
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=3)

password_button = Button(text="Generate password", command=generate_password)
password_button.grid(row=3, column=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
