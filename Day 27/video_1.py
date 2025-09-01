# import tkinter
from tkinter import *

from click import command

window = Tk()

window.title("This is my first GUI.")
window.minsize(width=500,height=400)
my_lavel = Label(text="I am level",font=("Arial", 23,"bold"))
my_lavel.pack()
# my_lavel.pack(side="left")
# my_lavel.pack(expand=1)

my_lavel["text"] = "New Text"
my_lavel.config(text="New Text")
def button_used():
    # print("Yes I am working.")
    my_lavel.config(text="I am working")

input = Entry(width=20)
input.pack()

def button_user_input():
    user = input.get()
    my_lavel.config(text=user)
#Create Button
button = Button(text="Click Me",font=("Arial", 12,"bold"), command=button_user_input)

#Entry
# input = Entry(width=20)
# input.pack()
# input.get()

button.pack()

window.mainloop()