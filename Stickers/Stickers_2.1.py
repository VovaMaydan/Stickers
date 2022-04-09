import json
from tkinter import *
from PIL import ImageTk, Image
from LIST_OF_TEAMS import TEAMS, TEAM_OPTIONS
import random

root = Tk()
root.title("Sticker Collection")
root.iconbitmap('e:/Stickers/Logo.ico')

collected_sticker_label = Label(root)
new_sticker_label = Label(root)
add_sticker_label = Label(root)
new_sticker_entry = Entry(root)
add_new_sticker_button = Button(root)
sticker_rest_label = Label(root)

def read(filename):
    with open(filename, "r", encoding = 'utf-8') as file:
        return json.load(file)

journal = read("data.json")

def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, "w", encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

def check_team(sticker_number):
    for team in TEAMS:
        if team["minRange"] < int(sticker_number) < team["maxRange"]:
            return team["name"]

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
    if sticker_number == "":
        collected_sticker_label = Label(frame, text="You didn't write a number")
        collected_sticker_label.grid(row=10, column=2)
    elif sticker_number in journal:
        collected_sticker_label = Label(frame, text="You have already collected a sticker of "+journal[sticker_number])
        collected_sticker_label.grid(row=11, column=2)
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


def sticker_rest():
    global sticker_count
    global sticker_rest_label
    collected_sticker_label.destroy()
    sticker_rest_label.destroy()
    sticker_count = 0
    team_name = team_name_selection.get()
    if team_name == "All":
        for sticker in range(0, 644):
            if str(sticker) in journal:
                pass
            elif str(sticker) not in journal:
                sticker_count += 1
        percentage = (644-sticker_count)/644*100
        percentage = int(percentage)
        sticker_rest_label = Label(frame, text="You have already collected a "+str(percentage)+"% of the album")
        sticker_rest_label.grid(row=10, column=2)
    else:
        for team_count in range(0, 32):
            if team_name == TEAMS[team_count]["name"]:
                selected_team = team_count
                min_number = TEAMS[selected_team]["minRange"]
                max_number = TEAMS[selected_team]["maxRange"]
                for sticker in range(int(min_number),int(max_number)):
                    if str(sticker) in journal:
                        pass
                    elif str(sticker) not in journal:
                        sticker_count += 1
                sticker_rest_label = Label(frame, text="You need to collect " + str(sticker_count) + " more stickers")
                sticker_rest_label.grid(row=10, column=2)


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

team_name_selection = StringVar()
team_name_selection.set("Pick a team")

teams_drop_menu = OptionMenu(frame, team_name_selection, *TEAM_OPTIONS)
teams_drop_menu.grid(row=8, column=2)

team_button = Button(frame, text="Check Team", command=sticker_rest)
team_button.grid(row=9, column=2)

root.mainloop()

