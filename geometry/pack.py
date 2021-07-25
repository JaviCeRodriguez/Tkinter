from tkinter import *

root = Tk()

a = Label(root, text="Python", bg="green", fg="white")
a.pack(fill=X, padx=10, pady=10)

a = Label(root, text="JavaScript", bg="yellow", fg="black")
a.pack(fill=X, side=LEFT)

a = Label(root, text="Java", bg="red", fg="white")
a.pack(fill=X)

a = Label(root, text="Golang", bg="skyblue", fg="white")
a.pack(fill=Y)

root.mainloop()