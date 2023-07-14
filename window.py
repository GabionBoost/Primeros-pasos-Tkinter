from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Ventanas")

# Solucion 1
# def open():
#     img = ImageTk.PhotoImage(Image.open("images/paisaje1.jpeg"))
#     top = Toplevel()
#     top.title("Ventana Nueva")
#     Label(top, text="Soy texto en una nueva ventana").pack()
#     Label(top, image=img).pack()
#     top.mainloop()

#Solucion 2
# def open():
#     global img
#     img = ImageTk.PhotoImage(Image.open("images/paisaje1.jpeg"))
#     top = Toplevel()
#     top.title("Ventana Nueva")
#     Label(top, text="Soy texto en una nueva ventana").pack()
#     Label(top, image=img).pack()

#Solucion 3
def open(img):
    top = Toplevel()
    top.title("Ventana Nueva")
    Label(top, text="Soy texto en una nueva ventana").pack()
    Label(top, image=img).pack()

img = ImageTk.PhotoImage(Image.open("images/paisaje1.jpeg"))
Button(root, text="Nueva Imagen", command=lambda: open(img)).pack()

root.mainloop()