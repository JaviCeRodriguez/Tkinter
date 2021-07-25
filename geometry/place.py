from tkinter import *

root = Tk()
root.title("Calculadora")

firstValueLabel = Label(root, text="Primer valor")
firstValueLabel.place(x=10, y=10)
firstValueEntry = Entry(root)
firstValueEntry.place(x=120, y=10)

secondValueLabel = Label(root, text="Segundo valor")
secondValueLabel.place(x=10, y=40)
secondValueEntry = Entry(root)
secondValueEntry.place(x=120, y=40)


def sumar(n1, n2):
    '''
    A partir de la suma de dos numeros, se sobreescribe el texto del label
    '''
    total = int(n1) + int(n2)
    totalLabel.config(text=total)

sumButton = Button(root, text="Sumar", command=lambda: sumar(firstValueEntry.get(), secondValueEntry.get()))
sumButton.place(x=10, y=70)

totalLabel = Label(root, text="")
totalLabel.place(x=120, y=70)

root.geometry("300x150+500+200")

root.mainloop()