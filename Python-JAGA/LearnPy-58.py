print()
print("|========================================|"
      "| GUI Button "
      "||========================================|")
print()
import pymysql
from tkinter import * 
def handler():
    con = pymysql.connect(
        host="localhost",
        user="Jaga",
        password="jaga@123",
        database="python"
    )
    print("Connection Successful")
root = Tk(className="Button")
Button(root, text="white", bg="cyan", fg="White", command=handler).place(x=20, y=30, width=160, height=30)
mainloop()