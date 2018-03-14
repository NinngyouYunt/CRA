import tkinter
from tkinter.font import Font
import MonthFrame


class YearFrame(tkinter.Frame):
    def __init__(self, master=None, is_year_view=True):
        super().__init__(master, bg="white")
        # Displaying year-view
        self.months = []
        self.currentYear = 2018
        self.showingYear = self.currentYear

        self.yearTitle = tkinter.Label(master=self, bg="white", font=Font(size=20,weight="bold"))
        self.yearTitle.grid(row=0,column=1,columnspan=2)

        self.prevYearButton = tkinter.Button(master=self,text="<-", bg="white", font=Font(size=20, weight="bold"),
                                             command=self.show_prev_year)
        self.prevYearButton.grid(row=0,column=0)

        self.nextYearButton = tkinter.Button(master=self, text="->", bg="white", font=Font(size=20, weight="bold"),
                                             command=self.show_next_year)
        self.nextYearButton.grid(row=0, column=3)

        for i in range(12):
                self.months.append(MonthFrame.MonthFrame(1, i+1, self.showingYear, simple=is_year_view, master=self))
                self.months[i].grid(row=int(i/4)+1, column=i % 4, padx=5, pady=5)

        self.update_calendar()
        self.grid()

    def update_calendar(self):
        self.yearTitle.config(text=self.showingYear)
        for month in self.months:
            month.update_calendar(month.get_shwoingMonth(), self.showingYear)
        self.update()

    def show_next_year(self):
        self.showingYear = self.showingYear + 1
        self.update_calendar()

    def show_prev_year(self):
        self.showingYear = self.showingYear - 1
        self.update_calendar()

    def change_view(self, mode):
        pass