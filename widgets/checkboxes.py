from tkinter import *

root = Tk()
root.title("Soy un título")
root.geometry("300x200")

var1 = IntVar()
var2 = IntVar()

# Utilizando place
# Checkbutton(root, text="Hombre", variable=var1).place(x=50, y=50)
# Checkbutton(root, text="Mujer", variable=var2).place(x=50, y=80)

# Utilizando grid
Checkbutton(root, text="Hombre", variable=var1).grid(row=0, sticky=W)
Checkbutton(root, text="Mujer", variable=var2).grid(row=1, sticky=W)

root.mainloop()