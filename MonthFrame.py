import tkinter as tk
from tkinter.font import Font
import calendar as cal


class MonthFrame(tk.Frame):
    # each month is a 6 by 7 matrix (without week and header)
    # each year could be in 4 by 3 or 3 by 4

    monthDict = {1: "January", 2: "February", 3: "March", 4: "April",
                 5: "May", 6: "June", 7: "July", 8: "August",
                 9: "September", 10: "October", 11: "November", 12: "December"}
    weekDict = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday",
                4: "Thursday", 5: "Friday", 6: "Saturday"}

    def __init__(self, day, month, year, master=None, simple=False):
        super().__init__(master, bg="white")
        self.isSimpleMode = simple
        self.calendar = cal.Calendar(firstweekday=6)
        # setting the font
        self.font = Font(size=10)
        # initialize fields
        self.days = []
        self.currentDay = day
        self.currentMonth = month
        self.currentYear = year
        self.showingDay = self.currentDay
        self.showingMonth = self.currentMonth
        self.showingYear = self.currentYear
        self.monthTitle = tk.Label(master=self)
        self.weekTitle = []
        self.place_content()

    # Filling self.days with the actually date
    # Will be called to update the date if month changes
    def update_date(self):
        # Getting all the dates from Calendar module
        current_month = self.calendar.monthdays2calendar(self.showingYear, self.showingMonth)
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
                if len(current_month) > week:
                    if current_month[week][day][0] != 0:
                        self.days[week][day].config(text=current_month[week][day][0])
                        self.days[week][day].config(font=Font(weight="bold"))
                    elif current_month[week][day][0] == 0:
                        if self.isSimpleMode is not True:
                            if week < 1:
                                self.days[week][day].config(text=prev_month[-1][day][0])
                            else:
                                self.days[week][day].config(text=next_month[starting][day][0])
                                if day == 6:
                                    starting += 1
                        else:
                            self.days[week][day].config(text="")
                else:
                    if self.isSimpleMode is not True:
                        self.days[week][day].config(text=next_month[starting][day][0])
                    else:
                        self.days[week][day].config(text="")

    # Add widgets into the frame, call in __init__()
    def place_content(self):
        # Placing title Label
        self.monthTitle.config(text=self.monthDict[self.showingMonth]+" "+str(self.showingYear),
                               font=self.font, bg="white")
        if self.isSimpleMode:
            self.monthTitle.config(text=self.monthDict[self.showingMonth])
        self.monthTitle.config(font=Font(weight="bold"))
        self.monthTitle.grid(row=0, column=0, columnspan=7)
        # Placing week title Label
        for weekTitle in range(7):
            self.weekTitle.append(tk.Label(master=self, text=self.weekDict[weekTitle][0:2], font=self.font, bg="white"))
            self.weekTitle[weekTitle].grid(row=1, column=weekTitle, pady=2, padx=5)
        # Placing days Label
        for week in range(6):
            self.days.append([])
            for day in range(7):
                self.days[week].append(tk.Label(master=self,font=self.font, bg="white"))
                self.days[week][day].grid(row=week+2, column=day)
        self.update_date()

    def update_calendar(self, month, year):
        self.showingYear = year
        self.showingMonth = month
        self.update_date()

    def change_mode(self, mode):
        if type(mode) is str:
            if mode[0] == 's':
                self.isSimpleMode = True
            elif mode[0] == 'c':
                self.isSimpleMode = False
        else:
            self.isSimpleMode = mode

    def get_shwoingMonth(self):
        return self.showingMonth