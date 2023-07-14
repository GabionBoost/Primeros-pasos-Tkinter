from tkinter import *

root = Tk()
root.title("RadioButton")
root.geometry("400x200")

radio = IntVar()
radio.set(1)

# Radiobutton(root, text="Opcion 1", variable=radio, value=1).pack()
# Radiobutton(root, text="Opcion 2", variable=radio, value=2).pack()

Emociones = [
    ('Feliz', 'Feliz'),
    ('Triste', 'Triste'),
    ('Enojado', 'Enojado'),
    ('Inspirado', 'Inspirado')
]

E = StringVar()

for text, valor in Emociones:
    Radiobutton(root, text=text, variable=E, value=valor).pack()

Label(root, textvariable=E).pack()

root.mainloop()