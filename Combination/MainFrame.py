import tkinter
from TODO.TodoItemList import TodoItemList
from Calendar.CalendarFrame import CalendarFrame
from TODO.EventFileStream import EventFileStream


class CRA(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.files = EventFileStream().get_instance().read_all_file()
        self.todoList = TodoItemList(self.files, self.update_calendar, master=self)
        self.calendar = CalendarFrame(show_certain_date_callback=self.todoList.display_date,
                                      check_event_callback=self.todoList.has_event,
                                      master=self)
        self.place_content()
        self.mainloop()

    def place_content(self):
        self.calendar.grid(row=0, column=0)
        self.todoList.grid(row=0, column=1)
        self.config(bg="white")

    def update_calendar(self):
        self.calendar.event_update_call()


# TEST_USE
if __name__ == "__main__":
    CRA()
