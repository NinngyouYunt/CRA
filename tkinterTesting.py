from tkinter import *


def do_this(widget, number):
    print(widget)
    print(number)

def do_that(event):
    print(event)

tk = Tk()

button1 = Button(tk, text="Click")
button1.configure(command=lambda btn=button1: do_this(btn, 1))
button1.pack()

label1 = Label(tk, text="Hello")
label1.bind("<Button-3>", do_that)
label1.bind("<Button-1>", lambda z: do_this("The WORLD!", 2))
label1.pack()

tk.mainloop()
