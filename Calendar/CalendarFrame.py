import tkinter
from Calendar import IndependentMonthFrame, YearFrame
from Calendar.Clock import *
from tkinter.font import Font


class CalendarFrame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="white")
        # Creating all the frames
        self.yearCalendar = YearFrame.YearFrame(master=self)
        self.monthCalendar = IndependentMonthFrame.IndependentMonthFrame(master=self)
        self.binding_events()
        self.calendarType = "year"
        # Creating all the buttons
        self.next_button = tkinter.Button(text="->", bg="white", font=Font(weight="bold", size=20),
                                          command=self.next_function, master=self)
        self.prev_button = tkinter.Button(text="<-", bg="white", font=Font(weight="bold", size=20),
                                          command=self.prev_function, master=self)
        self.switch_button = tkinter.Button(text="Change View", bg="white", font=Font(weight="bold", size=20),
                                            command=self.switch_mode, master=self)
        self.today_button = tkinter.Button(text="Today", bg="white", font=Font(weight="bold", size=20),
                                           command=self.jump_to_today, master=self)
        # Displaying content
        self.show_calendar()
        self.place_content()
        self.grid()

    # Show the calendar that is matching self.calendarType
    def show_calendar(self):
        if self.calendarType == "year":
            self.yearCalendar.grid(row=2, column=0, columnspan=4)
            self.monthCalendar.grid_remove()
        elif self.calendarType == "month":
            self.yearCalendar.grid_remove()
            self.monthCalendar.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
        self.update()

    # Used only in constructor to grid all the widgets that are not frames
    def place_content(self):
        self.prev_button.grid(row=1, column=0)
        self.switch_button.grid(row=1, column=1)
        self.today_button.grid(row=1, column=2)
        self.next_button.grid(row=1, column=3)

    # Switch between each year and month calendar
    # Also change the displaying date depending on the date that was being viewed
    def switch_mode(self):
        if self.calendarType == "year":
            self.calendarType = "month"
        else:
            self.yearCalendar.update_year(self.monthCalendar.showingYear)
            self.calendarType = "year"
        self.show_calendar()

    # Action for next_button
    def next_function(self):
        if self.calendarType == "year":
            self.yearCalendar.update_year(self.yearCalendar.showingYear+1)
        else:
            if self.monthCalendar.showingMonth == 12:
                self.monthCalendar.update_month(1, self.monthCalendar.showingYear+1)
            else:
                self.monthCalendar.update_month(self.monthCalendar.showingMonth + 1, self.monthCalendar.showingYear)

    # Action for prev_button
    def prev_function(self):
        if self.calendarType == "year":
            self.yearCalendar.update_year(self.yearCalendar.showingYear-1)
        else:
            if self.monthCalendar.showingMonth == 1:
                self.monthCalendar.update_month(12, self.monthCalendar.showingYear-1)
            else:
                self.monthCalendar.update_month(self.monthCalendar.showingMonth - 1, self.monthCalendar.showingYear)

    # Action for today_button
    def jump_to_today(self):
        if self.calendarType == "year":
            self.yearCalendar.update_year(Clock.get_instance().currentYear)
        else:
            self.monthCalendar.update_month(Clock.get_instance().currentMonth, Clock.get_instance().currentYear)

    # The action that is passed to the YearFrame to switch from year to a specific month
    def click_month_title(self, month):
        self.monthCalendar.update_month(month=month, year=self.yearCalendar.showingYear)
        self.switch_mode()

    # action listener for clicking on each of the day label in a calendar
    def click_day(self, day, month, year):
        show = str(year)+"/"+str(month)+"/"+str(day)
        print(show, "was clicked")

    # Pass all the event callback that need to be bind into each frame
    def binding_events(self):
        self.yearCalendar.bind_to_month_title(self.click_month_title)
        self.yearCalendar.bind_to_days(self.click_day)
        self.monthCalendar.bind_action_days(self.click_day)
