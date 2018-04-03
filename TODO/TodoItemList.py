import TODO.TodoItem as TodoItem
import tkinter


class TodoItemList(tkinter.Frame):

    def __init__(self, event_list, master=None):
        super().__init__(master)
        self.itemListFrame = tkinter.Frame(master=self)
        self.itemList = []
        for event in event_list:
            self.itemList.append(TodoItem.TodoItem(event, master=self.itemListFrame, delete_action=self.delete_item))
        self.place_content()

    def update_content(self):
        self.update()

    def place_content(self):
        for index in range(len(self.itemList)):
            self.itemList[index].grid(row=index, column=0)
        self.itemListFrame.grid()
        self.update_content()

    def delete_item(self, obj):
        obj.grid_forget()
        self.itemList.remove(obj)
        self.update_content()
