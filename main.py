import tkinter as tk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

email_username_entry = tk.Entry(width=52)
email_username_entry.grid(row=2, column=1, columnspan=2)

password_entry = tk.Entry(width=33)
password_entry.grid(row=3, column=1)

# Creating buttons
generate_password_button = tk.Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=44)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()