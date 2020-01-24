from tkinter import *
import numpy as np

def sum_pos(mass):
    result = 0
    for i in mass:
        if (int(i) > 0): result = result + int(i)
    return result

#1
mass = ["1","-25","0","18","26", "13"]
root1 = Tk()

label = Label(root1, text = "")
label.grid(row =1, columnspan = 3)

def cliked1():
    label["text"] = "Массиив:\n" + " ".join(mass)+"\n"+"Сумма положительных элементов\n"+ str(sum_pos(mass))

Button(root1, text = "Вычислить", command = cliked1).grid(row = 0, column = 1)

root1.mainloop()

#2
root2 = Tk()

ent = Entry(root2)
ent.grid(row = 0, columnspan = 3)

label = Label(root2, text = "")
label.grid(row =3, columnspan = 3)

def err():
    Er_win = Toplevel(root2)
    Er_win.title("Ошибка")
    Label(Er_win, text = "Введите правильные значения").pack()
    ent.delete(0,END)

def cliked1():
    try:
        mass = ent.get().split(" ")
        label["text"] = "Массиив:\n" + " ".join(mass) + "\n" + "Сумма положительных элементов\n" + str(sum_pos(mass))
    except: err()

Button(root2, text = "Вычислить", command = cliked1).grid(row = 1, column = 1)
root2.mainloop()


#2
root3 = Tk()

Label(root3, text = "Исходный массив").grid(row =0)

Label(root3, text = "Индекс").grid(row = 1, column = 0)
Label(root3, text = "0").grid(row = 1, column = 1)
Label(root3, text = "1").grid(row = 1, column = 2)
Label(root3, text = "2").grid(row = 1, column = 3)
Label(root3, text = "3").grid(row = 1, column = 4)
Label(root3, text = "4").grid(row = 1, column = 5)
Label(root3, text = "5").grid(row = 1, column = 6)

Label(root3, text = "Значение").grid(row = 2, column = 0)
ent0 = Entry(root3); ent0.grid(row = 2, column = 1)
ent1 = Entry(root3); ent1.grid(row = 2, column = 2)
ent2 = Entry(root3); ent2.grid(row = 2, column = 3)
ent3 = Entry(root3); ent3.grid(row = 2, column = 4)
ent4 = Entry(root3); ent4.grid(row = 2, column = 5)
ent5 = Entry(root3); ent5.grid(row = 2, column = 6)

label = Label(root3, text = " ")
label.grid(row = 5, columnspan = 6)


Label(root3, text = "Отсортированный массив").grid(row =6)
Label(root3, text = "Индекс").grid(row = 1, column = 0)
Label(root3, text = "0").grid(row = 7, column = 1)
Label(root3, text = "1").grid(row = 7, column = 2)
Label(root3, text = "2").grid(row = 7, column = 3)
Label(root3, text = "3").grid(row = 7, column = 4)
Label(root3, text = "4").grid(row = 7, column = 5)
Label(root3, text = "5").grid(row = 7, column = 6)

Label(root3, text = "Значение").grid(row = 2, column = 0)
ent01 = Entry(root3); ent01.grid(row = 8, column = 1)
ent11 = Entry(root3); ent11.grid(row = 8, column = 2)
ent21 = Entry(root3); ent21.grid(row = 8, column = 3)
ent31 = Entry(root3); ent31.grid(row = 8, column = 4)
ent41 = Entry(root3); ent41.grid(row = 8, column = 5)
ent51 = Entry(root3); ent51.grid(row = 8, column = 6)



def err():
    Er_win = Toplevel(root3)
    Er_win.title("Ошибка")
    Label(Er_win, text = "Введите правильные значения").pack()
    ent1.delete(0,END);    ent2.delete(0,END)
    ent3.delete(0,END);    ent4.delete(0,END)
    ent5.delete(0,END)

def cliked1():
    try:
        mass[0] = ent0.get();        mass[1] = ent1.get()
        mass[2] = ent2.get();        mass[3] = ent3.get()
        mass[4] = ent4.get();        mass[5] = ent5.get()
        label["text"] = "Массиив:\n" + " ".join(mass) + "\n" + "Сумма положительных элементов\n" + str(sum_pos(mass))


        np_mass = np.array(mass).astype(int);        np_mass.sort()
        ent01.insert(0, np_mass[0]);        ent11.insert(0, np_mass[1])
        ent21.insert(0, np_mass[2]);        ent31.insert(0, np_mass[3])
        ent41.insert(0, np_mass[4]);        ent51.insert(0, np_mass[5])

    except: err()
Button(root3, text = "Вычислить", command = cliked1).grid(row = 4, column = 3)

root3.mainloop()

