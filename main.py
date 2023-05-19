from tkinter import *
from tkinter import messagebox
import pyperclip
import json
from pass_generator import generate_password


# ---------------------------- NEEDED FUNCTIONS ------------------------------- #
def add_pass():
    """A function that adds a password."""
    password = generate_password()
    in_pass.delete(0, END)
    in_pass.insert(END, password)
    pyperclip.copy(password)


def save_info():
    """A function that saves info."""
    website = in_website.get()
    website = website.title()
    email = in_email.get()
    email = email.lower()
    password = in_pass.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check if empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="WARNING", message="Make sure fields are not empty.")
        return NONE

    # Check if inputted data is valid.
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details you've entered: \n"
                                                          f"Email: {email}\n"
                                                          f"Password: {password}\n"
                                                          f"Save?")

    if is_ok:
        try:
            with open("my_passwords.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("my_passwords.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("my_passwords.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            in_website.delete(0, END)
            in_pass.delete(0, END)


def search_data():
    """A function that searches for specific data."""
    website = in_website.get()
    website = website.title()

    is_ok = len(website) > 0
    if is_ok:
        try:
            with open("my_passwords.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="You currently have no passwords saved.")
        else:
            try:
                email = data[website]["email"]
            except KeyError:
                messagebox.showwarning(title="Error", message=f"No Information Saved for {website}")
            else:
                password = data[website]["password"]
                messagebox.showinfo(title="Saved Info", message=f"Saved info for {website}\n"
                                                                f"Email: {email}\n"
                                                                f"Password:{password}")
    else:
        messagebox.showwarning(title="Error", message="Input website title.")


# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = Tk()
window.title("Password Generator")
window.config(padx=40, pady=40)

# Logo Setup
logo = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=logo_img)
logo.grid(row=0, column=1)

# Labels
lb_website = Label(text="Website:")
lb_website.config(padx=0, pady=5)
lb_website.grid(row=1, column=0)

lb_email = Label(text="Email/Username:")
lb_email.grid(row=2, column=0)
lb_email.config(padx=0, pady=5)

lb_pass = Label(text="Password:", width=20)
lb_pass.grid(row=3, column=0)
lb_pass.config(padx=0, pady=5)

# Input Boxes / Entries
in_website = Entry(width=35, justify="left")
in_website.grid(row=1, column=1)
in_website.focus()

in_email = Entry(width=53, justify="left")
in_email.grid(row=2, column=1, columnspan=2)
in_email.insert(END, "tamarastajic97@gmail.com")

in_pass = Entry(width=35, justify="left")
in_pass.grid(row=3, column=1)

# Buttons

bt_search = Button(text="Search", width=14, command=search_data)
bt_search.grid(row=1, column=2)

bt_generate = Button(text="Generate Password", command=add_pass)
bt_generate.grid(row=3, column=2)

bt_add = Button(text="Add", width=45, command=save_info)
bt_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
