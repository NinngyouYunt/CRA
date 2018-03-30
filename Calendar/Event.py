
class Event:

    contentTuple = ("is_done", "over_due", "due_date", "input_date", "priority", "title", "content")

    def __init__(self, is_done, over_due, due_date, input_date, priority, title, content):
        self.isDone = is_done
        self.overDue = over_due
        self.dueDate = due_date
        self.inputDate = input_date
        self.priority = priority
        self.title = title
        self.content = content

    def change_done_status(self):
        self.isDone = not self.isDone

    def overdue(self):
        self.overDue = True

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in Event.contentTuple:
                setattr(self, key, value)

    def check_title(self):
        print(getattr(self, "title"))
