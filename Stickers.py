import json
from tkinter import *
from PIL import ImageTk, Image
from check_team import checkTeam

root = Tk()
root.title("Sticker Collection")
root.iconbitmap('e:/Stickers/Logo.ico')

addLabel = Label(root)
checkLabel = Label(root)
logoLabel = Label(root)

def read(filename):
    with open(filename, "r", encoding = 'utf-8') as file:
        return json.load(file)

journal = read("data.json")

def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, "w", encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

def addSticker():
    global myLabel_1
    addLabel.destroy()
    checkLabel.destroy()
    logoLabel.destroy()
    x = e.get()
    y = e_1.get()
    x = int(x)
    if x in journal:
        addLabel = Label(root, text="You have already collected the sticker of " + journal[x])
        addLabel.grid(row=7, column=0)
    if x not in journal:
        journal[x] = y
        addLabel = Label(root, text="You have successfully added the sticker of " + journal[x])
        addLabel.grid(row=7,column=0)
        write(journal, "data.json")

def checkSticker():
    global checkLabel
    global logoLabel
    addLabel.destroy()
    checkLabel.destroy()
    logoLabel.destroy()
    journal = read("data.json")
    sticker_number = e.get()
    if sticker_number in journal:
        checkLabel = Label(root, text="You have already collected a sticker of " +journal[sticker_number])
        checkLabel.grid(row=6,column=0)
    elif sticker_number not in journal:
        global my_img
        checkLabel = Label(root, text="Nema, but this sticker is from")
        checkLabel.grid(row=6, column=0)
        my_img = ImageTk.PhotoImage(Image.open("Images/"+checkTeam(sticker_number)+".jpg"))
        logoLabel = Label(image=my_img, width=300, height=450)
        logoLabel.grid(row=7, column=0)

e = Entry(root, width=35, borderwidth=5)
e.grid(row=3, column=0, padx=60, pady=30)
e.insert(0, "Write the Sticker Number")

e_1 = Entry(root, width=35, borderwidth=5)
e_1.grid(row=4, column=0, padx=60, pady=30)
e_1.insert(0, "Write the Name")


myButton = Button(root, text="Add Sticker", padx=60, pady=30, command=addSticker)
myButton_1 = Button(root, text="Check Sticker", padx=60, pady=30, command=checkSticker)

myButton.grid(row=1, column=0)
myButton_1.grid(row=5, column=0)

root.mainloop()
