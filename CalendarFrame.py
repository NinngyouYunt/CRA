import tkinter
import MonthFrame


class CalendarFrame(tkinter.Frame):
    def __init__(self, master=None, is_year_view=True):
        super().__init__(master)
        # Displaying year-view
        self.months = []
        '''
        for i in range(1):
            self.months.append(MonthFrame.MonthFrame(1, i+1, 2018, simple=is_year_view, master=self))
            self.months[i].grid(row=0, column=i)
        '''
        self.months.append(MonthFrame.MonthFrame(1, 1, 2018, simple=is_year_view, master=self))
        self.months[0].grid(row=0, column=0, rowspan=10)
        print(self.months[0].winfo_reqwidth())
        #self.months.append(MonthFrame.MonthFrame(1, 2, 2018, simple=is_year_view, master=self))
        #self.months[0].grid(row=1, column=0)

        self.grid()

    def change_view(self, mode):
        pass