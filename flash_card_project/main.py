import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
df = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Translate.csv")
    df = original_data.to_dict(orient="records")
else:
    df = data.to_dict(orient="records")


def next_card():
    global rand_word, flip_timer
    window.after_cancel(flip_timer)
    rand_word = random.choice(df)
    canvas.itemconfig(old_img, image=canv_img)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=f"{rand_word['English']}", fill="black")
    flip_timer = window.after(3000, trst_word)


def learn_word():
    global rand_word
    df.remove(rand_word)
    next_card()
    data_fr = pandas.DataFrame(df)
    data_fr.to_csv("data/words_to_learn.csv", index=False)


def trst_word():
    new_img = tk.PhotoImage(file="images/card_back.png")
    canvas.itemconfig(old_img, image=new_img)
    canvas.itemconfig(card_title, text="Russian", fill="white")
    canvas.itemconfig(card_word, text=f"{rand_word['Russian']}", fill="white")


window = tk.Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, trst_word)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canv_img = tk.PhotoImage(file="images/card_front.png")
old_img = canvas.create_image(400, 263, image=canv_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

rig_img = tk.PhotoImage(file="images/right.png")
but_agr = tk.Button(image=rig_img, highlightthickness=0, command=learn_word)
but_agr.grid(row=1, column=1)

wrng_img = tk.PhotoImage(file="images/wrong.png")
but_wrng = tk.Button(image=wrng_img, highlightthickness=0, command=next_card)
but_wrng.grid(row=1, column=0)

next_card()

window.mainloop()
