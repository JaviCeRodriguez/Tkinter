from tkinter import *

root = Tk()
root.title("Soy un título")
root.geometry("400x500")

Label(root, text="Usuario: ").grid(row=0, column=0)
Label(root, text="Contraseña: ").grid(row=1, column=0)

entry1 = Entry(root)
entry2 = Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.mainloop()