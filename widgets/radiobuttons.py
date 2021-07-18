from tkinter import *

root = Tk()
root.title("Soy un título")
root.geometry("300x300")

# Una variable entera para los radio buttons
radiovalue = IntVar()

# Creo los radio buttons
radio1 = Radiobutton(root, text="Enero", variable=radiovalue, value=1)
radio2 = Radiobutton(root, text="Febrero", variable=radiovalue, value=2)
radio3 = Radiobutton(root, text="Marzo", variable=radiovalue, value=3)

# Los ubico con grid (prueben sin el argumento sticky)
radio1.grid(row=0, column=0, sticky=W)
radio2.grid(row=1, column=0, sticky=W)
radio3.grid(row=2, column=0, sticky=W)

root.mainloop()