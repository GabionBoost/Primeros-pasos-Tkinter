from tkinter import *

root = Tk()
root.title("Ventana")
root.geometry("500x500")

e = Entry(root, width=40 ) #Esto es un input se mostrara una interfaz donde el usuario pondra lo que quiera
e.pack()
e.insert(0, "Enter text: ") #Esto es el texto por defecto, tener en cuenta que esto esta escrito de base

def click():
    text = e.get() #con la instruccion get() tomamos el valor que asignamos antes
    l = Label(root, text=text) #con esto creamos un label que tiene nuestro texto que obtuvimos con get() 
    l.pack()
    e.delete(0, END) #Esto elimara el texto una vez termine la instruccion
    # l.configure(text=text) # esto configuraba el texto de l1, haciendo que solo aparesca una vez 

button = Button( root, text="Click", command=click)
button.pack()

# l1 = Label(root, text="Etiqueta")
# l1.pack()
    
root.mainloop()