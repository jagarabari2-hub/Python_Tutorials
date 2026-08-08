print()
print("|========================================|"
      "| Using 'place()' method "
      "||========================================|")
print()
import tkinter
import random

root = tkinter.Tk(className="Layout")
root.geometry("200x250+50+30")

lang = ['Python', 'Ruby', 'C#', 'JavaScript', 'PHP']
labels = range(5)
i = 0
while i < 5:
    c = [random.randrange(256) for x in range(3)]
    ct_hex = '%02x%02x%02x' % tuple(c)
    bright = int(round(0.8 * c[0] + 0.01 * c[1] + 0.2 * c[2]))
    bg_colour = '#' + "".join(ct_hex)
    b = tkinter.Button(root, text=lang[i], fg='white' if bright < 100 else 'black', bg=bg_colour)
    b.place(x = 40, y = 30 + i * 40, width = 120, height = 25)
    i+=1

root.mainloop()