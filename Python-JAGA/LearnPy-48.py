print()
print("|========================================|"
      "| Creating a GUI in Python "
      "||========================================|")
print()
from tkinter import *
root = Tk()
Button(root, text="white", bg="white", fg="black").pack(fill=X, padx=15)
Button(root, text="orange", bg="orange", fg="brown").pack(fill=X, pady=15, padx=15)
Button(root, text="Red", bg="red", fg="black").pack(fill=X, padx=15)
mainloop()