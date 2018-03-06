import tkinter as tk
from tkinter.font import Font
import calendar as cal


class MonthFrame(tk.Frame):
    # each month is a 6 by 7 matrix (without week and header)
    # each year could be in 4 by 3 or 3 by 4

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        # define dict for month
        self.monthDict = {1: "January", 2: "February", 3: "March", 4: "April",
                          5: "May", 6: "June", 7: "July", 8: "August",
                          9: "September", 10: "October", 11: "November", 12: "December"}
        self.weekDict = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday",
                         4: "Thursday", 5: "Friday", 6: "Saturday"}
        self.calendar = cal.Calendar(firstweekday=6)
        # setting the font
        self.font = Font(size=10)
        # initialize fields
        self.days = []
        self.currentDay = 1
        self.currentMonth = 1
        self.currentYear = 2018
        self.showingDay = self.currentDay
        self.showingMonth = self.currentMonth
        self.showingYear = self.currentYear
        self.showingCalendar = self.calendar.monthdays2calendar(self.showingYear, self.showingMonth)
        self.monthTitle = self.create_tk_label(text=self.monthDict[self.showingMonth]+" "+str(self.showingYear))
        self.weekTitle = []
        self.create_content()

    # A working attempt to fill the 2D list of labels with correct dates
    # Require a little bit more re-work
    def show_date(self):
        showing_calendar = self.calendar.monthdays2calendar(self.showingYear, self.showingMonth)
        for week in range(len(self.showingCalendar)):
            for day in range(7):
                if self.showingCalendar[week][day][0] != 0:
                    self.days[week][day].configure(text=showing_calendar[week][day][0])
                    self.days[week][day].configure(font=Font(weight="bold"))
                elif week == 0:
                    self.days[week][day].configure(text=-1)
        if self.showingMonth == 1:
            prev_month_calendar = self.calendar.monthdays2calendar(self.showingYear-1, 12)
            next_month_calendar = self.calendar.monthdays2calendar(self.showingYear, self.showingMonth+1)
        elif self.showingMonth == 12:
            prev_month_calendar = self.calendar.monthdays2calendar(self.showingYear, self.showingMonth-1)
            next_month_calendar = self.calendar.monthdays2calendar(self.showingYear+1, 1)
        else:
            prev_month_calendar = self.calendar.monthdays2calendar(self.showingYear, self.showingMonth-1)
            next_month_calendar = self.calendar.monthdays2calendar(self.showingYear, self.showingMonth+1)
        print(next_month_calendar)
        for week in range(6):
            for day in range(7):
                if self.days[week][day]["text"] == -1:
                    self.days[week][day].configure(
                        text=prev_month_calendar[-1][day][0])
                elif self.days[week][day]["text"] == 0:
                    if week == 4:
                        self.days[week][day].configure(
                            text=next_month_calendar[0][day][0])
                        empty_row = True
                    elif week == 5:
                        if empty_row:
                            self.days[week][day].configure(
                                text=next_month_calendar[1][day][0])
                        else:
                            self.days[week][day].configure(
                                text=next_month_calendar[0][day][0])

    # Solution for assigning font to all label creations
    def create_tk_label(self, **kwargs):
        return tk.Label(font=self.font, **kwargs)

    # solution for assigning padding for all widget
    def grid_widget(self, widget, **kwargs):
        widget.grid(pady=2, padx=10, **kwargs)

    # change and add all the widget, call in __init__()
    def create_content(self):
        # title
        self.monthTitle.grid(row=0, columnspan=7)
        # week title
        for week in range(7):
            self.weekTitle.append(self.create_tk_label(text=self.weekDict[week][0:2]))
            self.grid_widget(self.weekTitle[week],column=week, row=1)
        # days
        for week in range(6):
            self.days.append([])
            for day in range(7):
                self.days[week].append(self.create_tk_label(text=0))
                self.days[week][day].grid(column=day, row=week+2)
        self.show_date()
