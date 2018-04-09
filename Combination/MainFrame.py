import tkinter
from TODO.TodoItemList import TodoItemList
from Calendar.CalendarFrame import CalendarFrame
from TODO.Event import Event


class CRA(tkinter.Tk):
    def __init__(self, for_test):
        super().__init__()
        self.todoList = TodoItemList(for_test, master=self)
        self.calendar = CalendarFrame()
        self.place_content()
        self.mainloop()

    def place_content(self):
        self.calendar.grid(row=0, column=0)
        self.todoList.grid(row=0, column=1)


eventList = [
    Event("Event1"
          "12345678901234567890", "Content1", 1, "2018/03/10", "0510", True, True, "2018/3/1"),
    Event("Event2", "Content2", 2, "2018/12/11", "1320", False, True, "2018/3/1"),
]
CRA(eventList)
