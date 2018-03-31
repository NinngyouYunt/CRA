import tkinter
from tkinter.font import Font
import os


class TodoItem(tkinter.Frame):

    labelWidth = 20

    def __init__(self, event, master=None):
        super().__init__(master, bd=1, relief="ridge")

        self.event = event

        # https://www.flaticon.com/free-icon/pencil-edit-button_61456
        pictureRoot = os.path.dirname(__file__) + "/assets"
        self.editButtonIcon = tkinter.PhotoImage(file=os.path.join(pictureRoot, "edit-button-icon.png"))
        # https://www.flaticon.com/free-icon/rubbish-bin_63260#term=delete&page=1&position=5
        self.deleteButtonIcon = tkinter.PhotoImage(file=os.path.join(pictureRoot, "delete-button-icon.png"))

        self.titleLabel = tkinter.Label(master=self)
        self.dueDateLabel = tkinter.Label(master=self)
        self.priorityLabel = tkinter.Label(master=self)
        self.deleteButton = tkinter.Button(master=self, image=self.deleteButtonIcon)
        self.editButton = tkinter.Button(master=self, image=self.editButtonIcon)
        self.checkButtonStatus = tkinter.IntVar()
        self.checkButton = tkinter.Checkbutton(master=self, variable=self.checkButtonStatus)

        self.place_content()

    def update_content(self):
        self.check_item()
        self.titleLabel.config(text=self.event.title)
        self.dueDateLabel.config(text=self.event.dueDate)
        self.priorityLabel.config(text=self.event.priority)
        self.update()

    def place_content(self):

        self.titleLabel.config(width=self.labelWidth, anchor="w",
                               justify=tkinter.LEFT, wraplength=self.labelWidth*8)
        self.dueDateLabel.config(anchor="e", width=int(self.labelWidth*0.9))
        self.priorityLabel.config(anchor="w", width=int(self.labelWidth*0.1))
        self.checkButton.config(command=self.check_button_action, anchor="c")
        self.deleteButton.config(command=self.delete_button_action, anchor="c", bd=2, relief="ridge")
        self.editButton.config(command=self.edit_button_action, anchor="c", bd=2, relief="ridge")

        self.titleLabel.grid(row=0, column=1, columnspan=2, padx=3, pady=0)
        self.priorityLabel.grid(row=1, column=1)
        self.dueDateLabel.grid(row=1, column=2)
        self.checkButton.grid(row=0, column=0, rowspan=2, padx=2)
        self.deleteButton.grid(row=1, column=3, padx=7)
        self.editButton.grid(row=0, column=3, padx=7)
        self.update_content()

    def check_item(self):
        # Is done, crossing it out
        if self.event.isDone is True:
            self.titleLabel.config(font=Font(overstrike=1))
            self.dueDateLabel.config(font=Font(overstrike=1))
            self.priorityLabel.config(font=Font(overstrike=1))
            self.checkButtonStatus.set(1)
        # Not done, keeping things
        else:
            self.titleLabel.config(font=Font(overstrike=0))
            self.dueDateLabel.config(font=Font(overstrike=0))
            self.priorityLabel.config(font=Font(overstrike=0))
            self.checkButtonStatus.set(0)
        self.update()

    def check_button_action(self):
        self.event.change_done_status()
        self.check_item()

    def grid(self,**kwargs):
        super().grid(ipady=3, ipadx=0, **kwargs)

    def delete_button_action(self):
        pass

    def edit_button_action(self):
        pass
