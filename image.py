from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Imagenes")

#img = Image.open("R.jpeg")
#img.show()

img = ImageTk.PhotoImage(Image.open("R.jpeg"))
label = Label(image=img)

label.pack()

root.mainloop()