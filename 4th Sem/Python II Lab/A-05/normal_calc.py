from tkinter import *
import math

def click(value):
    current = e1.get()

    if value == 'C':
        e1.delete(0, END)

    elif value == 'CE':
        e1.delete(len(current)-1, END)

    elif value == '=':
        try:
            current = current.replace('\u00F7', '/').replace('\u00D7', '*').replace('x²', '**2')
            result = str(eval(current))
            e1.delete(0, END)
            e1.insert(0, result)
        except Exception:
            e1.delete(0, END)
            e1.insert(0, "Error")

    elif value == '+/-':
        if current:
            if current[0] == '-':
                e1.delete(0, 1)
            else:
                e1.insert(0, '-')

    elif value == '1/x':
        try:
            result = str(1 / float(current))
            e1.delete(0, END)
            e1.insert(0, result)
        except Exception:
            e1.delete(0, END)
            e1.insert(0, "Error")

    elif value == 'x²':
        try:
            result = str(float(current) ** 2)
            e1.delete(0, END)
            e1.insert(0, result)
        except Exception:
            e1.delete(0, END)
            e1.insert(0, "Error")

    elif value == '√x':
        try:
            result = str(math.sqrt(float(current)))
            e1.delete(0, END)
            e1.insert(0, result)
        except Exception:
            e1.delete(0, END)
            e1.insert(0, "Error")

    else:
        e1.insert(END, value)

t = Tk()
t.geometry("385x380")
t.resizable(False, False)
t.title("Normal Calculator")

e1 = Entry(t, font=('Georgia', '20', 'bold'))
e1.grid(row=0, column=0, columnspan=4, sticky=W)

l = ['%', 'CE', 'C', '\u2BBD', '1/x', 'x²', '√x', '\u00F7', '7', '8', '9', '\u00D7', 
     '4', '5', '6', '-', '1', '2', '3', '+', '+/-', '0', '.', '=']

row1 = 2
col1 = 0

for i in l:
    b = Button(t, text=i, width=11, height=3, command=lambda b=i: click(b))
    b.grid(row=row1, column=col1)
    col1 += 1
    if col1 > 3:
        col1 = 0
        row1 += 1

t.mainloop()
