from tkinter import *

root = Tk()
root.title("Soy un título")
root.geometry("400x500")

variable = StringVar(root)
variable.set("1") # Le doy un valor inicial (puede ser cualquiera)

a = OptionMenu(root, variable, "1", "2", "3", "4", "5")
a.pack()

def print_value():
    print(variable.get())
    root.quit()

btn1 = Button(root, text="Ok!", command=print_value)
btn1.pack()

root.mainloop()