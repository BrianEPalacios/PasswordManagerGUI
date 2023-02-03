import tkinter as tk
from tkinter import messagebox

import pyperclip

from password_generator import PasswordGenerator

import json

DEFAULT_USERNAME_ENTRY = "b.estpalacios@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = PasswordGenerator()
    new_password = password.create_password()
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def append_to_file(password_data):
    with open("data.json", "r") as data_file:
        # read old data
        data = json.load(data_file)
        # Update old data with new data
        data.update(password_data)

    with open("data.json", "w") as outfile:
        json.dump(data, outfile, indent=4)


def create_new_file(password_data):
    with open("data.json", "w") as outfile:
        json.dump(password_data, outfile, indent=4)


def save_data():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"these are the details entered: \nEmail: {email}"
                                                      f"\n Password: {password}\nIs it ok to save?")
        if is_ok:
            password_data = {
                website: {
                    "email": email,
                    "password": password
                }
            }
            try:
                append_to_file(password_data)
            except:
                create_new_file(password_data)
            finally:
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")


# -------------------------------------------- Search  Function ------------------------------------------------------#
# ---------------------------- UI SETUP ------------------------------- #
# Creating window
window = tk.Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Creating Canvas
canvas = tk.Canvas(width=200, height=200)

# image for canvas
logo_img = tk.PhotoImage(file="logo.png")
# Add image to canvas using x and y coordinates and image
canvas.create_image(100, 100, image=logo_img)

canvas.grid(row=0, column=1)

# Creating labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

email_username_label = tk.Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

# Creating entry boxes
website_entry = tk.Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
# cursor automatically starts in here
website_entry.focus()

email_username_entry = tk.Entry(width=52)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, DEFAULT_USERNAME_ENTRY)

password_entry = tk.Entry(width=33)
password_entry.grid(row=3, column=1)

# Creating buttons
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=44, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()