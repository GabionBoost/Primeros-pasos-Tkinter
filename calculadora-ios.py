from tkinter import *

root = Tk()
root.title("Calculadora")
root.configure(bg="#333333")
root.geometry("386x150")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

equation = StringVar()

def press(num):
    equation.set(equation.get() + str(num))
    
def equalpress():
    try:
        total = str(equation.get())
        equation.set(eval(total))
    except: 
        equation.set("ERROR")
        
def clearpress():
    equation.set("")

espression_entry = Entry(root, textvariable=equation)
espression_entry.grid(row=0, columnspan=4, sticky="nswe")

button7 = Button(root, text="7", fg="#fff", bg="#666", command=lambda: press(7))
button7.grid(row=1, column=0, sticky="nswe")

button8 = Button(root, text="8", fg="#fff", bg="#666", command=lambda: press(8))
button8.grid(row=1, column=1, sticky="nswe")

button9 = Button(root, text="9", fg="#fff", bg="#666", command=lambda: press(9))
button9.grid(row=1, column=2, sticky="nswe")

button4 = Button(root, text="4", fg="#fff", bg="#666", command=lambda: press(4))
button4.grid(row=2, column=0, sticky="nswe")

button5 = Button(root, text="5", fg="#fff", bg="#666", command=lambda: press(5))
button5.grid(row=2, column=1, sticky="nswe")

button6 = Button(root, text="6", fg="#fff", bg="#666", command=lambda: press(6))
button6.grid(row=2, column=2, sticky="nswe")

button1 = Button(root, text="1", fg="#fff", bg="#666", command=lambda: press(1))
button1.grid(row=3, column=0, sticky="nswe")

button2 = Button(root, text="2", fg="#fff", bg="#666", command=lambda: press(2))
button2.grid(row=3, column=1, sticky="nswe")

button3 = Button(root, text="3", fg="#fff", bg="#666", command=lambda: press(3))
button3.grid(row=3, column=2, sticky="nswe")

button0 = Button(root, text="0", fg="#fff", bg="#666", command=lambda: press(0))
button0.grid(row=4, column=0, sticky="nswe", columnspan=2)

buttonDecimal = Button(root, text=".", fg="#fff", bg="#666", command=lambda: press("."))
buttonDecimal.grid(row=4, column=2, sticky="nswe")

sumar = Button(root, text="+", fg="#fff", bg="orange", command=lambda: press("+"))
sumar.grid(row=1, column=3, sticky="nswe")

restar = Button(root, text="-", fg="#fff", bg="orange", command=lambda: press("-"))
restar.grid(row=2, column=3, sticky="nswe")

multiplicar = Button(root, text="*", fg="#fff", bg="orange", command=lambda: press("*"))
multiplicar.grid(row=3, column=3, sticky="nswe")

dividir = Button(root, text="/", fg="#fff", bg="orange", command=lambda: press("/"))
dividir.grid(row=4, column=3, sticky="nswe")

igual = Button(root, text="=", fg="#fff", bg="orange", command=equalpress)
igual.grid(row=5, column=3, sticky="nswe")

clear = Button(root, text="clear", fg="#fff", bg="#999", command=clearpress)
clear.grid(row=5, column=2, sticky="nswe")
root.mainloop()

