# TkInter: Entorno gráfico (GUI) con Python 🐍
Un poco de lo que voy aprendiendo lo voy mostrando en este repositorio. *Todos los códigos están en los distintos módulos, acá muestro solo una parte de cada script hecho.*

Sientanse libres de proponer cambios o ejemplos de código mediante un **pull request**!

Algunos enlaces útiles para acompañar esto con teoría/documentación:
- [Documentación oficial (Inglés)](https://docs.python.org/3/library/tkinter.html)
- [Interfaces gráficas con Tkinter - Hektor Docs](https://docs.hektorprofe.net/python/interfaces-graficas-con-tkinter/)

---

## Creación de ventana básica
```py
from tkinter import *

root = Tk() # Instancia de la clase Tk en root
root.title("Soy un título") # Indico título para root
root.geometry("400x500") # Indico la dimensión

root.mainloop() # Loop para escuchar cambios
```

## Widgets (básicos)
### Labels
1° forma:

```py
label = Label(root, text="Hola mundo") # Creo la etiqueta label
label.pack() # Coloco la etiqueta label en la ventana root
```

2° forma:

```py
var = StringVar() # Creo una variable de tipo string
label2 = Label(root, textvariable=var) # Creo la etiqueta label2
var.set("Soy otro label") # Asigno la variable var con un texto
label2.pack() # Coloco la etiqueta label2 en la ventana root
```

### Buttons
Se pueden utilizar comandos e insertarlos en los botones de esta forma:
```py
def console_print():
    print("I'm a button")

# Creo un botón para cerrar la GUI y la ubico abajo
button = Button(root, text="QUIT", fg="red", command=quit)
button.pack(side=BOTTOM)

# Creo otro botón para que envie un mensaje por consola
msg_cmd = Button(root, text="Hola?", command=console_print)
msg_cmd.pack(side=TOP)
```

Otro ejemplo: Contador de segundos (ver `examples/count.py`)

### Frames
Son marcos que se pueden utilizar para envolver otros widgets.
```py
frame = Frame(root, bd=2, relief="groove", padx=10, pady=10)
frame.pack(side=BOTTOM)

leftframe = Frame(root, bd=2, relief="groove", padx=10, pady=10)
leftframe.pack(side=LEFT)

rightframe = Frame(root, bd=2, relief="groove", padx=10, pady=10)
rightframe.pack(side=RIGHT)
```

### Checkboxes
Podemos definir checkboxes de las siguientes maneras:
```py
var1 = IntVar()
var2 = IntVar()

# Utilizando place
Checkbutton(root, text="Hombre", variable=var1).place(x=50, y=50)
Checkbutton(root, text="Mujer", variable=var2).place(x=50, y=80)

# Utilizando grid
Checkbutton(root, text="Hombre", variable=var1).grid(row=0, sticky=W)
Checkbutton(root, text="Mujer", variable=var2).grid(row=1, sticky=W)
```

Usando place es más intuitivo, grid es un poco más "complejo". Lo veremos más adelante


## Radio buttons
Similar a los checkboxes, solo que acá comparten la variable entera:
```py
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
```

## Entries
Simples campos de texto:

```py
entry1 = Entry(root)
entry2 = Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
```

## Dropdowns
```py
variable = StringVar(root)
variable.set("1") # Le doy un valor inicial (puede ser cualquiera)

a = OptionMenu(root, variable, "1", "2", "3", "4", "5")
a.pack()
```


## Geometry Management
### Pack
Con el método pack, nos preocupamos nada más de que nos pueda colocar el widget en la ventana según los parámetros que les pasemos.

```py
a = Label(root, text="Python", bg="green", fg="white")
a.pack(fill=X, padx=10, pady=10) # se expande en X y tiene padding de 10 en X y en Y

a = Label(root, text="JavaScript", bg="yellow", fg="black")
a.pack(fill=X, side=LEFT) # se expande en X y lo ubico a la izquierda

a = Label(root, text="Java", bg="red", fg="white")
a.pack(fill=X) # se expande en X

a = Label(root, text="Golang", bg="skyblue", fg="white")
a.pack(fill=Y) # se expande en Y
```

