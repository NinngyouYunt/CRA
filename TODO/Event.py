
class Event:

    contentTuple = ("isDone", "isLate",
                    "dueDate", "dueTime",
                    "priority",
                    "title", "content")

    # title - string - mandatory
    # content - string - optional
    # priority - int - optional
    # dueDate - list of int[yyyy, mm, dd] - optional
    # dueTime - list of int [hh, mm] - optional
    # isDone - boolean - mandatory
    # isLate - boolean - auto set

    def __init__(self, title, content, priority, due_date, due_time, is_done, is_late):
        self.title = title
        if content is None:
            self.content = ""
        else:
            self.content = content
        if priority is None:
            self.priority = 0
        else:
            self.priority = priority
        self.dueDate = due_date
        self.dueTime = due_time
        if is_done is None:
            self.isDone = False
        else:
            self.isDone = is_done
        if is_late is None:
            self.isLate = False
        else:
            self.isLate = is_late

    def change_done_status(self):
        self.isDone = not self.isDone

    def check_title(self):
        print(getattr(self, "title"))

    def get_list(self):
        return [self.title, self.content, self.priority, self.dueDate, self.dueTime,
                self.isDone, self.isLate]

    def update(self, event):
        for field in Event.contentTuple:
            new_field = getattr(event, field)
            if new_field is not None:
                setattr(self, field, new_field)

    def get_due_date(self):
        date_str = ""
        if self.dueDate != "" and self.dueDate is not None:
            date_str = str(self.dueDate[0])
            if self.dueDate[1] < 10:
                date_str = date_str + "/0" + str(self.dueDate[1])
            else:
                date_str = date_str + "/" + str(self.dueDate[1])
            if self.dueDate[2] < 10:
                date_str = date_str + "/0" + str(self.dueDate[2])
            else:
                date_str = date_str + "/" + str(self.dueDate[2])
        return date_str

    def get_due_time(self):
        time_str = ""
        if self.dueTime != "" and self.dueTime is not None:
            if self.dueTime[0] < 10:
                time_str = time_str + "0" + str(self.dueTime[0])
            else:
                time_str = time_str + str(self.dueTime[0])
            if self.dueTime[1] < 10:
                time_str = time_str + ":0" + str(self.dueTime[1])
            else:
                time_str = time_str + ":" + str(self.dueTime[1])
        return time_str

    def get_saving_string(self):
        string = self.title + "\n" + self.content + "\n" + str(self.priority) + "\n" + \
                 self.get_due_date() + "\n" + self.get_due_time() + "\n" + \
                 str(self.isDone) + "\n" + str(self.isLate)
        return string

    def __eq__(self, other):
        return self.title == other.title

    # Test USE only
    def __str__(self):
        return self.title + "\n " + self.content + "\n" + self.priority + "\n" + \
               self.get_due_date() + "\n" + self.get_due_time() + "\n" + \
               str(self.isDone) + "\n" + str(self.isLate)
