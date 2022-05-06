from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass(x, y):
    if x == 0:
        return
    b.append(random.choice(y))
    generate_pass(x - 1, y)


b = []


def werfwef():
    global b
    b = []
    p_input.delete(0, END)
    generate_pass(5, letters)
    generate_pass(5, numbers)
    generate_pass(5, symbols)
    random.shuffle(b)
    password = "".join(b)
    pyperclip.copy(password)
    p_input.insert(END, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website = m_input.get()
    email = e_input.get()
    passw = p_input.get()
    new_data = {
        website: {
            "email": email,
            "password": passw,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(passw) == 0:
        messagebox.showinfo(title='Error', message="Dont")
    else:
        # is_ok = messagebox.askokcancel(title="website", message="Are you sure?")
        # if is_ok:
        try:
            with open("data.json", "r") as txt:
                data = json.load(txt)
        except FileNotFoundError:
            with open("data.json", "w") as txt:
                json.dump(new_data, txt, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as txt:
                json.dump(data, txt, indent=4)
        finally:
            m_input.delete(0, END)
            p_input.delete(0, END)


def search():
    website = m_input.get()
    try:
        with open("data.json", "r") as txt:
            data = json.load(txt)
    except FileNotFoundError:
        messagebox.showinfo(title=f"{website}", message="File not found")
    else:
        if website in data:
            email = data[website]["email"]
            passw = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {passw}")
        else:
            messagebox.showinfo(title=f"{website}", message=f"Website {website} not found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MANAGER")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

label_site = Label(text="WebSite", font=(FONT_NAME, 12, "bold"))
label_site.grid(row=1, column=0)

label_login = Label(text="Login", font=(FONT_NAME, 12, "bold"))
label_login.grid(row=2, column=0)

label_pass = Label(text="Password", font=(FONT_NAME, 12, "bold"))
label_pass.grid(row=3, column=0)

m_input = Entry(width=33)
m_input.focus()
m_input.insert(END, string="website")
m_input.grid(row=1, column=1)

e_input = Entry(width=43)
e_input.insert(END, string="login")
e_input.grid(row=2, column=1, columnspan=2)

p_input = Entry(width=33)
p_input.insert(END, string="password")
p_input.grid(row=3, column=1)

button_g = Button(text="Generate", width=7, command=werfwef)
button_g.grid(row=3, column=2)

button_a = Button(text="Add", width=36, command=add_to_file)
button_a.grid(row=4, column=1, columnspan=2)

button_g = Button(text="Search", width=7, command=search)
button_g.grid(row=1, column=2)

window.mainloop()
