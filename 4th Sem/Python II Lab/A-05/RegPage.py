from tkinter import *
import csv
import os

# Creating CSV file and adding columns Name, Age, Gender, Favorite Food
if not os.path.isfile("student_db.csv"):
    f1 = open("student_db.csv", "w", newline="")
    writer = csv.writer(f1)
    writer.writerow(["Name", "Age", "Gender", "Favorite Food"])
    f1.close()

def check():
    global FF
    x = FF1.get()
    y = FF2.get()
    z = FF3.get()
    
    if x == 1:
        FF = "Chicken Biryani"
    elif y == 1:
        FF = "Mutton Biryani"
    elif z == 1:
        FF = "Fried Rice"
    else:
        FF = ""
        
    l5.config(text="Selected Food: " + FF)

def click():
    g = gen.get()

def submit():
    student = []
    
    name = name_var.get()
    student.append(name)
    
    # Validate name and age fields
    if not name:
        l5.config(text="Please enter your name.")
        return
    
    try:
        age = age_var.get()
        if age <= 0:
            l5.config(text="Please enter a valid age.")
            return
    except ValueError:
        l5.config(text="Please enter a valid age.")
        return
    student.append(age)
    
    gender = gen.get()
    student.append(gender)
    
    try:
        student.append(FF)
    except:
        student.append("No Food Choice")

    f1 = open("student_db.csv", "a", newline="")
    w = csv.writer(f1)
    w.writerow(student)
    f1.close()
    print("Appended this data:", student)

t = Tk()
t.title("SKF Fest")
t.geometry("330x300")
t.resizable(False, False)

Label(t, text="- Fest Registration -", bg="cyan").grid(row=1, column=0, columnspan=4, padx=110, pady=5, sticky=W)

# Name
name_var = StringVar()
l1 = Label(t, text="Enter your name:", bg="blue")
l1.grid(row=2, column=0, padx=10, pady=5, sticky=W)
name_entry = Entry(t, textvariable=name_var)
name_entry.grid(row=2, column=1, columnspan=4)

# Age
age_var = IntVar()
l2 = Label(t, text="Enter your age:", bg="blue")
l2.grid(row=3, column=0, padx=10, pady=5, sticky=W)
age_entry = Entry(t, textvariable=age_var)
age_entry.grid(row=3, column=1, padx=40, columnspan=4, sticky=W)

# Gender
gen = StringVar()
l3 = Label(t, text="Gender:", bg="blue")
l3.grid(row=4, column=0, padx=10, pady=5, sticky=W)
M = Radiobutton(t, text="Male", variable=gen, value="M", command=click)
M.grid(row=4, column=1, sticky=W)
F = Radiobutton(t, text="Female", variable=gen, value="F", command=click)
F.grid(row=4, column=2, sticky=W)
O = Radiobutton(t, text="Other", variable=gen, value="O", command=click)
O.grid(row=4, column=3, sticky=W)

# Favorite Food
FF1 = IntVar()
FF2 = IntVar()
FF3 = IntVar()
l4 = Label(t, text="Favorite Food: ", bg="red")
l4.grid(row=5, column=0, padx=10, pady=5, sticky=W)
CB = Checkbutton(t, text="Chicken Biryani", variable=FF1, onvalue=1, offvalue=0, command=check)
CB.grid(row=6, column=0, sticky=W)
MB = Checkbutton(t, text="Mutton Biryani", variable=FF2, onvalue=1, offvalue=0, command=check)
MB.grid(row=7, column=0, sticky=W)
FR = Checkbutton(t, text="Fried Rice", variable=FF3, onvalue=1, offvalue=0, command=check)
FR.grid(row=8, column=0, sticky=W)

l5 = Label(t, text="Selected Food: ", bg="yellow")
l5.grid(row=9, column=0, columnspan=4, padx=10, pady=5, sticky=W)

# Submit Button
submit_btn = Button(t, text="Submit", bg="green", fg="white", command=submit)
submit_btn.grid(row=10, column=0, columnspan=4, pady=10)

t.mainloop()
