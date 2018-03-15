import tkinter
import YearFrame, IndependentMonthFrame
from Clock import *
from tkinter.font import Font
import MonthFrame


class CalendarFrame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.clock = Clock.get_instance()

        self.yearCalendar = YearFrame.YearFrame(master=self)
        self.yearCalendar.mouse_binding(self.choose_month)
        self.monthCalendar = IndependentMonthFrame.IndependentMonthFrame(master=self)
        self.calendarType = "year"

        self.next_button = tkinter.Button(text="->", bg="white", font=Font(weight="bold", size=20),
                                          command=self.next_function, master=self)
        self.prev_button = tkinter.Button(text="<-", bg="white", font=Font(weight="bold", size=20),
                                          command=self.prev_function, master=self)
        self.switch_button = tkinter.Button(text="Change View", bg="white", font=Font(weight="bold", size=20),
                                            command=self.switch_mode, master=self)
        self.today_button = tkinter.Button(text="Today", bg="white", font=Font(weight="bold", size=20),
                                           command=self.jump_to_today, master=self)

        self.show_calendar()
        self.place_content()
        self.grid()

    def show_calendar(self):
        if self.calendarType == "year":
            self.yearCalendar.grid(row=2, column=0, columnspan=4)
            self.monthCalendar.grid_remove()
        elif self.calendarType == "month":
            self.yearCalendar.grid_remove()
            self.monthCalendar.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
        self.update()

    def place_content(self):
        self.prev_button.grid(row=1, column=0)
        self.switch_button.grid(row=1, column=1)
        self.today_button.grid(row=1, column=2)
        self.next_button.grid(row=1, column=3)

    def switch_mode(self):
        if self.calendarType == "year":
            self.calendarType = "month"
        else:
            self.yearCalendar.update_year(self.monthCalendar.showingYear)
            self.calendarType = "year"
        self.show_calendar()

    def next_function(self):
        if self.calendarType == "year":
            self.yearCalendar.update_year(self.yearCalendar.showingYear+1)
        else:
            if self.monthCalendar.showingMonth == 12:
                self.monthCalendar.update_month(1, self.monthCalendar.showingYear+1)
            else:
                self.monthCalendar.update_month(self.monthCalendar.showingMonth + 1, self.monthCalendar.showingYear)

    def prev_function(self):
        if self.calendarType == "year":
            self.yearCalendar.update_year(self.yearCalendar.showingYear-1)
        else:
            if self.monthCalendar.showingMonth == 1:
                self.monthCalendar.update_month(12, self.monthCalendar.showingYear-1)
            else:
                self.monthCalendar.update_month(self.monthCalendar.showingMonth - 1, self.monthCalendar.showingYear)

    def jump_to_today(self):
        if self.calendarType == "year":
            self.yearCalendar.update_year(Clock.get_instance().currentYear)
        else:
            self.monthCalendar.update_month(Clock.get_instance().currentMonth, Clock.get_instance().currentYear)

    def choose_month(self, event):
        month = Clock.monthDict.index(event.widget["text"])
        self.monthCalendar.update_month(month=month, year=self.yearCalendar.showingYear)
        self.switch_mode()

