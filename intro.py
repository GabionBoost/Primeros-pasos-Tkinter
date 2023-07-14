from tkinter import *

root = Tk() 
root.title("Hola Ventana") #Esto indica el titulo de mi ventana
root.geometry("500x500") #Esto indica el ancho y la altura de la ventana

#Asignamos Label() a una variable referenciando a Tk(ventana) y mostrar un texto
label = Label(root, text="Hola esto es una etiqueta!!")  
label2 = Label(root, text="Y esto esta en la columna 1 fila 0")     

#Es la funcion .grid() podemos mostrar los textos en filas y columnas 
#Tener en cuenta que sin importar la columna final, si no hay contenido entre medio no se muestra,
#tambien las columnas tienen su ancho en base a el contenido de estas
label.grid(row=0, column=0)
label2.grid(row=0, column=1)

root.mainloop()
