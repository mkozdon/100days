import tkinter as tk
import tkinter.messagebox as mb
import random
import json

IMG_PATH = "Day 29\logo.png"
STORAGE_PATH = "Day 29/data.json"
LETTERS = 8
SYMBOLS = 3
NUMBERS = 2


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [chr(n) for n in range(65, 91)] + [chr(n) for n in range(97, 123)]
    numbers = [chr(n) for n in range(48, 58)]
    symbols = [chr(n) for n in range(33, 48)]
    raw_pwd = []
    raw_pwd += [random.choice(letters) for n in range(1, LETTERS + 1)]
    raw_pwd += [random.choice(symbols) for n in range(1, SYMBOLS + 1)]
    raw_pwd += [random.choice(numbers) for n in range(1, NUMBERS + 1)]
    random.shuffle(raw_pwd)
    return "".join(raw_pwd)


def generate_password_click():
    new_password = generate_password()
    window.clipboard_clear()
    window.clipboard_append(new_password)
    window.update()
    pwd_entry.delete(0, "end")
    pwd_entry.insert(tk.END, string=new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pwd():
    website = website_entry.get()
    username = username_entry.get()
    password = pwd_entry.get()
    new_data = {website: {"username": username, "password": password}}
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        mb.showwarning(title="Warning", message="Empty fields are not allowed.")
        return
    if mb.askyesno(
        "Save Prompt", f"Save below logon data?\n{website}\n{username}\n{password}"
    ):
        try:
            with open(STORAGE_PATH, "r") as output:
                data = json.load(output)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        with open(STORAGE_PATH, "w") as output:
            json.dump(data, output, indent=4)

        pwd_entry.delete(0, "end")
        username_entry.delete(0, "end")
        website_entry.delete(0, "end")


def search():
    website = website_entry.get()
    try:
        with open(STORAGE_PATH, "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        mb.showwarning(title="Error", message="Data File Not Found")
    else:
        if website in data:
            message = f"Email: {data[website]['username']} \nPassword: {data[website]['password']}"
        else:
            message = f"Data for {website} not found."
        mb.showwarning(title=website, message=message)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()

window.title("Password Manager")
# window.minsize(250, 150)
window.config(padx=50, pady=50)
logo = tk.PhotoImage(file=IMG_PATH)
canvas = tk.Canvas(width=200, height=190)
canvas.create_image(100, 100, image=logo)

website_label = tk.Label(text="Website:")
username_label = tk.Label(text="Email/Username:")
pwd_label = tk.Label(text="Password:")
website_entry = tk.Entry(width=21)
username_entry = tk.Entry(width=40)
pwd_entry = tk.Entry(width=21)
generate_button = tk.Button(
    text="Generate Password", command=generate_password_click, width=17
)
add_button = tk.Button(text="Add", width=39, command=save_pwd)
search_button = tk.Button(text="Search", width=17, command=search)

canvas.grid(column=0, row=0, columnspan=3)
website_label.grid(column=0, row=1)
username_label.grid(column=0, row=2)
pwd_label.grid(column=0, row=3)

website_entry.grid(column=1, row=1, sticky="w")
username_entry.grid(column=1, row=2, columnspan=2)
pwd_entry.grid(column=1, row=3, sticky="w")
generate_button.grid(column=2, row=3, sticky="e")
add_button.grid(column=1, row=4, columnspan=2)
search_button.grid(column=2, row=1, sticky="e")

window.mainloop()
# columnspan = 2
