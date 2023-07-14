from tkinter import *

root = Tk()
root.title("Option menu")
root.geometry("500x500")

def enviar():
    Label(root, text=value.get()).pack()

lista = [ "Option 1", "Option 2", "Option 3" ]

value = StringVar(); value.set(lista[0])

OptionMenu(root, value, *lista).pack()

Button(root, text="click", command=enviar).pack()

root.mainloop()