import tkinter
from TODO import TodoItem, Event


tk = tkinter.Tk()
todoitem = TodoItem.TodoItem(Event.Event("title","content","10","2018/3/10", "1310", False, True, "2018/3/1"),
                             master=tk)

todoitem.grid(row=1, column=1)

tk.mainloop()