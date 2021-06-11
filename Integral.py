import time as t
from tkinter import *
from tkinter import ttk
import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as pl
from matplotlib.pyplot import mlab

fs = ('Calibri', 10)
x = ''
funcs = ['Синус', 'Косинус', 'Тангенс', 'Котангенс', 'Логарифмическая', 'Линейная', 'Квадратичная', 'Гипербола']
coefficients = [1, 1, 1]


def wod():
    print(ent.get())
    global x
    x = ent.get()
    return x


def callback_creator(input):
    def callback():
        if input != '':
            print(input)


def kf_creator(a, b, c):
    def kf():
        if a == '':
            print('Пусто')
            return
        q = int(a)
        w = int(b)
        e = int(c)
        sin_graph(q, w, e)
        return
    return kf


def sin_graph(q, w, e):

    ob = np.arange(-2, 2, 0.01)

    fig = pl.figure(1)
    pl.subplot(311)

    pl.plot(ob, q * sin(w * ob * pi) + e, 'g^')
    pl.axis([-1, 2, -1, 1])
    pl.title('sin')

    pl.show()


def sinx(x):
    Label(text='y = a * sin(b * '+x+') + c', font=fs).place_configure(x=10, y=140)
    # q1, w1, e1 = '', '', ''

    a1 = StringVar()
    b1 = StringVar()
    c1 = StringVar()

    # кооэфицент а
    Label(text='a =', font=fs).place_configure(x=10, y=180)
    a = Entry(width=5, textvariable=a1)
    a.config(bd=2)
    # a.pack()
    # a.place_configure(x=40, y=180)

    # кооэфицент b
    Label(text='b =', font=fs).place_configure(x=85, y=180)
    b = Entry(width=5, textvariable=b1)
    b.config(bd=2)
    # b.pack()
    # b.place_configure(x=115, y=180)

    # кооэфицент с
    Label(text='c =', font=fs).place_configure(x=160, y=180)
    c = Entry(width=5, textvariable=c1)
    c.config(bd=2)
    # c.pack()
    # c.place_configure(x=190, y=180)

    a.pack()
    a.place_configure(x=40, y=180)
    b.pack()
    b.place_configure(x=115, y=180)
    c.pack()
    c.place_configure(x=190, y=180)

    q1 = a1.get()
    w1 = b1.get()
    e1 = c1.get()

    btn3 = Button(text='Input', width=16, font=fs, command=kf_creator(q1, w1, e1))
    btn3.pack()
    btn3.place_configure(x=110, y=220)



def cosx(x):
    Label(text='y = a * cos(b * ' + x + ') + c', font=fs).place_configure(x=10, y=140)

    # кооэфицент а
    Label(text='a =', font=fs).place_configure(x=10, y=180)
    a = Entry(width=5)
    a.config(bd=2)
    a.pack()
    a.place_configure(x=40, y=180)

    # кооэфицент b
    Label(text='b =', font=fs).place_configure(x=85, y=180)
    b = Entry(width=5)
    b.config(bd=2)
    b.pack()
    b.place_configure(x=115, y=180)

    # кооэфицент с
    Label(text='c =', font=fs).place_configure(x=160, y=180)
    c = Entry(width=5)
    c.config(bd=2)
    c.pack()
    c.place_configure(x=190, y=180)


def choice():
    print(cmb.get())
    after_chs = cmb.get()
    if after_chs == "Синус":
        sinx(x)
    if after_chs == "Косинус":
        cosx(x)


# window settings
window = Tk()
window.geometry('800x700')
window.grid()

# main comment
lbl = Label(text='Укажите параметры функции', font=('Calibri', 14))
lbl.pack()
lbl.place_configure(x=10, y=5)

# input fields
Label(text='Введите имя зависимой переменной', font=fs).place_configure(x=10, y=30)
ent = Entry(width=20)
ent.config(bd=2)
ent.pack()
ent.place_configure(x=12, y=55)
btn1 = Button(text='Input', font=fs, command=wod)
btn1.place_configure(x=150, y=51.5)


Label(text='Выберите вид функции из выпадающего списка', font=fs).place_configure(x=10, y=80)
cmb = ttk.Combobox(window, values=funcs, width=15, font=fs)
cmb.place_configure(x=10, y=105)
cmb.current(0)
btn2 = Button(text='Input', font=fs, command=choice)
btn2.place_configure(x=150, y=103)


window.mainloop()
