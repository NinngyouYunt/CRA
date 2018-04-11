import TODO.TodoItem as TodoItem
import tkinter
from tkinter.font import Font
from TODO.EventFileStream import EventFileStream


class TodoItemList(tkinter.Frame):

    def __init__(self, event_list, master=None):
        super().__init__(master)
        self.itemListFrame = tkinter.Frame(master=self)
        self.itemList = []
        for event in event_list:
            self.itemList.append(TodoItem.TodoItem(event, master=self.itemListFrame, delete_action=self.delete_item))
        self.addEventButton = tkinter.Button(self, text="+", command=self.add_event_button_action)
        self.place_content()

    def update_content(self):
        self.update()

    def place_content(self):
        self.addEventButton.config(width=10, height=1)
        self.addEventButton.config(font=Font(size=15))

        for index in range(len(self.itemList)):
            self.itemList[index].grid(row=index, column=0)
        self.itemListFrame.grid(row=0, column=0)
        self.addEventButton.grid(row=2, column=0)
        self.update_content()

    def delete_item(self, obj):
        obj.grid_forget()
        self.itemList.remove(obj)
        self.update_content()

    def get_events(self):
        events = []
        for item in self.itemList:
            events.append(item.event)
        return events

    def add_new_event(self, new_event):
        if new_event is not None:
            self.itemList.append(TodoItem.TodoItem(new_event, master=self.itemListFrame, delete_action=self.delete_item))
            self.itemList[len(self.itemList)-1].grid(column=0)
            self.update_content()
            # TEST ONLY
            EventFileStream.get_instance().save_file("testFile", self.get_events())



    def add_event_button_action(self):
        adding = TodoItem.EventInputWindow(self, self.add_new_event, True)
        adding.focus_force()
