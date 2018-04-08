
class Event:

    contentTuple = ("isDone", "overDue",
                    "dueDate", "inputDate", "dueTime",
                    "priority",
                    "title", "content")

    def __init__(self, title, content, priority, due_date, due_time, is_done, over_due, input_date):
        self.title = title
        self.content = content
        self.priority = priority
        self.dueDate = due_date
        self.dueTime = due_time
        self.isDone = is_done
        self.overDue = over_due
        self.inputDate = input_date

    def change_done_status(self):
        self.isDone = not self.isDone

    def check_title(self):
        print(getattr(self, "title"))

    def get_list(self):
        return [self.title, self.content, self.priority, self.dueDate, self.dueTime,
                self.isDone, self.overDue, self.inputDate]

    def update(self, event):
        for field in Event.contentTuple:
            new_field = getattr(event, field)
            if new_field is not None:
                setattr(self, field, new_field)

    # Test USE only
    def __str__(self):
        return self.title + ", " + self.content + ", " + self.priority + ", " + self.dueDate + \
               ", " + self.dueTime + ", " + self.isDone + ", " + self.overDue + ", " + self.inputDate

    def __eq__(self, other):
        return self.title == other.title