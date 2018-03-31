from TODO.Event import *
# from tkinter import *
#
#
# root = Tk()
#
#
# # icon from https://www.flaticon.com/free-icon/pencil-edit-button_61456
# def doThis():
#     print(cb1Var.get())
#
#
# cb1Var = IntVar()
# cb1 = Checkbutton(text="hello", master=root, command=doThis, variable=cb1Var).grid()
# Checkbutton(text="hello2", master=root).grid()
#
#
# def changeCheck():
#     cb1Var.set(not cb1Var.get())
#
#
# Button(text="Click", command=changeCheck, master=root).grid()
#
# root.mainloop()

def removeLineBreak(item):
    return item[0:len(item)-1]
# r - read only, w - overwrite/create, a - append
file = open("testFile", "r")

fileContent = file.readlines() # array with each line (line break is escape code)
print(fileContent)
fileContent = list(map(removeLineBreak, fileContent))
print(fileContent)

itemNumber = int(len(fileContent)/9)
for i in range(itemNumber):
    print(fileContent[i*9:i*9+9])
