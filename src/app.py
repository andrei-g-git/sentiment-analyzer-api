from tkinter import Tk, Canvas, Label
import threading

root = Tk()

canvas = Canvas(
    root,
    width=480,
    height=320
)
canvas.grid(columnspan=3, rowspan=3)

port = "123"
running_label = Label(root, text="running on port " + port + " ...")
running_label.grid(column=1, row=1)

def delete_this(arg1):
    print("seriously, delete it")

thread_2 = threading.Thread(target=delete_this, args=(345))
thread_2.start()

root.mainloop()