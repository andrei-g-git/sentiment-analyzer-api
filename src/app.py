from tkinter import Tk, Canvas, Label
import threading
from server import AnalyzerServer

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

#AnalyzerServer.init_analyzer()

thread_2 = threading.Thread(target=AnalyzerServer.init_server, args=("localhost", 9999))
thread_2.start()

root.mainloop()