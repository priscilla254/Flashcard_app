from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
try:
   data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
   original_data=pandas.read_csv("data/french_words.csv")
   data_dict=original_data.to_dict(orient="records")
else:
   data_dict = data.to_dict(orient='records')
current_word={}
def generate_random_card():
   global current_word, flip_timer
   window.after_cancel(flip_timer)
   current_word=random.choice(data_dict)
   canvas.itemconfig(title,text="French",fill="black")
   canvas.itemconfig(word,text=current_word["French"],fill="black")
   canvas.itemconfig(canvas_image, image=card_front_img)
   flip_timer=window.after(3000, flip_card)
def flip_card():
   global current_word
   canvas.itemconfig(title,text="English",fill="white")
   canvas.itemconfig(word,text=current_word["English"],fill="white")
   canvas.itemconfig(canvas_image, image=card_back_img)

def is_known():
   data_dict.remove(current_word)
   data=pandas.DataFrame(data_dict)
   data.to_csv("data/words_to_learn.csv",index=False)
   generate_random_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer=window.after(3000, func=flip_card)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image=canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bd=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=generate_random_card)
wrong_button.grid(column=0, row=1)
generate_random_card()
window.mainloop()
