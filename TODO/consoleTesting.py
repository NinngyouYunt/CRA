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

import datetime, time

dueDate = "2018-3-14".split("-")
try:
    print(dueDate)
    datetime.datetime(year=int(dueDate[0]), month=int(dueDate[1]), day=int(dueDate[2]))
except (ValueError, IndexError) as error:
    print("Please input a proper date \nFormat:yyyy-mm-dd")

now = datetime.datetime.now()
if len(str(now.month)) < 2:
    str = "0" + str(now.month)
    print(str)
else:
    print(now.month)
input="11:11:11"
"".isdigit()
print(time.strptime(input, '%H:%M'))
