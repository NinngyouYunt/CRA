import datetime


# Implementation of Singleton Design pattern
class Clock:
    instanceCount = 0
    instance = None
    # Used for other classes to reference and access
    # Change name to tuple
    monthTuple = ("January", "February", "March", "April",
                  "May", "June", "July", "August",
                  "September", "October", "November", "December")
    weekTuple = ("Sunday", "Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday")

    # Should never be called somewhere else
    # Should be private
    def __init__(self):
        self.date = datetime.datetime.now()
        self.currentDay = self.date.day
        self.currentMonth = self.date.month
        self.currentYear = self.date.year

    def update(self):
        self.date = datetime.datetime.now()

    # Use this method to get an instance, not constructor
    @staticmethod
    def get_instance():
        # Insuring that only one instance is ever created in a runtime
        if Clock.instance is not None:
            return Clock.instance
        else:
            Clock.instance = Clock()
            return Clock.instance
