from tkinter import *

root = Tk()
root.title("Soy un título")
root.geometry("400x500")

label = Label(root, text="Hola mundo") # Creo la etiqueta label
label.pack() # Coloco la etiqueta label en la ventana root

# Otra forma de crear una etiqueta
var = StringVar() # Creo una variable de tipo string
label2 = Label(root, textvariable=var) # Creo la etiqueta label2
var.set("Soy otro label") # Asigno la variable var con un texto
label2.pack() # Coloco la etiqueta label2 en la ventana root

root.mainloop()