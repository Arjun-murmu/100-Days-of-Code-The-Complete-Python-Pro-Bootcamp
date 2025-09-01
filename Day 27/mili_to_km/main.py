from tkinter import *

FONT = ("Arial", 13, "bold")

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=100, pady=100)

miles_input = Entry(width=15)
miles_input.grid(column=1, row=0)

def calculation_part():
    my_answer = Label(font=("Arial",12))
    my_answer.grid(column=1, row=1)
    miles = float(miles_input.get())
    km = round(1.609 * miles)
    my_answer.config(text=f"{km}")


#Label
my_level_one = Label(text="miles", font=FONT)
my_level_one.grid(column=3, row=0)

#Label
my_level_two = Label(text="is equal to", font=FONT)
my_level_two.grid(column=0, row=1)

#Label
my_level_km = Label(text="km", font=FONT)
my_level_km.grid(column=2, row=1)

#Button
button = Button(text="Calculation", command=calculation_part)
button.grid(column=1, row=2)

window.mainloop()