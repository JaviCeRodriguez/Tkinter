# TkInter: Entorno gráfico (GUI) con Python 🐍
Un poco de lo que voy aprendiendo lo voy mostrando en este repositorio. *Todos los códigos están en los distintos módulos, acá muestro solo una parte de cada script hecho.*

Sientanse libres de proponer cambios o ejemplos de código mediante un **pull request**!

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