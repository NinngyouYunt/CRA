import tkinter
import Event


class TodoItem(tkinter.Frame):

    def __init__(self, event, master=None):
        super().__init__(master)
        self.event = event
        self.titleLabel = tkinter.Label(master=self)
        self.dueDateLabel = tkinter.Label(master=self)
        self.priorityLabel = tkinter.Label(master=self)
        self.checkButton = tkinter.Button(master=self)

        self.place_content()

    def update_content(self):
        self.titleLabel.config(text=self.event.title)
        self.dueDateLabel.config(text=self.event.dueDate)
        self.priorityLabel.config(text=self.event.priority)
        self.update()

    def place_content(self):
        self.checkButton.config(text="Done")
        self.titleLabel.grid(row=0, column=1, rowspan=3)
        self.dueDateLabel.grid(row=1, column=2, rowspan=2)
        self.priorityLabel.grid(row=0, column=4, columnspan=2)
        self.checkButton.grid(row=0, column=0, columnspan=2)
        self.update_content()


tk = tkinter.Tk()
todoitem = TodoItem(Event.E)

tk.mainloop()