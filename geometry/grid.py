from tkinter import *

root = Tk()

colours = ('red','green','blue','white','orange')

for c, x in enumerate(colours):
    Label(text=x, relief=RIDGE, width=20).grid(row=c, column=0)
    Entry(bg=x, relief=SUNKEN, width=10).grid(row=c, column=1)

root.mainloop()