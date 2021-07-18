from tkinter import *

def clicked():
      res = "Welcome to " + txt.get()
      lbl.configure(text= res)


root = Tk()
root.title("Welcome to 🤔")
root.geometry("300x50")

lbl = Label(root, text="Hello")
lbl.grid(column=0, row=0)

txt = Entry(root,width=10)
txt.grid(column=1, row=0)

btn = Button (root, text="Enter", command=clicked)
btn.grid(column=2, row=0)

root.mainloop()