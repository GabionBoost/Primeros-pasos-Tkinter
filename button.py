from tkinter import *

root = Tk()
root.title("Ventana")

label = Label(root, text="Funciono") #Creamos un texto 
def click():  #En esta funcion ejecutamos para que se pinte el texto
    return label.pack()

#Creamos un boton que tendra el commando de click y sin los parentesis no se ejecuta 
#fg seria para el color de el frente del boton
#bg seria para el fondo del mismo
button = Button( root, text="Click", command=click, fg="blue", bg="black" )
button.pack()

root.mainloop()