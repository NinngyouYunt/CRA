import tkinter
from tkinter.font import Font
import MonthFrame
import CalendarTemplate


class YearFrame(CalendarTemplate.Template):
    def __init__(self, day, month, year, master=None):
        super().__init__(day,month, year, master, bg="white")
        # Displaying year-view
        self.months = []

        self.yearTitle = tkinter.Label(master=self, bg="white", font=Font(size=20,weight="bold"))
        self.yearTitle.grid(row=0,column=1,columnspan=2)

        self.prevYearButton = tkinter.Button(master=self,text="<-", bg="white", font=Font(size=20, weight="bold"),
                                             command=self.show_prev_year)
        self.prevYearButton.grid(row=0,column=0)

        self.nextYearButton = tkinter.Button(master=self, text="->", bg="white", font=Font(size=20, weight="bold"),
                                             command=self.show_next_year)
        self.nextYearButton.grid(row=0, column=3)

        for i in range(12):
                self.months.append(MonthFrame.MonthFrame(1, i+1, self.showingYear, simple=True, master=self))
                self.months[i].grid(row=int(i/4)+1, column=i % 4, padx=5, pady=5)

        self.update_graphics()
        self.grid()

    def new_day(self, day, month, year):
        self.currentYear = year
        self.currentMonth = month
        self.currentDay = day

    def update_graphics(self):
        self.yearTitle.config(text=self.showingYear)
        for month in self.months:
            month.update_showing_date(self.showingDay, self.showingMonth, self.showingYear)

    def show_next_year(self):
        self.showingYear = self.showingYear + 1
        self.update_graphics()

    def show_prev_year(self):
        self.showingYear = self.showingYear - 1
        self.update_graphics()

    def change_view(self, mode):
        pass