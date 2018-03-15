import MonthFrame
from Clock import *

class IndependentMonthFrame(MonthFrame.MonthFrame):
    def __init__(self, master=None):
        super().__init__(month=Clock.get_instance().currentMonth, master=master)

    def place_content(self):
        super().place_content()
        self.monthTitle.config(text=str(Clock.monthDict[self.showingMonth-1])+" "+str(self.showingYear))

    def update_graphics(self):
        super().update_graphics()
        self.monthTitle.config(text=str(Clock.monthDict[self.showingMonth-1])+" "+str(self.showingYear))
