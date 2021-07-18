# TkInter: Entorno gráfico (GUI) con Python 🐍

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