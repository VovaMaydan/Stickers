import json
from tkinter import *
from PIL import ImageTk, Image
from CheckTeam import check_team
import random

root = Tk()
root.title("Sticker Collection")
root.iconbitmap('e:/Stickers/Logo.ico')

collected_sticker_label = Label(root)
new_sticker_label = Label(root)
add_sticker_label = Label(root)
new_sticker_entry = Entry(root)
add_new_sticker_button = Button(root)

def read(filename):
    with open(filename, "r", encoding = 'utf-8') as file:
        return json.load(file)

journal = read("data.json")

def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, "w", encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

def check_sticker():
    global collected_sticker_label
    global new_sticker_label
    global new_sticker_entry
    global add_new_sticker_button
    global add_sticker_label
    collected_sticker_label.destroy()
    new_sticker_label.destroy()
    new_sticker_entry.destroy()
    add_new_sticker_button.destroy()
    add_sticker_label.destroy()
    sticker_number = check_sticker_entry.get()
    if sticker_number in journal:
        collected_sticker_label = Label(frame, text="You have already collected a sticker of "+journal[sticker_number])
        collected_sticker_label.grid(row=9, column=2)
    else:
        greeting_picture_label.destroy()
        logo_picture = ImageTk.PhotoImage(Image.open("Teams/"+check_team(sticker_number)+".jpg"))
        logo_picture_label = Label(frame, image=logo_picture, width=500, height=280)
        logo_picture_label.image = logo_picture
        logo_picture_label.grid(row=0, column=2)
        new_sticker_label = Label(frame, text="My Congratulations!\n \n Please write the footballers name:")
        new_sticker_label.grid(row=8, column=2)
        new_sticker_entry = Entry(frame, width=35, borderwidth=5)
        new_sticker_entry.grid(row=9, column=2)
        new_sticker_entry.insert(0, "")
        add_new_sticker_button = Button(frame, text="Add Sticker", command=add_sticker)
        add_new_sticker_button.grid(row=10, column=2, pady=20)


def add_sticker():
    global add_sticker_label
    sticker_number = check_sticker_entry.get()
    sticker_name = new_sticker_entry.get()
    journal[sticker_number] = sticker_name
    add_sticker_label = Label(frame, text="You have successfully added the sticker of " + journal[sticker_number])
    add_sticker_label.grid(row=11, column=2)
    write(journal, "data.json")


frame = LabelFrame(root)
frame.grid()

random_number = random.randint(1, 8)
greeting_picture = ImageTk.PhotoImage(Image.open("Winners/"+str(random_number)+".jpg"))
greeting_picture_label = Label(frame, image=greeting_picture, width=500, height=280)
greeting_picture_label.grid(row=0, column=2)

greeting_label = Label(frame, text="Please enter the number of the sticker:")
greeting_label.grid(row=5, column=2)

check_sticker_entry = Entry(frame, width=35, borderwidth=5)
check_sticker_entry.grid(row=6, column=2, padx=20)
check_sticker_entry.insert(0, "")

start_button = Button(frame, text="Check Sticker", command=check_sticker)
start_button.grid(row=7, column=2, pady=20)

root.mainloop()

