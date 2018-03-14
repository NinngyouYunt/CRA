import tkinter as tk
import MonthFrame
import CalendarFrame


root = tk.Tk(className="FrameTesting")
root.config(bg="white")
cf = CalendarFrame.CalendarFrame(root)

root.mainloop()
