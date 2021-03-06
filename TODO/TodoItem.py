import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
from TODO import Event
import os, datetime, time


class TodoItem(tk.Frame):

    labelWidth = 20

    def __init__(self, event, master=None, delete_action=None, edit_action=None):
        super().__init__(master, bd=1, relief="ridge")

        self.event = event
        self.editingWindow = None

        # https://www.flaticon.com/free-icon/pencil-edit-button_61456
        picture_root = os.path.dirname(__file__) + "/assets"
        self.editButtonIcon = tk.PhotoImage(file=os.path.join(picture_root, "edit-button-icon.png"))
        # https://www.flaticon.com/free-icon/rubbish-bin_63260#term=delete&page=1&position=5
        self.deleteButtonIcon = tk.PhotoImage(file=os.path.join(picture_root, "delete-button-icon.png"))

        self.titleLabel = tk.Label(master=self, bg="white")
        self.dueDateLabel = tk.Label(master=self, bg="white")
        self.priorityLabel = tk.Label(master=self, bg="white")
        self.deleteButton = tk.Button(master=self, image=self.deleteButtonIcon, bg="white")
        self.editButton = tk.Button(master=self, image=self.editButtonIcon, bg="white")
        self.checkButtonStatus = tk.IntVar()
        self.checkButton = tk.Checkbutton(master=self, variable=self.checkButtonStatus, bg="white")
        self.bind_delete_action(delete_action)
        self.parentEditCallback = edit_action
        self.config(bg="white")
        self.place_content()

    def update_content(self):
        self.titleLabel.config(text=self.event.title)
        self.dueDateLabel.config(text=self.event.get_due_date())
        self.priorityLabel.config(text=self.event.priority)
        self.check_item()
        self.update()

    def place_content(self):
        self.titleLabel.config(width=self.labelWidth, anchor="w",
                               justify=tk.LEFT, wraplength=self.labelWidth*8)
        self.dueDateLabel.config(anchor="e", width=int(self.labelWidth*0.9))
        self.priorityLabel.config(anchor="e", width=int(self.labelWidth*0.1))
        self.checkButton.config(command=self.check_button_action, anchor="c")
        self.deleteButton.config(anchor="c", bd=2, relief="ridge")
        self.editButton.config(command=self.edit_button_action, anchor="c", bd=2, relief="ridge")

        self.titleLabel.grid(row=0, column=1, columnspan=2, padx=3, pady=0)
        self.priorityLabel.grid(row=1, column=1)
        self.dueDateLabel.grid(row=1, column=2)
        self.checkButton.grid(row=0, column=0, rowspan=2)
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
        self.parentEditCallback(self.event)

    def grid(self,**kwargs):
        super().grid(ipady=3, ipadx=0, **kwargs)

    def bind_delete_action(self, parent_callback):
        self.deleteButton.config(command=lambda: parent_callback(self))

    def edit_button_action(self):
        if self.editingWindow is None:
            self.editingWindow = EventInputWindow(self, self.edit_callback, False)
            self.editingWindow.focus_force()
            print("Open Edit Window")
        else:
            self.editingWindow.focus_force()
            print("Editing Window Opened")

    def edit_callback(self, event):
        self.editingWindow = None
        if event is None:
            print("Cancel")
        else:
            self.event.update(event)
            print("Editing Event")
            self.update_content()
            self.parentEditCallback(self.event)

    def __eq__(self, other):
        return self.event == other.event


class EventInputWindow(tk.Toplevel):

    def __init__(self, parent, callback, add_new=True):
        super().__init__(parent)
        self.mode = add_new # True - adding new event, False - editing event
        if self.mode:
            self.title("Add Event")
        else:
            self.title("Edit Event")
        self.resizable(False, False)
        self.callback = callback
        self.titleInput = tk.Entry(self)
        self.contentInput = tk.Entry(self)
        self.priorityInput = tk.Entry(self)
        self.dueDateInput = tk.Entry(self)
        self.dueTimeInput = tk.Entry(self)
        if self.mode:
            self.saveButton = tk.Button(self, text="Add", command=self.save, bg="white")
        else:
            self.saveButton = tk.Button(self, text="Save", command=self.save, bg="white")
        self.cancelButton = tk.Button(self, text="Cancel", command=self.cancel, bg="white")

        if self.mode:
            self.titleLabel = tk.Label(self, text="Title(*):", bg="white")
        else:
            self.titleLabel = tk.Label(self, text="Title:", bg="white")
        self.contentLabel = tk.Label(self, text="Content:", bg="white")
        self.priorityLabel = tk.Label(self, text="Priority:", bg="white")
        self.dueDateLabel = tk.Label(self, text="Date(yyyy-mm-dd):", bg="white")
        self.dueTimeLabel = tk.Label(self, text="Time(hh:mm):", bg="white")

        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.place_content()

        self.titleInput.focus_force()

    def place_content(self):
        self.titleLabel.grid(row=0, column=0)
        self.contentLabel.grid(row=1, column=0)
        self.priorityLabel.grid(row=2, column=0)
        self.dueDateLabel.grid(row=3, column=0)
        self.dueTimeLabel.grid(row=4, column=0)

        self.titleInput.grid(row=0, column=1)
        self.contentInput.grid(row=1, column=1)
        self.priorityInput.grid(row=2, column=1)
        self.dueDateInput.grid(row=3, column=1)
        self.dueTimeInput.grid(row=4, column=1)

        self.saveButton.grid(row=5, columnspan=2)
        self.cancelButton.grid(row=6, columnspan=2)
        self.config(bg="white")

    def process_input(self):
        params = []
        # Check if title is empty
        if self.titleInput.get() == "":
            # Title is mandatory for new event
            if self.mode:
                return "Title is a mandatory field for creating new event!"
            else:
                params.append(None)
        else:
            params.append(self.titleInput.get())
        # Check if content is empty
        if self.contentInput.get() == "":
            params.append(None)
        else:
            params.append(self.contentInput.get())
        # Check if priority is empty
        if self.priorityInput.get() == "":
            params.append(None)
        else:
            # Check if priority is an integer
            if self.priorityInput.get().isdigit() is False:
                return "Please input a non-negative integer for priority!"
            else:
                if 0 <= int(self.priorityInput.get()) < 10:
                    params.append(int(self.priorityInput.get()))
                else:
                    return "Priority is an integer between 0 and 9"
        # Check if dueDate is empty
        if self.dueDateInput.get() == "":
            params.append(None)
        else:
            # Check if dueDate is valid
            due_date = self.dueDateInput.get().split("-")
            try:
                datetime.datetime(year=int(due_date[0]), month=int(due_date[1]), day=int(due_date[2]))
                params.append(list(map(lambda x: int(x), due_date)))
            except (ValueError, IndexError) as error:
                return "Please input a proper date \nFormat: yyyy-mm-dd"
        # Check if dueTime is empty
        if self.dueTimeInput.get() == "":
            params.append(None)
        else:
            # Check if dueTime is valid
            try:
                time.strptime(self.dueTimeInput.get(), '%H:%M')
                due_time = self.dueTimeInput.get().split(":")
                params.append(list(map(lambda x: int(x), due_time)))
            except (IndexError, ValueError) as error:
                return "Please input a proper time using 24-hour\nFormat: hh-mm"
        # Append is_done = no change, is_late = no change
        params.append(None)
        params.append(None)
        return params

    def save(self):
        params = self.process_input()
        print("Change", params)
        if type(params) is str:
            messagebox.showerror("Error", params, parent=self)
        else:
            event = Event.Event(*params)
            self.callback(event)
            self.destroy()

    def cancel(self):
        if self.priorityInput.get() == "" and self.titleInput.get() == "" \
                and self.contentInput.get() == "" and self.dueTimeInput.get() == "" \
                and self.dueDateInput.get() == "":
            self.callback(None)
            self.destroy()
        else:
            print(self.titleInput.get() == "")
            result = messagebox.askyesno("Cancel", "Do you want to abandon changes?", icon="warning", parent=self)
            if result:
                self.callback(None)
                self.destroy()
