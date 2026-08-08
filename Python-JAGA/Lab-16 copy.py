from tkinter import *
from tkinter import messagebox
import pymysql

# ---------------------- DATABASE ---------------------- #
def Dbase():
    global conn, cursor

    conn = pymysql.connect(
        host="localhost",
        user="Jaga",
        password="jaga@123",
        database="python"
    )

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS member(
            mem_id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL
        )
    """)

    cursor.execute(
        "SELECT * FROM member WHERE username=%s AND password=%s",
        ("admin", "admin")
    )

    if cursor.fetchone() is None:
        cursor.execute(
            "INSERT INTO member(username,password) VALUES(%s,%s)",
            ("admin", "admin")
        )
        conn.commit()


# ---------------------- LOGIN ---------------------- #
def LoginFun(event=None):
    Dbase()

    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Fields can't be empty", fg="red")
        conn.close()
        return

    cursor.execute(
        "SELECT * FROM member WHERE username=%s AND password=%s",
        (USERNAME.get(), PASSWORD.get())
    )

    if cursor.fetchone():
        USERNAME.set("")
        PASSWORD.set("")
        lbl_text.config(text="")
        conn.close()
        HomeScreen()
    else:
        lbl_text.config(
            text="Invalid Username or Password",
            fg="red"
        )
        PASSWORD.set("")
        conn.close()


# ---------------------- HOME SCREEN ---------------------- #
def HomeScreen():
    root.withdraw()

    home = Toplevel(root)
    home.title("Home")

    width = 500
    height = 300

    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    home.geometry(f"{width}x{height}+{x}+{y}")
    home.resizable(False, False)

    Label(
        home,
        text="Login Successful!",
        font=("Arial", 20, "bold"),
        fg="green"
    ).pack(pady=40)

    Button(
        home,
        text="Logout",
        width=20,
        command=lambda: Logout(home)
    ).pack(pady=20)


# ---------------------- LOGOUT ---------------------- #
def Logout(home):
    home.destroy()
    root.deiconify()


# ---------------------- MAIN WINDOW ---------------------- #
root = Tk()
root.title("Login Application")

width = 600
height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) // 2

root.geometry(f"{width}x{height}+{x}+{y}")
root.resizable(False, False)

# ---------------------- VARIABLES ---------------------- #
USERNAME = StringVar()
PASSWORD = StringVar()

# ---------------------- FRAMES ---------------------- #
top_frame = Frame(root, bd=2, relief=RIDGE)
top_frame.pack(side=TOP, fill=X)

form_frame = Frame(root)
form_frame.pack(pady=40)

# ---------------------- TITLE ---------------------- #
Label(
    top_frame,
    text="Login Screen",
    font=("Arial", 18, "bold")
).pack(fill=X, pady=10)

# ---------------------- USERNAME ---------------------- #
Label(
    form_frame,
    text="Username :",
    font=("Arial", 14)
).grid(row=0, column=0, padx=10, pady=10, sticky=E)

Entry(
    form_frame,
    textvariable=USERNAME,
    font=("Arial", 14),
    width=25
).grid(row=0, column=1, pady=10)

# ---------------------- PASSWORD ---------------------- #
Label(
    form_frame,
    text="Password :",
    font=("Arial", 14)
).grid(row=1, column=0, padx=10, pady=10, sticky=E)

Entry(
    form_frame,
    textvariable=PASSWORD,
    show="*",
    font=("Arial", 14),
    width=25
).grid(row=1, column=1, pady=10)

# ---------------------- MESSAGE LABEL ---------------------- #
lbl_text = Label(
    form_frame,
    text="",
    font=("Arial", 12)
)
lbl_text.grid(row=2, column=0, columnspan=2)

# ---------------------- LOGIN BUTTON ---------------------- #
btn_login = Button(
    form_frame,
    text="Login",
    width=20,
    font=("Arial", 12, "bold"),
    command=LoginFun
)

btn_login.grid(row=3, column=0, columnspan=2, pady=20)

# Press Enter to Login
root.bind("<Return>", LoginFun)

# ---------------------- RUN ---------------------- #
root.mainloop()