import tkinter
import MonthFrame, YearFrame


class CalendarFrame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        yf = YearFrame.YearFrame(14,3,2018,master=self)
        self.grid()