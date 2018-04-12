import tkinter
from tkinter.font import Font
from Calendar import Clock, MonthFrame


class YearFrame(tkinter.Frame):
    def __init__(self, check_event_callback, master=None):
        super().__init__(master=master, bg="white",width=100)
        self.showingYear = Clock.Clock.get_instance().currentYear
        # Displaying year-view
        self.months = []

        self.yearTitle = tkinter.Label(master=self, bg="white", font=Font(size=20,weight="bold"))
        self.yearTitle.grid(row=0,column=0,columnspan=4)

        for i in range(12):
            self.months.append(MonthFrame.MonthFrame(i + 1, check_event_callback, master=self))
            self.months[i].grid(row=int(i/4)+1, column=i % 4, padx=5, pady=5)

        self.update_graphics()

    # Updating information in the months list and refreshing the frame
    # could be private
    def update_graphics(self):
        self.yearTitle.config(text=self.showingYear)
        for i in range(len(self.months)):
            self.months[i].update_month(month=i+1, year=self.showingYear)
        self.update()

    # Use to change the diaplayed year
    def update_year(self, year):
        self.showingYear = year
        self.update_graphics()

    # Pass the callback the months for binding to month titles
    def bind_to_month_title(self, callback):
        for month in self.months:
            month.bind_action_month_title(callback)

    # pass the callback to months for binding to days
    def bind_to_days(self, callback):
        for month in self.months:
            month.bind_action_days(callback)
