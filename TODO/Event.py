
class Event:

    contentTuple = ("is_done", "over_due",
                    "due_date", "input_date", "due_time"
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

    def overdue(self):
        self.overDue = True

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in Event.contentTuple and key != "input_date":
                setattr(self, key, value)
        # Set input-date to current date

    def check_title(self):
        print(getattr(self, "title"))

    # Test USE only
    def __str__(self):
        return self.title + ", " + self.content + ", " + self.priority + ", " + self.dueDate + \
               ", " + self.dueTime + ", " + self.isDone + ", " + self.overDue + ", " + self.inputDate

    def __eq__(self, other):
        return self.title == other.title