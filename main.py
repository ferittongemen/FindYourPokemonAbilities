from tkinter import messagebox
from tkinter import *
import requests
from PIL import ImageTk, Image

target_url = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=1292"


def get_poke_data():
    response = requests.get(target_url)
    if response.status_code == 200:
        return response.json()


poke_response = get_poke_data()


def get_poke_abilities():
    user_input = user_entry.get()
    found = False
    for poke in poke_response["results"]:
        if poke["name"] == user_input:
            user_poke_info = requests.get(poke["url"])

            for info in user_poke_info.json()["abilities"]:
                response = info["ability"]
                responseAbility = response["name"]
                hidden = info["is_hidden"]
                if hidden == 1:
                    messagebox.showinfo("Is Ability Hidden?", f"{responseAbility}" " " "(hidden)")
                else:
                    messagebox.showinfo("Is Ability Hidden?", f"{responseAbility}" " " "(not hidden)")

            found = True

    if not found:
        messagebox.showerror("Error", "Enter Your Poke Correctly!")


# GUI
win = Tk()
win.config()
win.geometry("700x500")

frame = Frame(win, width=100, height=100)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("Poké_Ball_icon.svg.png"))

label = Label(frame, image=img)
label.pack()

button = Button(text="Get Your Pokemon Abilities", bg="#F6382C", command=get_poke_abilities)
button.place(x=260, y=435)
button.config(width=25)

user_entry = Entry()
user_entry.place(x=285, y=410)
user_entry.config(width=20)

output_label = Label()
output_label.pack()

win.mainloop()
