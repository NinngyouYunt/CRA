
class Event:

    contentTuple = ("isDone", "isLate",
                    "dueDate", "dueTime",
                    "priority",
                    "title", "content")

    # title - string
    # content - string
    # priority - int
    # dueDate - list of int[yyyy, mm, dd]
    # dueTime - list of int [hh, mm]
    # isDone - boolean
    # isLate - boolean

    def __init__(self, title, content, priority, due_date, due_time, is_done, is_late):
        self.title = title
        self.content = content
        self.priority = priority
        self.dueDate = due_date
        self.dueTime = due_time
        self.isDone = is_done
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

    # Test USE only
    def __str__(self):
        return self.title + ", " + self.content + ", " + self.priority + ", " + self.dueDate + \
               ", " + self.dueTime + ", " + self.isDone + ", " + self.isLate

    def __eq__(self, other):
        return self.title == other.title
