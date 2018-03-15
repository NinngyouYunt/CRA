import tkinter
import YearFrame, IndependentMonthFrame, Clock
from tkinter.font import Font


class CalendarFrame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.clock = Clock.Clock.get_instance()

        self.yearCalendar = YearFrame.YearFrame(master=self)
        self.monthCalendar = IndependentMonthFrame.IndependentMonthFrame(master=self)
        self.calendarType = "year"

        self.next_button = tkinter.Button(text="->", bg="white", font=Font(weight="bold", size=20),
                                          command=self.next_function)
        self.prev_button = tkinter.Button(text="<-", bg="white", font=Font(weight="bold", size=20),
                                          command=self.prev_function)
        self.switch_button = tkinter.Button(text="Change", bg="white", font=Font(weight="bold", size=20),
                                          command=self.switch_mode)

        self.show_calendar()
        self.place_content()
        self.grid()

    def show_calendar(self):
        if self.calendarType == "year":
            self.yearCalendar.grid(row=2, column=1)
            self.monthCalendar.grid_remove()
        elif self.calendarType == "month":
            self.yearCalendar.grid_remove()
            self.monthCalendar.grid(row=2, column=1)
        self.update()

    def place_content(self):
        self.next_button.grid(row=1, column=2)
        self.prev_button.grid(row=1, column=0)
        self.switch_button.grid(row=1, column=1)

    def switch_mode(self):
        if self.calendarType == "year":
            self.calendarType = "month"
        else:
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
