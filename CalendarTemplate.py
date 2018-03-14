import tkinter

class Template(tkinter.Frame):
    def __init__(self, day, month, year, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.currentDay = day
        self.currentMonth = month
        self.currentYear = year
        self.showingYear = self.currentYear
        self.showingMonth = self.currentMonth
        self.showingDay = self.currentDay
        self.grid()

    def update_showing_date(self, day, month, year):
        self.showingYear = day
        self.showingMonth = month
        self.showingDay = year
        self.update_graphics()

    def update_current_date(self, day, month, year):
        self.currentDay = day
        self.currentMonth = month
        self.currentYear = year

    def update_graphics(self):
        self.update()
