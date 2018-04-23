import TODO.TodoItem as TodoItem
import tkinter
from tkinter.font import Font
from TODO.EventFileStream import EventFileStream


class TodoItemList(tkinter.Frame):

    def __init__(self, event_list, update_calendar_callback, master=None):
        super().__init__(master)
        self.itemListFrame = tkinter.Frame(master=self)
        self.itemList = []
        for event in event_list:
            self.itemList.append(TodoItem.TodoItem(event, master=self.itemListFrame,
                                                   delete_action=self.delete_item, edit_action=self.edit_item))
        self.addEventButton = tkinter.Button(self, text="+", command=self.add_event_button_action)
        self.showAllButton = tkinter.Button(self, text="Show All", command=self.show_all_events)
        self.showDateLabel = tkinter.Label(self, text="All")
        self.update_calendar = update_calendar_callback
        self.place_content()

    def update_content(self):
        self.update()

    def place_content(self):
        self.showDateLabel.config(font=Font(size=15), bg="white")
        self.addEventButton.config(width=10, height=1, bg="white")
        self.addEventButton.config(font=Font(size=15), bg="white")
        self.showAllButton.config(bg="white")

        self.showDateLabel.grid(row=0, column=0)
        for index in range(len(self.itemList)):
            self.itemList[index].grid(row=index, column=0)
        self.itemListFrame.grid(row=1, column=0)
        self.addEventButton.grid(row=2, column=0)
        self.showAllButton.grid(row=3, column=0)
        self.config(bg="white")
        self.update_content()

    def delete_item(self, obj):
        obj.grid_forget()
        self.itemList.remove(obj)
        self.update_content()
        self.update_file(obj.event.get_due_date())
        self.update_calendar()

    def add_new_event(self, new_event):
        if new_event is not None:
            self.itemList.append(TodoItem.TodoItem(new_event, master=self.itemListFrame,
                                                   delete_action=self.delete_item, edit_action=self.edit_item))
            self.itemList[len(self.itemList)-1].grid(column=0)
            self.update_content()
            self.update_file(new_event.get_due_date())
            self.update_calendar()

    def edit_item(self, edited_event):
        self.update_file(edited_event.get_due_date())
        self.update_calendar()

    def update_file(self, due_date):
        events = []
        for item in self.itemList:
            if item.event.compare_month(due_date):
                events.append(item.event)
        EventFileStream.get_instance().save_file("data", events)

    def add_event_button_action(self):
        adding = TodoItem.EventInputWindow(self, self.add_new_event, True)
        adding.focus_force()

    def process_date(self, year, month, day):
        res = str(year)
        if month < 10:
            res += "/0" + str(month)
        else:
            res += "/" + str(month)
        if day < 10:
            res += "/0" + str(day)
        else:
            res += "/" + str(day)
        return res

    def show_all_events(self):
        for widget in self.itemListFrame.winfo_children():
            widget.grid_forget()
        for event in self.itemList:
            event.grid(column=0)
        self.showDateLabel.config(text="All")
        self.update()

    def find_events(self, year, month, day):
        items = []
        for item in self.itemList:
            if item.event.get_due_date() == self.process_date(year, month, day):
                items.append(item)
        return items

    def display_date(self, year, month, day):
        for widget in self.itemListFrame.winfo_children():
            widget.grid_forget()
        for event in self.find_events(year, month, day):
            event.grid(column=0)
        self.showDateLabel.config(text=self.process_date(year, month, day))
        self.update()

    def has_event(self, year, month, day):
        for item in self.itemList:
            if item.event.get_due_date() == self.process_date(year, month, day):
                return True
        return False
