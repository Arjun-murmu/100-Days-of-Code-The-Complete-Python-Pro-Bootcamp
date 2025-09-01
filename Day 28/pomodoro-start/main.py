from tkinter import *
import math

from pandas.io.sas.sas_constants import column_format_text_subheader_index_length

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_level.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    work_time = WORK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        timer_level.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_level.config(text="Short Break", fg=GREEN)
    else:
        count_down(work_time)
        timer_level.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    #"25:00"
    count_min = math.floor(count/60)
    count_second = count % 60

    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count - 1)      #milisecond
    else:
        start_timer()
        mark = ""
        working_session = math.floor(reps/2)
        for _ in range(working_session):
            mark += "✔️"
            check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Promodoro app")
window.config(padx=110,pady=60, bg=YELLOW)

canvas = Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
image_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image_tomato)
timer_text = canvas.create_text(100,130, text="00:00", fill="black", font=(FONT_NAME,28,"bold"))
canvas.grid(column=1,row=1)


#lebel
timer_level = Label(text="Timer" , fg=PINK ,bg=YELLOW,font=(FONT_NAME,45))
timer_level.grid(column=1,row=0)

check_mark = Label(text="", fg=GREEN ,bg=YELLOW,font=(FONT_NAME,15,"bold"))
check_mark.grid(row=3,column=1)

#BUTTON
start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2,column=2)


window.mainloop()
