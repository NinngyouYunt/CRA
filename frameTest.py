import tkinter as tk
import MonthFrame


root = tk.Tk(className="FrameTesting")
root.config(bg="white")
calFrame = MonthFrame.MonthFrame(root, True)

root.mainloop()
