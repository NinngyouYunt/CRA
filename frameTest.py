import tkinter as tk
import MonthFrame
import YearFrame


root = tk.Tk(className="FrameTesting")
root.config(bg="white")
yf = YearFrame.YearFrame(root)

root.mainloop()