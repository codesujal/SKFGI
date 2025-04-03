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
            current = current.replace('\u00F7', '/').replace('\u00D7', '*').replace('^', '**')
            result = str(eval(current))
            e1.delete(0, END)
            e1.insert(0, result)
        except:
            e1.delete(0, END)
            e1.insert(0, "Error")

    elif value == 'π':
        e1.insert(END, str(math.pi))

    elif value == 'n!':
        try:
            result = str(math.factorial(int(current)))
            e1.delete(0, END)
            e1.insert(0, result)
        except:
            e1.delete(0, END)
            e1.insert(0, "Error")

    elif value in ['sin', 'cos', 'tan', 'cosec', 'sec', 'cot']:
        try:
            num = float(current)
            radians = math.radians(num)

            if value == 'sin':
                result = str(math.sin(radians))
            elif value == 'cos':
                result = str(math.cos(radians))
            elif value == 'tan':
                result = str(math.tan(radians))
            elif value == 'cosec':
                result = str(1 / math.sin(radians))
            elif value == 'sec':
                result = str(1 / math.cos(radians))
            elif value == 'cot':
                result = str(1 / math.tan(radians))

            e1.delete(0, END)
            e1.insert(0, result)
        except:
            e1.delete(0, END)
            e1.insert(0, "Error")

    else:
        e1.insert(END, value)

t = Tk()
t.geometry("400x372")
t.resizable(False, False)
t.title("Scientific Calculator")

e1 = Entry(t, font=('Georgia', '20', 'bold'), justify=RIGHT)
e1.grid(row=0, column=0, columnspan=5, sticky=W+E)

buttons = [
    'C', 'CE', 'π', 'n!', '/',
    '7', '8', '9', '\u00D7', '-',
    '4', '5', '6', '+', 'sin',
    '1', '2', '3', '.', 'cos',
    '0', '(', ')', '=', 'tan',
    'cosec', 'sec', 'cot', '^', '√'
]

row1 = 1
col1 = 0

for button in buttons:
    b = Button(t, text=button, width=10, height=3, command=lambda b=button: click(b))
    b.grid(row=row1, column=col1)
    col1 += 1
    if col1 > 4:
        col1 = 0
        row1 += 1

t.mainloop()
