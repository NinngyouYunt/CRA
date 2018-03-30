from TODO.Event import *
from tkinter import *


root = Tk()

# icon from https://www.flaticon.com/free-icon/pencil-edit-button_61456
photo = PhotoImage(file="pencil-edit-button.png")
Button(text="hello", image=photo, master=root).grid()

root.mainloop()
