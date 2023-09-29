from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
check_count = 0

IMAGE = 'tomato.png'



# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check_count, reps
    window.after_cancel(timer)
    check_count = 0
    reps = 0
    check_label.config(text='')
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(canvas_text, text='00:00')
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, check_count
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    check_label.config(text='✔' * check_count)
    if reps % 8 == 0:
        timer_label.config(text='Break', fg=PINK)
        count_timer(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text='Break', fg=GREEN)
        count_timer(short_break_sec)
    else:
        check_count += 1
        timer_label.config(text='Work', fg=RED)
        count_timer(work_sec)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_timer(count):
    global timer
    minutes = count // 60
    seconds = count % 60

    if seconds < 10:
        seconds = f'0{seconds}'
    if seconds == 0:
        seconds = '00'

    canvas.itemconfig(canvas_text, text=f'{minutes}:{seconds}')
    if count > 0:
        timer = window.after(1000, count_timer, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(400, 400)
window.title('Pomodoro')
window.config(padx=40, pady=20, bg=YELLOW)

bg = PhotoImage(file=IMAGE)

timer_label = Label(text='Timer', font=('Courier', 40, 'bold'), fg=GREEN, background=YELLOW)

timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=bg)
canvas.grid(row=1, column=1)

canvas_text = canvas.create_text(110, 130, text='00:00', font=('Courier', 25, 'bold'), fill='white')


start_button = Button(text='Start', background=YELLOW,highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

check_label = Label(text='', background=YELLOW, font=('Courier', 35, 'bold'), fg=GREEN)
check_label.grid(row=2, column=1)

reset_button = Button(text='Stop', background=YELLOW,highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()