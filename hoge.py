from tkinter import *
from tkinter import ttk
def makebtn(test,root,btn_l):
    btn_l.append(ttk.Button(root,text=test,padding=20))

root = Tk()
root.title("hoge button test")

btns=[]

mainframe=ttk.Frame(root,padding=30)
frame2=ttk.Frame(mainframe,padding=30)

frame=frame2
for i in range(10):
    makebtn(i,frame2,btns)

mainframe.pack()
frame2.pack()
for i in range(0,10):
    btns[i].pack()

root.mainloop()