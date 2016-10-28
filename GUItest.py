from Tkinter import *
import Tkinter

top = Tkinter.Tk()
b1 = Tkinter.Button(top, text="add")
b2 = Tkinter.Button(top, text="return")
b1.pack()
b2.pack()
v = Tkinter.StringVar()
v.set("Let's begin")
e = Tkinter.Entry(top, textvariable=v)
e.pack()
list = []

def bt1():
    text = v.get()
    list.append(text)
    print list

listbox = Tkinter.Listbox(top, height=3)
listbox.pack()

def tt1():
    listbox.delete(0,END)
    for item in list:
        listbox.insert(END,item)




b1.configure(command=bt1)
b2.configure(command=tt1)
top.mainloop()