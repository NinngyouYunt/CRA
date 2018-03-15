import tkinter
from tkinter.font import Font
import MonthFrame, Clock


class YearFrame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master=master, bg="white")
        self.showingYear = Clock.Clock.get_instance().currentYear
        # Displaying year-view
        self.months = []

        self.yearTitle = tkinter.Label(master=self, bg="white", font=Font(size=20,weight="bold"))
        self.yearTitle.grid(row=0,column=0,columnspan=4)

        for i in range(12):
            self.months.append(MonthFrame.MonthFrame(master=self))
            self.months[i].grid(row=int(i/4)+1, column=i % 4, padx=5, pady=5)

        self.update_graphics()

    def update_graphics(self):
        self.yearTitle.config(text=self.showingYear)
        for i in range(len(self.months)):
            self.months[i].update_month(month=i+1, year=self.showingYear)
        self.update()

    def update_year(self, year):
        self.showingYear = year
        self.update_graphics()
