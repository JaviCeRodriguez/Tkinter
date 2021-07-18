from tkinter import *

root = Tk()
root.title("Soy un título")
root.geometry("200x200")

def console_print():
    print("I'm a button")

# Creo un botón para cerrar la GUI y la ubico abajo
button = Button(root, text="QUIT", fg="red", command=quit)
button.pack(side=BOTTOM)

# Creo otro botón para que envie un mensaje por consola
msg_cmd = Button(root, text="Hola?", command=console_print)
msg_cmd.pack(side=TOP)

root.mainloop()