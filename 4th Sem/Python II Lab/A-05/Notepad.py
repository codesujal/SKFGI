'''
Sir I have implemented these notepad operations:
1. New File
2. Open File
3. Save File
4. Save As
5. Undo
6. Cut
7. Copy
8. Paste
9. Delete
10. Select All
Also used t.bind() function to implement shortcut keys.
'''

from tkinter import *
from tkinter import filedialog

t = Tk()
t.title("Notepad")
t.geometry("500x500")

sb1 = IntVar()
current_file = None

zoom_level = 1.0

def zoom_in():
    global zoom_level
    zoom_level += 0.1
    text.config(font=("Arial", int(12 * zoom_level)))

def zoom_out():
    global zoom_level
    zoom_level -= 0.1
    text.config(font=("Arial", int(12 * zoom_level)))

def restore_default_zoom():
    global zoom_level
    zoom_level = 1.0
    text.config(font=("Arial", 12))

def save_file():
    global current_file
    if current_file:
        with open(current_file, 'w') as file: file.write(text.get("1.0", "end"))
    else: save_file_as()

def save_file_as():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        current_file = file_path
        with open(file_path, 'w') as file: file.write(text.get("1.0", "end"))

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        current_file = file_path
        with open(file_path, 'r') as file: text.delete(1.0, "end"); text.insert("1.0", file.read())

def new_file():
    global current_file
    current_file = None
    text.delete(1.0, "end")

def undo():
    text.edit_undo()

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def delete():
    text.delete(SEL_FIRST, SEL_LAST)

def select_all():
    text.tag_add(SEL, "1.0", "end")
    text.mark_set(INSERT, "1.0")
    text.see(INSERT)

mb = Menu(t)

f = Menu(mb, tearoff=0)
mb.add_cascade(label="File", menu=f)
f.add_command(label="New        Ctrl+N", command=new_file)
f.add_command(label="Open...    Ctrl+O", command=open_file)
f.add_command(label="Save        Ctrl+S", command=save_file)
f.add_command(label="Save as...  Ctrl+Shift+S", command=save_file_as)
f.add_separator()
f.add_command(label="Exit        Ctrl+Q", command=t.quit)

ed = Menu(mb, tearoff=0)
mb.add_cascade(label="Edit", menu=ed)
ed.add_command(label="Undo        Ctrl+Z", command=undo)
ed.add_separator()
ed.add_command(label="Cut         Ctrl+X", command=cut)
ed.add_command(label="Copy        Ctrl+C", command=copy)
ed.add_command(label="Paste       Ctrl+V", command=paste)
ed.add_command(label="Delete      Del", command=delete)
ed.add_separator()
ed.add_command(label="Select All  Ctrl+A", command=select_all)

view = Menu(mb, tearoff=0)
z = Menu(mb, tearoff=0)
z.add_command(label="Zoom in        Ctrl+Plus", command=zoom_in)
z.add_command(label="Zoom out       Ctrl+Minus", command=zoom_out)
z.add_command(label="Restore Default Zoom    Ctrl+0", command=restore_default_zoom)
view.add_cascade(label="Zoom", menu=z)
view.add_checkbutton(label="Status Bar", onvalue=1, offvalue=0, variable=sb1)
mb.add_cascade(label="View", menu=view)

text = Text(t, undo=True, font=("Arial", 12))
text.pack(expand=True, fill=BOTH)


t.bind('<Control-n>', lambda event: new_file())
t.bind('<Control-o>', lambda event: open_file())
t.bind('<Control-s>', lambda event: save_file())
t.bind('<Control-z>', lambda event: undo())
t.bind('<Control-x>', lambda event: cut())
t.bind('<Control-c>', lambda event: copy())
t.bind('<Control-v>', lambda event: paste())
t.bind('<Control-a>', lambda event: select_all())

t.config(menu=mb)
t.mainloop()

