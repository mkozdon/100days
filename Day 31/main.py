import tkinter as tk
import pandas as pd
import json
import random

BACKGROUND_COLOR = "#B1DDC6"
DICT_PATH = "Day 31/data/french_words.csv"
WORK_DICT_PATH = "Day 31/data/working_dict.json"
CARD_FRONT = "Day 31/images/card_front.png"
CARD_BACK = "Day 31/images/card_back.png"
BUTTON_CORRECT = "Day 31/images/right.png"
BUTTON_WRONG = "Day 31/images/wrong.png"
FONT_LANG = ("Arial", 30, "italic")
FONT_WORD = ("Arial", 40, "bold")


def initial_dict_load():
    dict_df = pd.read_csv(DICT_PATH)
    dict_lang = dict(zip(dict_df["French"], dict_df["English"]))
    with open(WORK_DICT_PATH, "w") as file:
        json.dump(dict_lang, file)


def get_working_dict():
    try:
        with open(WORK_DICT_PATH, "r") as file:
            work_dict = json.load(file)
    except FileNotFoundError:
        initial_dict_load()
        with open(WORK_DICT_PATH, "r") as file:
            work_dict = json.load(file)
    return work_dict


def get_fr_word_to_guess():
    global current_word_fr
    current_word_fr = random.choice(list(words.keys()))
    return current_word_fr


def get_correct_en_word():
    return words[current_word_fr]


def guess_word():
    get_fr_word_to_guess()
    show_word_to_guess(current_word_fr)


def show_word_to_guess():
    word = get_fr_word_to_guess()
    for obj in canvas.find_all():
        canvas.delete(obj)
    canvas.create_image(400, 263, image=back_image)
    canvas.create_text(
        400, 150, text="French", font=FONT_LANG, fill="white", anchor="center"
    )
    word = canvas.create_text(
        400, 250, text=word, font=FONT_WORD, fill="white", anchor="center"
    )
    window.after(3000, show_correct)


def show_correct():
    correct_word = words[current_word_fr]
    for obj in canvas.find_all():
        canvas.delete(obj)
    canvas.create_image(400, 263, image=front_image)
    canvas.create_text(
        400, 150, text="English", font=FONT_LANG, fill="black", anchor="center"
    )
    word = canvas.create_text(
        400, 250, text=correct_word, font=FONT_WORD, fill="black", anchor="center"
    )


def guessed():
    global words
    del words[current_word_fr]
    with open(WORK_DICT_PATH, "w") as file:
        json.dump(words, file)
    show_word_to_guess()


def not_guessed():
    show_word_to_guess()


current_word_fr = ""
words = get_working_dict()

window = tk.Tk()
back_image = tk.PhotoImage(file=CARD_BACK)
front_image = tk.PhotoImage(file=CARD_FRONT)
correct_image = tk.PhotoImage(file=BUTTON_CORRECT)
wrong_image = tk.PhotoImage(file=BUTTON_WRONG)
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
correct_button = tk.Button(
    image=correct_image, bg=BACKGROUND_COLOR, bd=0, command=guessed
)
wrong_button = tk.Button(
    image=wrong_image, bg=BACKGROUND_COLOR, bd=0, command=not_guessed
)

canvas.grid(column=0, row=0, columnspan=2)
wrong_button.grid(column=0, row=1)
correct_button.grid(column=1, row=1)
show_word_to_guess()
window.mainloop()
