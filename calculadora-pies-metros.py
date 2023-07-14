from tkinter import *
root = Tk()
root.title("Calculadora Pies a Metros")

def calcular(*args):  #Definimos una funcion calcular que toma las teclas que le pasemos
    try:  #Intentamos convertir value en un float y hacemos los calculos
        value = float(pies.get())
        m = round((0.3048 * value * 10000 + 0.5) / 10000, 2)
        metros.set(m) #Set es cuando definimos un nuevo valor 
    except ValueError:
        metros.set("ERROR")
        
frame = Frame(root, padx=12, pady=3)
frame.grid(row=0, column=0)

pies = StringVar()
pies_input = Entry(frame, width=7, textvariable=pies)
pies_input.grid(row=0, column=1)

metros = StringVar()
Label(frame, textvariable=metros).grid(row=1, column=1)

Button(frame, text="Calcular", command=calcular).grid(row=2, column=2)

Label(frame, text="Pies").grid(row=0, column=0)
Label(frame, text="es igual a").grid(row=1, column=0)
Label(frame, text="metros").grid(row=1, column=2)

pies_input.focus()  #.focus() hace que seleccionemos algo al iniciar la ventana.
root.bind("<Return>", calcular)#sirve para indicar una tecla en especial, y lo pasamos a la funcion calcular()
root.mainloop()