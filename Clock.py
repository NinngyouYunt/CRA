import datetime


class Clock:
    instanceCount = 0
    instance = None
    monthDict = ("January", "February", "March", "April",
                 "May", "June", "July", "August",
                 "September", "October", "November", "December")
    weekDict = ("Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday")

    def __init__(self):
        self.date = datetime.datetime.now()
        self.currentDay = self.date.day
        self.currentMonth = self.date.month
        self.currentYear = self.date.year

    def update(self):
        self.date = datetime.datetime.now()

    @staticmethod
    def get_instance():
        if Clock.instance is not None:
            return Clock.instance
        else:
            Clock.instance = Clock()
            return Clock.instance
