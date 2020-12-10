from tkinter import *
from tkinter import ttk

root = Tk()
root.title("hoge2")

mainframe=ttk.Frame(root,padding=30)
frame2=ttk.Frame(mainframe,padding=20)
lab1=ttk.Label(frame2,text="hello world hoge2")

mainframe.pack()
frame2.pack()
lab1.pack()

root.mainloop()