import tkinter
from TODO.TodoItemList import TodoItemList
from TODO.TodoItem import TodoItem
from TODO.Event import Event


tk = tkinter.Tk()

eventList = [
    Event("Event1"
          "12345678901234567890", "Content1", 1, [2018, 3, 14], [5,10], True, True),
    Event("Event2", "Content2", 2, [2018, 12, 11], [13,20], False, True, ),
]
print(eventList[0].dueTime)
print(eventList[0].get_due_time())

print(eventList[0].dueDate)
print(eventList[0].get_due_date())

itemList = TodoItemList(eventList, master=tk)

itemList.grid()

tk.mainloop()