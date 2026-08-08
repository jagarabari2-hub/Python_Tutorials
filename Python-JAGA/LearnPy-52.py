print()
print("|========================================|"
      "| File Open "
      "||========================================|")
print()
from tkinter import *
from tkinter.filedialog import askopenfilename
def handler():
    print(askopenfilename())

root = Tk(className="File open dialog")
root.geometry('250x30')
Button(text='Open file', command=handler).pack()
root.mainloop()