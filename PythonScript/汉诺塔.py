import tkinter.simpledialog
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("汉诺塔")
root.geometry('500x500')
# frm = ttk.Frame(root, padding=150)
# frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
num = tkinter.simpledialog.askinteger("输入汉诺塔个数",root)

ttk.Label(frm, text=num).grid(column=2, row=0)
# print(numEntry.get())
root.mainloop()
