print("|========================================|"
      "| Display Real Clock "
      "||========================================|")
print()
import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time, fg="red")
    time_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

time_label = tk.Label(root, font=("Consolas", 25, "bold"))
time_label.pack(padx=20, pady=20)
text_label = tk.Label(root, text="Hello Jaga", font=("Arial", 20, "bold"), fg="Green")
text_label.pack(pady=10)

update_time()

root.mainloop()