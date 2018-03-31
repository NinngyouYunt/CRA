import tkinter
from TODO.TodoItemList import TodoItemList
from TODO.TodoItem import TodoItem
from TODO.Event import Event


tk = tkinter.Tk()
todoItem = TodoItem(Event("title","content","10","2018/3/10", "1310", False, True, "2018/3/1"),
                    master=tk)

eventList = [
    Event("Event1"
          "12345678901234567890", "Content1", 1, "2018/03/10", "0510", True, True, "2018/3/1"),
    Event("Event2", "Content2", 2, "2018/12/11", "1320", False, True, "2018/3/1"),
]

itemList = TodoItemList(eventList, master=tk)

itemList.grid()

tk.mainloop()