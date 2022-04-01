import json
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sticker Collection")
root.iconbitmap('e:/Stickers/Logo.ico')

myLabel_1 = Label(root)
myLabel_2 = Label(root)
myLabel_3 = Label(root)

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
    myLabel_1.destroy()
    myLabel_2.destroy()
    x = e.get()
    y = e_1.get()
    x = int(x)
    if x in journal:
        myLabel_1 = Label(root, text="You have already collected the sticker of " + journal[x])
        myLabel_1.grid(row=7, column=0)
    if x not in journal:
        journal[x] = y
        myLabel_1 = Label(root, text="You have successfully added the sticker of " + journal[x])
        myLabel_1.grid(row=7,column=0)
        write(journal, "data.json")

def checkSticker():
    global myLabel_2
    myLabel_1.destroy()
    myLabel_2.destroy()
    journal = read("data.json")
    n = e.get()
    if n in journal:
        myLabel_2 = Label(root, text="You have already collected a sticker of " +journal[n])
        myLabel_2.grid(row=6,column=0)
    elif n not in journal:
        if int(n) == 333:
            global my_img
            my_img = ImageTk.PhotoImage(Image.open("Images/Shakhtar.jpg"))
            myLabel_2 = Label(root, text="Nema, but this sticker is from")
            myLabel_3 = Label(image=my_img)
            myLabel_2.grid(row=6, column=0, padx=15, pady=7)
            myLabel_3.grid(row=7, column=0, padx=15, pady=7)
        else:
            myLabel_2 = Label(root, text="Nema")
            myLabel_2.grid(row=6, column=0, padx=15, pady=7)




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
