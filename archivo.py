from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Archivos")

# root_filename = filedialog.askopenfilename( title="Elije una foto", filetypes=(("Archivos JPEG", "*.jpeg"), ("Todos", "*")) )
# img = ImageTk.PhotoImage(Image.open(root_filename))

# Label(root, text=root_filename).pack()
# Label(root, image=img).pack()
rep = 0

def click():
    global img, root_filename, l1, l2, rep, buscar
    if rep == 0:
        root_filename = filedialog.askopenfilename( title="Elije una foto", filetypes=(("Archivos JPEG", "*.jpeg"), ("Todos", "*")) )
        img = ImageTk.PhotoImage(Image.open(root_filename))
        l1 = Label(root, text=root_filename)
        l2 = Label(root, image=img)
        rep += 1
        buscar.pack_forget()
        buscar = Button(root, text="Buscar otra imagen", command=click)
        buscar.pack()
        l1.pack()
        l2.pack()
    elif rep == 1:
        l1.destroy()
        l2.destroy()
        rep = 0
        click()

    
    
buscar = Button(root, text="Buscar imagen", command=click)
buscar.pack()

root.mainloop()
