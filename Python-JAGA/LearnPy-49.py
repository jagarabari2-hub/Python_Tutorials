print()
print("|========================================|"
      "| The Grid Layout Manager "
      "||========================================|")
print()
from tkinter import *
I = ['Name', 'Country', 'Contact', 'Percentage', 'District', 'Address']
root = Tk(className="Layout")
i = 0
for x in I:
    Label(text=x, width=20) .grid(row=i, column=0)
    Entry(width=20) .grid(row=i, column=1)
    i+=1
Button(text="Submit", width=17) .grid(row=i, column=1)
root.mainloop()