from tkinter import *

root = Tk()
root.title("Ventana")

#Podemos hacer recuadros con LabelFrame(), no es necesario tener un texto ejemplo:
# frame = LabelFrame(root, text="Titulo", padx=10, pady=10, borderwidth=5)
frame = LabelFrame(root, padx=10, 
        pady=10, borderwidth=5, bg="black") #ademas con padx y pady asignamos los espacios que tendra el frame por dentro
frame.pack(padx=50, pady=50) #Lo renderizamos con los mismos y estos se asignaran hacia afuera del frame

l = Label(frame, text="Esto esta dentro de frame", fg="white", bg="black")
button = Button(frame, text="Exit", command=root.quit, fg="white", bg="black") #la nueva instruccion quit() cerrara nuestra interface 
l.pack()
button.pack()

root.mainloop()