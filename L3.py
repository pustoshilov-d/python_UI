import math
import sys
from tkinter import *
import numpy as np
from tkinter import ttk

def func(a,b,c,x): return math.sqrt(c*x + 62.7 * math.exp(x))/(a*math.pow(x,2) + 7*x + b * math.log(x))

root=Tk()

ent1 = Entry(root); ent1.grid(row = 1, column = 1)
ent2 = Entry(root); ent2.grid(row = 2, column = 1)
ent3 = Entry(root); ent3.grid(row = 3, column = 1)
ent4 = Entry(root); ent4.grid(row = 4, column = 1)
ent5 = Entry(root); ent5.grid(row = 8, column = 0)
ent6 = Entry(root); ent6.grid(row = 8, column = 1)
ent7 = Entry(root); ent7.grid(row = 8, column = 2)

Label(root, text = "a").grid(row = 1, column = 0)
Label(root, text = "b").grid(row = 2, column = 0)
Label(root, text = "c").grid(row = 3, column = 0)
Label(root, text = "x").grid(row = 4, column = 0)
Label (root, text = "y").grid(row = 6, column = 0)
Label(root, text = "x_first").grid(row = 7, column = 0)
Label(root, text = "x_last").grid(row = 7, column = 1)
Label(root, text = "step").grid(row = 7, column = 2)

ent8 = Entry(root, state = "disabled")
ent8.grid(row = 6, column = 1)

def erorr_window():
    Er_win = Toplevel(root)
    Er_win.title("Ошибка")
    Label(Er_win, text = "Введите правильные значения").pack()
    ent1.delete(0,END); ent2.delete(0,END)
    ent3.delete(0,END); ent4.delete(0,END)
    ent5.delete(0,END); ent6.delete(0,END)
    ent7.delete(0,END)

def button1_clicked():
    try:
        arg = np.array((ent1.get(),ent2.get(),ent3.get(), ent4.get())).astype(float)
        y = func(arg[0],arg[1], arg[2], arg[3])
        ent8.config(state = "normal"); ent8.insert(0, y)
        ent8.config(state = "disabled")
    except:
        erorr_window()


button1 = Button(root, text= "Рассчёт", command=button1_clicked)
button1.grid(row = 5, column = 1)

tree = ttk.Treeview(root, columns = ["b","c","x","y"])
tree.grid(row = 10, columnspan = 5)
tree.column("#0", width=70)
tree.column("b", width=70)
tree.column("c", width=70)
tree.column("x", width=70)
tree.column("y", width=70)

tree.heading("#0", text = "a")
tree.heading("b", text = "b")
tree.heading("c", text = "c")
tree.heading("x", text = "x")
tree.heading("y", text = "y")

def button2_clicked():
    try:
        arg = np.array((ent1.get(),ent2.get(),ent3.get(), ent5.get(), ent6.get(), ent7.get())).astype(float)
        x_cur = arg[3]

        while (x_cur<=arg[4]):
            tree.insert("", "end", text = arg[0], values = (arg[1], arg[2], x_cur, func(arg[0],arg[1],arg[2],x_cur)))
            x_cur = x_cur + arg[5]
    except:
        erorr_window()

button2 = Button(root, text="Рассчёт_2", command=button2_clicked)
button2.grid(row = 9, column = 1)

root.mainloop()



