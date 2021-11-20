from tkinter import *
from tkinter import messagebox
import random as rdm

count = 30
points = 0
wrong_answers = 0
colors = ["red", "yellow", "green", "blue", "orange", "purple"]


def counter_start():
    global root, count, counter
    if count == 0:
        messagebox.showinfo("Score", f"Total answered = {points+wrong_answers}\nRight answers = {points}\n"
                                     f"Wrong answers = {wrong_answers}")
        root.destroy()
        return
    count -= 1
    counter.config(text="Time left = "+str(count)+"s")
    root.after(1000, counter_start)


def check_color():
    global color_label, points, wrong_answers
    if color_label["fg"] == answer_box.get():
        points += 1
    else:
        wrong_answers += 1

    answer_box.delete(0, END)
    color_label.config(text=rdm.choice(colors))
    text_color = rdm.choice(colors)
    while text_color == color_label["text"]:
        text_color = rdm.choice(colors)
    color_label.config(fg=text_color)


root = Tk()

color_label = Label(root, text=rdm.choice(colors), font=("Verdana", 25))
color_label.pack()
color_for_text = rdm.choice(colors)
while color_for_text == color_label["text"]:
    color_for_text = rdm.choice(colors)
color_label.config(fg=color_for_text)
counter = Label(root, text="Time left = "+str(count)+"s", font=("Verdana", 10), relief=SUNKEN)
counter.pack(pady=10)

answer_box = Entry(root, font=("Verdana", 20))
answer_box.pack(pady=10)
answer_box.focus()

button = Button(root, text="Submit", font=("Comic Sans MS", 10), command=check_color)
button.pack(padx=50)
counter_start()
root.mainloop()
