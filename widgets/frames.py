from tkinter import *

root = Tk()
root.title("Soy un título")
root.geometry("300x300")

# Creo varios frames
frame = Frame(root, bd=2, relief="groove", padx=10, pady=10)
frame.pack(side=BOTTOM)
leftframe = Frame(root, bd=2, relief="groove", padx=10, pady=10)
leftframe.pack(side=LEFT)
rightframe = Frame(root, bd=2, relief="groove", padx=10, pady=10)
rightframe.pack(side=RIGHT)

# Creo botones para colocar dentro de los frames
btn1 = Button(leftframe, text="Boton 1", fg="white", bg="black")
btn1.pack(side=LEFT)
btn2 = Button(rightframe, text="Boton 2", fg="red", bg="yellow")
btn2.pack(side=RIGHT)
btn3 = Button(frame, text="Boton 3", fg="blue", activebackground="green")
btn3.pack(side=RIGHT)

root.mainloop()