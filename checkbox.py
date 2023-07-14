from tkinter import *

root = Tk()
root.title("Checkbox prueba")
root.geometry("500x500")

def mostrar():
    Label(root, text=var.get()).pack()

var = StringVar()
var.set("si")

Checkbutton(root, text="Checkbox generico", variable=var, onvalue="si", offvalue="Cualquiercosa").pack()

Button(root, text="Click", command=mostrar).pack()

root.mainloop()