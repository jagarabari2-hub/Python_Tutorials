print("|========================================|"
      "| Login Application "
      "||========================================|")
print()
from tkinter import *
import pymysql

root = Tk()
root.title("Login Application")
width = 600
height = 400
app_width = root.winfo_screenwidth()
app_height = root.winfo_screenheight()
xaxis = (app_width / 2) - (width / 2)
yaxis = (app_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, xaxis, yaxis))
root.resizable(0, 0)
####################### METHODS ##########################
def Dbase():
    global conn, cursor
    conn = pymysql.connect(host="localhost", user="root", password="", database="python")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (`username`, `password`) VALUES ('admin', 'admin')")
        conn.commit()

def LoginFun(event=None):
    Dbase()

    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Fields can't be empty", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = %s AND `password` = %s", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeScreen()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")

def HomeScreen():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Login Screen")
    width = 600
    height = 500
    app_width = root.winfo_screenwidth()
    app_height = root.winfo_screenheight()
    xaxis = (app_width / 2) - (width / 2)
    yaxis = (app_height / 2) - (height / 2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d+" % (width, height, xaxis, yaxis))
    lbl_home = Label(Home, text="Login Successful!", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)

def Back():
    Home.destroy()
    root.deiconify()

####################### VARIABLES ##########################
USERNAME = StringVar()
PASSWORD = StringVar()

####################### FRAMES ##########################
Top = Frame(root, bd=2, relief=RIDGE)
Top.pack(side=TOP, fill=X) 
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

####################### LABELS ##########################
lbl_title = Label(Top, text = "Login Screen", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

####################### ENTRY WIDGETS ##########################
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)

####################### BUTTONS WIDGETS ##########################
btn_login = Button(Form, text="Login", width=45, command=LoginFun)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', LoginFun)