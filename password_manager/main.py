import tkinter as Tk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letter
    random.shuffle(password_list)

    password = "".join(password_list)
    ent_pas.delete(0, Tk.END)
    ent_pas.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    get_web = ent_web.get()
    get_email = ent_email.get()
    get_pas = ent_pas.get()
    new_data = {
        get_web: {
            "email": get_email,
            "password": get_pas
        }
    }

    if len(get_web) == 0 or len(get_pas) == 0 or len(get_email) == 0:
        messagebox.showerror(title="Ошибка", message="Заполните все пустые строки")
    else:
        is_ok = messagebox.askokcancel(title=get_web, message=f"Проверьте правильность введенных данных\n"
                                                              f"Email: {get_email}\nPassword: {get_pas}")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                ent_web.delete(0, Tk.END)
                ent_pas.delete(0, Tk.END)


def find_password():
    web = ent_web.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No Data File Found")
    else:
        if web in data:
            result = data[web]
            mes_res = f"Email: {result['email']}\n" \
                      f"Password: {result['password']}"
            pyperclip.copy(result['password'])
            messagebox.showinfo(title=web, message=mes_res)
        else:
            messagebox.showinfo(title="Error", message="No Data Found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Tk.Canvas(width=200, height=200, highlightthickness=0)
logo_img = Tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website = Tk.Label(text="Website:")
website.grid(row=1, column=0)

email = Tk.Label(text="Email/Username:")
email.grid(row=2, column=0)

password = Tk.Label(text="Password:")
password.grid(row=3, column=0)

ent_web = Tk.Entry(width=23)
ent_web.grid(row=1, column=1)
ent_web.focus()

ent_email = Tk.Entry(width=45)
ent_email.grid(row=2, column=1, columnspan=2)

ent_pas = Tk.Entry(width=23)
ent_pas.grid(row=3, column=1)

butt_gen = Tk.Button(text="Generate Password", width=20, command=generate)
butt_gen.grid(row=3, column=2)

butt_add = Tk.Button(text="Add", width=45, command=save)
butt_add.grid(row=4, column=1, columnspan=2)

butt_srch = Tk.Button(text="Search", width=20, command=find_password)
butt_srch.grid(row=1, column=2)

window.mainloop()
