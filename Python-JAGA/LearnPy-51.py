print()
print("|========================================|"
      "| Event Handling "
      "||========================================|")
print()
from tkinter import *
def handler1():
    print("Button 1 was clicked")
def handler2():
    print("Button 2 was clicked")
def handler3():
    print("Button 3 was clicked")
root = Tk(className="Event")
b1 = Button(root, text="Button 1", bg="white", fg="black", command=handler1).pack(fill=X, padx=15)
b2 = Button(root, text="Button 2", bg="orange", fg="brown", command=handler2).pack(fill=X, pady=15, padx=15)
b3 = Button(root, text="Button 3", bg="red", fg="white", command=handler3).pack(fill=X, padx=15)
mainloop()