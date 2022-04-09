import json
from tkinter import *
from PIL import ImageTk, Image
from CheckTeam import check_team

root = Tk()
root.title("Sticker Collection")
root.iconbitmap('e:/Stickers/Logo.ico')

add_label = Label(root)
check_label = Label(root)
logo_label = Label(root)

def read(filename):
    with open(filename, "r", encoding = 'utf-8') as file:
        return json.load(file)

journal = read("data.json")

def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, "w", encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

def add_sticker():
    global add_label
    add_label.destroy()
    check_label.destroy()
    logo_label.destroy()
    x = e.get()
    y = e_1.get()
    x = int(x)
    if x in journal:
        add_label = Label(root, text="You have already collected the sticker of " + journal[x])
        add_label.grid(row=7, column=0)
    if x not in journal:
        journal[x] = y
        add_label = Label(root, text="You have successfully added the sticker of " + journal[x])
        add_label.grid(row=7,column=0)
        write(journal, "data.json")

def check_sticker():
    global check_label
    global logo_label
    add_label.destroy()
    check_label.destroy()
    logo_label.destroy()
    journal = read("data.json")
    sticker_number = e.get()
    if sticker_number in journal:
        check_label = Label(root, text="You have already collected a sticker of " +journal[sticker_number])
        check_label.grid(row=6,column=0)
    elif sticker_number not in journal:
        global my_img
        check_label = Label(root, text="Nema, but this sticker is from")
        check_label.grid(row=6, column=0)
        my_img = ImageTk.PhotoImage(Image.open("Images/"+check_team(sticker_number)+".jpg"))
        logo_label = Label(image=my_img, width=300, height=450)
        logo_label.grid(row=7, column=0)

e = Entry(root, width=35, borderwidth=5)
e.grid(row=3, column=0, padx=60, pady=30)
e.insert(0, "Write the Sticker Number")

e_1 = Entry(root, width=35, borderwidth=5)
e_1.grid(row=4, column=0, padx=60, pady=30)
e_1.insert(0, "Write the Name")


add_button = Button(root, text="Add Sticker", padx=60, pady=30, command=add_sticker)
check_button = Button(root, text="Check Sticker", padx=60, pady=30, command=check_sticker)

add_button.grid(row=1, column=0)
check_button.grid(row=5, column=0)

root.mainloop()
