import tkinter
from TODO.TodoItemList import TodoItemList
from Calendar.CalendarFrame import CalendarFrame
from TODO.Event import Event
from TODO.EventFileStream import EventFileStream


class CRA(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.files = EventFileStream()
        self.todoList = TodoItemList(self.files.events, master=self)
        self.calendar = CalendarFrame()
        self.place_content()
        self.mainloop()

    def place_content(self):
        self.calendar.grid(row=0, column=0)
        self.todoList.grid(row=0, column=1)


# TEST_USE
if __name__ == "__main__":
    eventList = [
        Event("Event1"
              "12345678901234567890", "Content1", 1, [2018, 3, 14], [5,10], True, True),
        Event("Event2", "Content2", 2, [2018, 12, 11], [13,20], False, True),
    ]
    CRA()


