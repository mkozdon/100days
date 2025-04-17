import tkinter as tk


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMG_PATH = "Day 28\\tomato.png"
CHECKMARK = "✓"
is_running = False
reps = 0
timer_id = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global is_running
    is_running = False
    window.after_cancel(timer_id)
    canvas.itemconfig(timer, text="00:00")
    check_label["text"] = ""
    reps = 0
    start_timer()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global is_running
    global reps

    reps += 1
    short_sec = SHORT_BREAK_MIN * 60
    work_sec = WORK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    if is_running:
        return

    if reps % 2 != 0:
        count_down(work_sec)
        main_label["text"] = "Work"
    if reps in range(2, 8, 2):
        mark = int(reps / 2)
        count_down(short_sec)
        main_label["text"] = "Break"
    if reps == 8:
        count_down(long_sec)
        main_label["text"] = "Break"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global is_running
    global timer_id
    is_running = True
    text = f"{int(count/60):02d}:{count % 60:02d}"
    canvas.itemconfig(timer, text=text)
    if count > 0:
        timer_id = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_label["text"] = CHECKMARK * int(reps / 2)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()

window.title("Pomodoro")
# window.minsize(250, 150)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file=IMG_PATH)
canvas.create_image(100, 112, image=tomato)

timer = canvas.create_text(
    100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white"
)
main_label = tk.Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
check_label = tk.Label(text="", font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW)
start = tk.Button(text="Start", command=start_timer)
reset = tk.Button(text="Reset", command=reset_timer)

start.grid(column=0, row=2)
reset.grid(column=2, row=2)
check_label.grid(column=1, row=3)
main_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)

window.mainloop()
