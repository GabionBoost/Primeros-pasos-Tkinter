from tkinter import * 
from tkinter import messagebox
root = Tk()
root.title("Ventana 1")

def click():
    #messagebox.showwarning("Ventana 2", "Esto es una ventana que contiene una alerta")
    #messagebox.showinfo("Ventana 2", "Esto es una ventana que contiene un informacion")
    #messagebox.showerror("Ventana 2", "Esto es una ventana que contiene un error")
    respuesta = messagebox.askquestion("Ventana 2", "Esto es una ventana que contiene una pregunta ¿si o no?")
    if respuesta == "yes": 
        messagebox.showinfo("Respuesta", "Tu respuesta a sido afirmativa")
    else: messagebox.showinfo("Respuesta", "Tu respuesta a sido negativa")
    
    
button = Button(root, text="Cklickeame", command=click)
button.grid(row=0, column=0)

btnquit = Button(root, text="Cerrar", command=root.quit)
btnquit.grid(row=0, column=1)

root.mainloop()