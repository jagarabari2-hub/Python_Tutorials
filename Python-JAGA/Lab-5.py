print("|========================================|"
      "| GUI "
      "||========================================|")
print()
from tkinter import *
labels = 'Name', 'Address', 'Country', 'Experience'
def createForm(r, labels):
    e = []
    for label in labels:
        rw = Frame(r)
        l = Label(rw, width=15, text=label, anchor='w')
        entry = Entry(rw)
        rw.pack(side=TOP, fill=X, padx=5, pady=5)
        l.pack(side=LEFT)
        entry.pack(side=RIGHT, expand=YES, fill=X)
        e.append((label, entry))
    return e
def get(e):
    for x in e:
        label = x[0]
        text_sharing = x[1].get()
        print(label+':', text_sharing)

if __name__ == '__main__':
    root = Tk()
    entries = createForm(root, labels)
    root.bind('<Return>', (lambda event, e=entries: get(e)))
    btn1 = Button(root, text='Display', command=(lambda e=entries: get(e)))
    btn1.pack(side=LEFT, padx=5, pady=5)
    btn2 = Button(root, text='Stop', command=root.quit)
    btn2.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()