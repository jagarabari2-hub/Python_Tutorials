import tkinter as tk

root = tk.Tk()
root.title("Stop Watch")

time_label = tk.Label(root, text="00:00:00", font=("Consolas", 25, "bold"), fg="blue")
time_label.pack(padx=20, pady=20)

def start_stopwatch():
    global running
    if not running:
        running = True
        update_stopwatch()

def stop_stopwatch():
    global running
    running = False

def reset_stopwatch():
    global running, elapsed_time
    running = False
    elapsed_time = 0
    time_label.config(text="00:00:00")

def update_stopwatch():
    global elapsed_time
    if running:
        elapsed_time += 1
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        time_label.after(1000, update_stopwatch)

running = False
elapsed_time = 0

# All Btn Have In One Row With 10 Each Padding like that Start   Stop   Reset
start_btn = tk.Button(root, text="START", bg="Blue", fg="White", command=start_stopwatch)
stop_btn = tk.Button(root, text="STOP", bg="Red", fg="White", command=stop_stopwatch)
reset_btn = tk.Button(root, text="RESET", bg="Black", fg="White", command=reset_stopwatch)
start_btn.pack(side="left", padx=10, pady=10)
stop_btn.pack(side="left", padx=10, pady=10)
reset_btn.pack(side="left", padx=10, pady=10)


root.mainloop()                                                      
