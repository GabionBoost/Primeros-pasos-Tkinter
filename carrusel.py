from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Carrusel de Imagenes")

img1 = ImageTk.PhotoImage(Image.open("images/paisaje1.jpeg"))
img2 = ImageTk.PhotoImage(Image.open("images/paisaje2.jpeg"))
img3 = ImageTk.PhotoImage(Image.open("images/paisaje3.jpeg"))
img4 = ImageTk.PhotoImage(Image.open("images/paisaje4.jpeg"))

images = [img1, img2, img3, img4]

def adelante(n):
   global label
   global retroceder
   global avanzar
   
   label.grid_forget()
   label = Label(root, image=images[n])
   label.grid( row=0, column=0, columnspan=3 )
   if n != 0:
       retroceder.grid_forget()
       retroceder = Button(root, text="<-", command=lambda: adelante(n-1))
       retroceder.grid(row=1, column=0)
   else:
       retroceder.grid_forget()
       retroceder = Button(root, text="N/A", state=DISABLED)
       retroceder.grid(row=1, column=0)
   
   if n != 3:    
       avanzar.grid_forget()
       avanzar = Button(root, text="->", command=lambda: adelante(n+1))
       avanzar.grid(row=1, column=2)
   else:
       avanzar.grid_forget()
       avanzar = Button(root, text="N/A", state=DISABLED)
       avanzar.grid(row=1, column=2)

   
retroceder = Button(root, text="N/A", state=DISABLED)
avanzar = Button(root, text="->", command=lambda: adelante(1))

label = Label( root, image=img1 )
label.grid( row=0, column=0, columnspan=3 )

retroceder.grid(row=1, column=0)
avanzar.grid(row=1, column=2)

root.mainloop() 