import tkinter as tk
import CalendarFrame


root = tk.Tk(className="FrameTesting")
root.config(bg="white")
cf = CalendarFrame.CalendarFrame(root)


root.mainloop()