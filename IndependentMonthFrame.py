import MonthFrame


class IndependentMonthFrame(MonthFrame.MonthFrame):
    def __init__(self, master=None):
        super().__init__(master=master)

    def place_content(self):
        super().place_content()
        self.monthTitle.config(text=str(self.monthDict[self.showingMonth])+" "+str(self.showingYear))

    def update_graphics(self):
        super().update_graphics()
        self.monthTitle.config(text=str(self.monthDict[self.showingMonth])+" "+str(self.showingYear))
