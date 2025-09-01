from tkinter import *
from tkinter import messagebox
import random
from random import choice, randint,shuffle
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
PALE_RED = "#e2979c"
FONT_NAME = "Arial"   # "Facile" might not exist on all systems, so using Arial

# ---------------------------- Password Generator ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    if password_entry.get():
        messagebox.showinfo("Info", "Password already generated! Please clear it first.")
        return

    # password_latter = [random.choice(letters) for _ in range(randint(8, 10))]
    # password_numbers = [random.choice(numbers) for _ in range(randint(2, 4))]
    # password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = (
            [random.choice(letters) for _ in range(3)] +  # 4 letters
            [random.choice(numbers) for _ in range(3)] +  # 2 numbers
            [random.choice(symbols) for _ in range(3)]  # 2 symbols
    )
    random.shuffle(password_list)

    # password_list = password_latter + password_numbers + password_symbols
    # random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        # messagebox.showwarning(title="warning", message="pleases don't leave any filed")
        messagebox.showinfo(title="Oops", message="pleases don't leave any filed")
    else:
        # messagebox.showinfo(title="Title" ,message="Message")
        is_ok = messagebox.askokcancel(title="website", message=f"These are you details entry: \n Website Name : {website}\n email_id : {email}\n password : {password}\n")

        # confirm_message = messagebox.askquestion(title="website", message=f"These are you details entry: \n Website Name : {website}\n email_id : {email}\n password : {password}\n")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0,END)
                email_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

# Canvas (Logo)
canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
image_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=(FONT_NAME, 12, "bold"), bg=YELLOW)
website_label.grid(row=1, column=0, sticky="e")

email_label = Label(text="Email/Username:", font=(FONT_NAME, 12, "bold"), bg=YELLOW)
email_label.grid(row=2, column=0, sticky="e")

password_label = Label(text="Password:", font=(FONT_NAME, 12, "bold"), bg=YELLOW)
password_label.grid(row=3, column=0, sticky="e")

# Entries
website_entry = Entry(width=35, font=(FONT_NAME, 11))
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()  #cursor will automatically be placed inside the Website entry box.

email_entry = Entry(width=35, font=(FONT_NAME, 11))
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0,"arjunmurmu@gmail.com")

password_entry = Entry(width=21, font=(FONT_NAME, 11))
password_entry.grid(row=3, column=1, pady=5)

# Buttons
password_generate_button = Button(
    text="Generate Password",
    font=(FONT_NAME, 10, "bold"),
    command=password_generator,
    relief="groove",
    bg=GREEN,
    highlightthickness=0
)
password_generate_button.grid(row=3, column=2, padx=5)

add_button = Button(
    text="Save",
    width=36,
    font=(FONT_NAME, 11, "bold"),
    command=save_data,
    bg=PALE_RED,
    relief="groove",
    highlightthickness=0

)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
