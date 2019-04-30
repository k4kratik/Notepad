from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import webbrowser

# -------------------- FUNCTIONS DEFINATIONS START -------------------------------


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text documents", '*.txt')])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text documents", '*.txt')])

        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print('FILE SAVED SUCCESSFULLY')

    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def newFile2(event):
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile2(event):
    global file
    file = askopenfilename(defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text documents", '*.txt')])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile2(event):
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text documents", '*.txt')])

        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print('FILE SAVED SUCCESSFULLY')

    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()


def cut():
    TextArea.event_generate("<<Cut>>")


def copy():
    TextArea.event_generate("<<Copy>>")


def paste():
    TextArea.event_generate("<<Paste>>")


def about():
    showinfo("Notepad", "Notepad by KRATIK JAIN @k4kratik")


def selectall(event):
    TextArea.tag_add(SEL, "1.0", END)
    TextArea.mark_set(INSERT, "1.0")
    TextArea.see(INSERT)
    return 'break'


def aboutus():
    # basic settings
    newWindow = Toplevel(root)
    newWindow.geometry("400x500")
    fb = PhotoImage(file='facebook.png')
    qra = PhotoImage(file='quora.png')
    insta = PhotoImage(file='instagram.png')
    b1 = Button(newWindow)
    b1.config(image=fb,command=callback2)
    b1.pack()
    b2 = Button(newWindow,command=callback3)
    b2.config(image=qra)
    b2.pack()
    b3 = Button(newWindow,command=callback4)
    b3.config(image=insta)
    b3.pack()

    photo = PhotoImage(file='image.png')
    display = Label(newWindow, image=photo, cursor="hand2", anchor=W)
    display.bind("<Button-1>", callback)
    display.pack()
    newWindow.transient(root)
    newWindow.grab_set()
    root.wait_window(newWindow)


    mainloop()


def callback(event):
    webbrowser.open_new(r"http://www.facebook.com/k4kratik")


def callback2():
    webbrowser.open_new(r"http://www.facebook.com/k4kratik")


def callback3():
    webbrowser.open_new(r"https://www.quora.com/profile/Kratik-Jain-1")


def callback4():
    webbrowser.open_new(r"http://www.instagram.com/k4kratik")    

# --------------------FUNCTIONS DEFINATIONS END-------------------------------

# basic Tkinter Setup
root = Tk()
root.geometry("644x788")

# --------------------KEY BINDINGS -------------------------------------------

root.bind('<Control-a>', selectall)
root.bind('<Control-A>', selectall)
root.bind('<Control-o>', openFile2)
root.bind('<Control-s>', saveFile2)
root.bind('<Control-n>', newFile2)
root.bind('<Control-O>', openFile2)
root.bind('<Control-S>', saveFile2)
root.bind('<Control-N>', newFile2)
root.title('Untitled - Notepad')


try:
    root.iconbitmap('1.ico')
except TclError:
    print("No Icon file is defined")


root.geometry("644x788")


# Add Text Area
TextArea = Text(root, font="luciada 20")
file = None
TextArea.pack(fill=BOTH, expand=True)

# MenuBar
MenuBar = Menu(root)
# MenuBar - File Menu
FileMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label='New', command=newFile)
FileMenu.add_command(label='Open', command=openFile)
FileMenu.add_command(label='Save', command=saveFile)
FileMenu.add_separator()
FileMenu.add_command(label='Exit    Alt+F4', command=quitApp)
MenuBar.add_cascade(label='File', menu=FileMenu)

# MenuBar - Edit Menu
EditMenu = Menu(MenuBar, tearoff=0)
EditMenu.add_command(label='Cut', command=cut)
EditMenu.add_command(label='Copy', command=copy)
EditMenu.add_command(label='Paste', command=paste)
MenuBar.add_cascade(label="Edit", menu=EditMenu)

# MenuBar - Edit Menu
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label='About Notepad', command=about)
HelpMenu.add_command(label='About Us', command=aboutus)
MenuBar.add_cascade(label='Help', menu=HelpMenu)

root.config(menu=MenuBar)

# Scrollbar
Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)


TextArea.focus()
root.mainloop()

