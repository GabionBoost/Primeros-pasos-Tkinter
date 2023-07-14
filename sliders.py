from tkinter import *

root = Tk()
root.title("Sliders Prueba")

def enviar():
    h = horizontal.get()
    v = vertical.get()
    print(h, " ", v)

vertical = Scale(root, from_=0, to=200, command=lambda x: enviar())
vertical.pack()

horizontal = Scale(root, from_=0, to=200, command=lambda x: enviar())
horizontal.pack()

Button(root, text="Enviar posicion", command=enviar).pack()



root.mainloop()