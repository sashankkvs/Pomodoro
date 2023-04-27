from tkinter import *
import math
from playsound import playsound
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
timing = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodore")
window.config(padx = 100, pady= 50, bg = YELLOW)

def start_timer():
    # play()
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec =LONG_BREAK_MIN * 60

    if reps % 2 ==0:
       count_down(short_break_sec)
       timer_label.config(text = "Break", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text = "Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=RED)

def play():
    playsound("mixkit-arcade-game-jump-coin-216.wav")
def play_reset():
    playsound("mixkit-positive-interface-beep-221.wav")

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timing
        timing = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work = math.floor(reps/2)
        for _ in range(work):
            mark += "✔"
        my_label.config(text=mark)




def stop_timer():
    # play_reset()
    window.after_cancel(timing)
    canvas.itemconfig(timer, text=f"00:00")
    timer_label.config(text="Timer")
    my_label.config(text="")
    global reps
    reps= 0


canvas = Canvas(width=200, height=224, bg = YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer = canvas.create_text(100, 130, text = "00:00", font = (FONT_NAME, 35, "bold"),fill = "white")
canvas.grid(column=1,row=1)

my_label = Label(foreground=RED, font=(FONT_NAME, "10", "bold"),bg=YELLOW)
my_label.grid(column=1, row=3)

timer_label = Label(text = "Timer", foreground=GREEN, font = (FONT_NAME, "50", "bold"),background=YELLOW)
timer_label.grid(column=1, row = 0)

button = Button(text = "Start", command=start_timer)
button.grid(column=0, row=2)

button_1 = Button(text="Reset", command=stop_timer)
button_1.grid(column=2, row=2)




window.mainloop()