from tkinter import *

def count(label, counter):
    counter = 0
    def count_up(counter):
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count_up, counter)
    count_up(counter)

root = Tk()
root.title("Counting Seconds")

label = Label(root, fg="green")
label.pack()
count(label, 0)

button = Button(root, text='Stop', width=25, command=root.destroy)
button.pack()

root.mainloop()