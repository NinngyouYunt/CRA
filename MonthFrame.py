import tkinter as tk
from tkinter.font import Font
import calendar as cal
from Clock import *


class MonthFrame(tk.Frame):
    # each month is a 6 by 7 matrix (without week and header)
    # each year could be in 4 by 3 or 3 by 4

    def __init__(self, month, master=None):
        super().__init__(master=master, bg="white")
        self.showingMonth = month
        self.showingYear = Clock.get_instance().currentYear
        self.calendar = cal.Calendar(firstweekday=6)
        # setting the font
        self.font = Font(size=10)
        # initialize fields
        self.days = []
        self.monthTitle = tk.Label(master=self)
        self.weekTitle = []
        self.place_content()

    # Add widgets into the frame, call in __init__()
    def place_content(self):
        # Placing title Label
        self.monthTitle.config(text=Clock.monthDict[self.showingMonth-1],
                               font=self.font, bg="white")
        self.monthTitle.config(font=Font(weight="bold"))
        self.monthTitle.grid(row=0, column=0, columnspan=7)
        # Placing week title Label
        for weekTitle in range(7):
            self.weekTitle.append(tk.Label(master=self, text=Clock.weekDict[weekTitle][0:2], font=self.font, bg="white"))
            self.weekTitle[weekTitle].grid(row=1, column=weekTitle, pady=2, padx=5)
        # Placing days Label
        for week in range(6):
            self.days.append([])
            for day in range(7):
                self.days[week].append(tk.Label(master=self,font=self.font, bg="white"))
                self.days[week][day].grid(row=week+2, column=day)
        self.update_graphics()

    # Filling self.days with the actually date
    # Will be called to update the date if month changes
    def update_graphics(self):
        # Getting all the dates from Calendar module
        current_month_calendar = self.calendar.monthdays2calendar(self.showingYear, self.showingMonth)
        prev_month = None
        next_month = None
        if 1 < self.showingMonth < 12:
            prev_month = self.calendar.monthdays2calendar(self.showingYear, self.showingMonth - 1)
            next_month = self.calendar.monthdays2calendar(self.showingYear, self.showingMonth + 1)
        elif self.showingMonth == 1:
            prev_month = self.calendar.monthdays2calendar(self.showingYear-1, 12)
            next_month = self.calendar.monthdays2calendar(self.showingYear, self.showingMonth + 1)
        elif self.showingMonth == 12:
            prev_month = self.calendar.monthdays2calendar(self.showingYear, self.showingMonth - 1)
            next_month = self.calendar.monthdays2calendar(self.showingYear+1, 1)
        # iterate through the list to fill in dates
        starting = 0
        for week in range(6):
            for day in range(7):
                if len(current_month_calendar) > week:
                    if current_month_calendar[week][day][0] != 0:
                        self.days[week][day].config(text=current_month_calendar[week][day][0])
                        self.days[week][day].config(font=Font(weight="bold"), fg="black")
                        if self.showingYear == Clock.get_instance().currentYear and \
                                self.showingMonth == Clock.get_instance().currentMonth and \
                                self.days[week][day]["text"] == Clock.get_instance().currentDay:
                            self.days[week][day].config(fg="blue")
                    elif current_month_calendar[week][day][0] == 0:
                        self.days[week][day].config(font=Font(weight="normal"))
                        if type(self) is not MonthFrame:
                            if week < 1:
                                self.days[week][day].config(text=prev_month[-1][day][0])
                            else:
                                self.days[week][day].config(text=next_month[starting][day][0])
                                if day == 6:
                                    starting += 1
                        else:
                            self.days[week][day].config(text="")
                else:
                    self.days[week][day].config(font=Font(weight="normal"))
                    if type(self) is not MonthFrame:
                        self.days[week][day].config(text=next_month[starting][day][0])
                    else:
                        self.days[week][day].config(text="")
        self.update()

    def update_month(self, month, year):
        self.showingYear = year
        self.showingMonth = month
        self.update_graphics()

    def mouse_binding(self, callback):
        self.monthTitle.bind("<Button-1>", callback)
