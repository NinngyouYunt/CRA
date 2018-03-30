import tkinter
from tkinter.font import Font


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

        self.checkButton.bind("<Button-1>", self.check_button_action)

        self.titleLabel.grid(row=0, column=1, columnspan=3)
        self.dueDateLabel.grid(row=1, column=2, columnspan=2)
        self.priorityLabel.grid(row=0, column=4, rowspan=2)
        self.checkButton.grid(row=0, column=0, rowspan=2)
        self.update_content()

    def check_button_action(self, event):
        # Uncheck
        if self.event.isDone:
            self.checkButton.config(bg="white")
            self.titleLabel.config(font=Font(overstrike=0))
            self.dueDateLabel.config(font=Font(overstrike=0))
            self.priorityLabel.config(font=Font(overstrike=0))
        # Check
        else:
            self.checkButton.config(bg="red")
            self.titleLabel.config(font=Font(overstrike=1))
            self.dueDateLabel.config(font=Font(overstrike=1))
            self.priorityLabel.config(font=Font(overstrike=1))
        self.event.isDone = not self.event.isDone
        self.update()
