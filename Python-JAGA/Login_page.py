print("|========================================|"
      "| LOGIN APPLICATION "
      "||========================================|")
print()
# Login Page with id and password and login and btn when click on login button it will check the id and password if it is correct then it will show the home page otherwise it will show the error message check id password with database table pymysql
from logging import root

import pymysql
import tkinter as tk
from tkinter import StringVar, messagebox

def Dbase():
    global conn, cursor
    conn = pymysql.connect(host="localhost", user="Jaga", password="jaga@123", database="python")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS logs(log_id INT AUTO_INCREMENT PRIMARY KEY, username TEXT, password TEXT)")
    conn.commit()   
    cursor.execute("SELECT * FROM logs WHERE username=%s AND password=%s", (username, password))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO logs(username, password) VALUES(%s, %s)", (username, password))
    conn.commit()

def Login(_event=None):
    global username, password
    username = entry_username.get()
    password = entry_password.get()
    Dbase()
    cursor.execute("SELECT * FROM logs WHERE username=%s AND password=%s", (username, password))
    if cursor.fetchone():
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        root.destroy()
        HomeScreen()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def HomeScreen():
    home_screen = tk.Tk()
    home_screen.title("Home Screen")
    home_screen.geometry("400x300")
    label_welcome = tk.Label(home_screen, text="Welcome to the Home Screen!", font=("Arial", 16))
    label_welcome.pack(pady=50)
    home_screen.mainloop()

def Logout():
    messagebox.showinfo("Logout", "You have been logged out.")
    root.destroy()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Login Page")
root.geometry("600x400")
root.resizable(False, False)

entry_username = StringVar()
entry_password = StringVar()


top_frame = tk.Frame(root, bd=2, relief=tk.RIDGE)
top_frame.pack(side=tk.TOP, fill=tk.X)

form_frame = tk.Frame(root)
form_frame.pack(pady=40)


tk.Label(
    top_frame,
    text="Login Screen",
    font=("Arial", 18, "bold")
).pack(fill=tk.X, pady=10)


tk.Label(
    form_frame,
    text="Username :",
    font=("Arial", 14)
).grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

tk.Entry(
    form_frame,
    textvariable=entry_username,
    font=("Arial", 14),
    width=25
).grid(row=0, column=1, pady=10)


tk.Label(
    form_frame,
    text="Password :",
    font=("Arial", 14)
).grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

tk.Entry(
    form_frame,
    textvariable=entry_password,
    show="*",
    font=("Arial", 14),
    width=25
).grid(row=1, column=1, pady=10)


lbl_text = tk.Label(
    form_frame,
    text="",
    font=("Arial", 12)
)
lbl_text.grid(row=2, column=0, columnspan=2)


btn_login = tk.Button(
    form_frame,
    text="Login",
    width=20,
    font=("Arial", 12, "bold"),
    command=Login
)

btn_login.grid(row=3, column=0, columnspan=2, pady=30)

# Press Enter to Login
root.bind("<Return>", Login)


root.mainloop()

