# kn20


#Подключаем библотеки (в том числе mpmath для реализции функций sin, cos и т.д)
import tkinter as tk
from tkinter import messagebox
from mpmath import *
mp.dps = 25; mp.pretty = True

#Добавление элементов

def add_digit(digit):
    value = calc.get()
    if value [0] == '0' and len(value) == 1:
        value = value [1:]
    calc['state'] = tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,value+digit)
    calc['state'] = tk.DISABLED

#Операции в калькуляторе

def add_operation(operation):
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value[-1] in '-+/*':
        value = value [:-1]    
    calc.delete(0,tk.END)
    calc.insert(0,value+operation)
    calc['state'] = tk.DISABLED

# Основные функции нашего калькулятора   

def calculate():
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value [-1] in '+-/*':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'Нужно вводить цифры. Вы ввели другие символы')
        calc.insert(0,0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль не делится, придурок')
        calc.insert (0,0)
    calc['state'] = tk.DISABLED

#Кнопочки стереть. 1 число и все, что находится в поле 

def clear_all():
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0,0)
    calc['state'] = tk.DISABLED

def clear():
    calc['state'] = tk.NORMAL
    value = calc.get()
    if len(value) == 1:
        value  = '0'
    else:
        value = value[0:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value)
    calc['state'] = tk.DISABLED

#Перевод числа с бинарного в двоичный и наоборот

def binary():
    calc['state'] = tk.NORMAL
    value = calc.get()
    calc.delete(0,tk.END)
    value = bin(int(value))
    value = value[2:]
    calc.insert(0, value)
    calc['state'] = tk.DISABLED

def dec():
    calc['state'] = tk.NORMAL
    value = calc.get()
    calc.delete(0,tk.END)
    value = str(int(value, 2))
    calc.insert(0, value)
    calc['state'] = tk.DISABLED

def make_digit_button(digit):
    return tk.Button(text =digit, font = ('Arial', 13), command = lambda: add_digit(digit))
                     
def make_operation_button(operation):
    return tk.Button(text = operation, font = ('Arial', 13), command = lambda: add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text = operation, font = ('Arial', 13), command = calculate)

def make_clear_button(operation):
    return tk.Button(text = operation, font = ('Arial', 13), command = clear)

def make_clear_all_button(operation):
    return tk.Button(text = operation, font = ('Arial', 13), command = clear_all)

#ввод с клавиатуры

def press_key(event):
    calc['state'] = tk.NORMAL
    print(event)
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '-+/*':
        add_operation (event.char)
    elif event.char == '\r':
        calculate()
        calc['state'] = tk.DISABLED

#Размер окна калькулятора

win = tk.Tk()
win.geometry(f"355x330+100+200")
win['bg'] = '#8A2BE2'
win.wm_attributes('-alpha', 0.95)
win.title('Калькулятор')

win.bind('<Key>', press_key)

win.resizable(width = False, height = False)

calc = tk.Entry(win, justify = tk.RIGHT,font = ('Arial' ,15), fg = 'red' ,width=20)
calc.insert (0, '0')
calc['state'] = tk.DISABLED
calc.grid (row = 0, column = 0, columnspan = 6, stick = 'we')

#Кнопки в калькуляторе 

make_digit_button('1').grid(row = 1, column = 0, stick = 'wens',padx = 5, pady = 5)
make_digit_button('2').grid(row = 1, column = 1, stick = 'wens',padx = 5, pady = 5)
make_digit_button('3').grid(row = 1, column = 2, stick = 'wens',padx = 5, pady = 5)
make_digit_button('4').grid(row = 2, column = 0, stick = 'wens',padx = 5, pady = 5)
make_digit_button('5').grid(row = 2, column = 1, stick = 'wens',padx = 5, pady = 5)
make_digit_button('6').grid(row = 2, column = 2, stick = 'wens',padx = 5, pady = 5)
make_digit_button('7').grid(row = 3, column = 0, stick = 'wens',padx = 5, pady = 5)
make_digit_button('8').grid(row = 3, column = 1, stick = 'wens',padx = 5, pady = 5)
make_digit_button('9').grid(row = 3, column = 2, stick = 'wens',padx = 5, pady = 5)
make_digit_button('0').grid(row = 4, column = 1, stick = 'wens',padx = 5, pady = 5)
make_digit_button('(').grid(row = 5, column = 2, stick = 'wens',padx = 5, pady = 5)
make_digit_button(')').grid(row = 5, column = 3, stick = 'wens',padx = 5, pady = 5)
make_digit_button('sin(').grid(row = 1, column = 4, stick = 'wens',padx = 5, pady = 5)
make_digit_button('cos(').grid(row = 2, column = 4, stick = 'wens',padx = 5, pady = 5)
make_digit_button('tan(').grid(row = 3, column = 4, stick = 'wens',padx = 5, pady = 5)
make_digit_button('sec(').grid(row = 1, column = 5, stick = 'wens',padx = 5, pady = 5)
make_digit_button('csc(').grid(row = 2, column = 5, stick = 'wens',padx = 5, pady = 5)
make_digit_button('ctg(').grid(row = 3, column = 5, stick = 'wens',padx = 5, pady = 5)
make_digit_button('Lg').grid(row = 4, column = 5, stick = 'wens',padx = 5, pady = 5)
make_digit_button('Ln').grid(row = 4, column = 4, stick = 'wens',padx = 5, pady = 5)
tk.Button(text='Bin',font=('Arial', 13), command = binary).grid(row=5, column=4, stick='wens', padx = 5, pady = 5)
tk.Button(text='Dec',font=('Arial', 13), command = dec).grid(row=5, column=5, stick='wens', padx = 5, pady = 5)

make_operation_button('+').grid(row = 1, column = 3, stick = 'wens',padx = 5, pady = 5)
make_operation_button('-').grid(row = 2, column = 3, stick = 'wens',padx = 5, pady = 5)
make_operation_button('/').grid(row = 3, column = 3, stick = 'wens',padx = 5, pady = 5)
make_operation_button('*').grid(row = 4, column = 3, stick = 'wens',padx = 5, pady = 5)
make_operation_button('%').grid(row = 5, column = 1, stick = 'wens',padx = 5, pady = 5)


make_calc_button('=').grid(row = 4, column = 2, stick = 'wens',padx = 5, pady = 5)
make_clear_button('CE').grid(row = 4, column = 0, stick = 'wens',padx = 5, pady = 5)
make_clear_all_button('C').grid(row = 5, column = 0, stick = 'wens',padx = 5, pady = 5)

#Строки и столбцы

win.grid_columnconfigure(0,minsize = 60)
win.grid_columnconfigure(1,minsize = 60)
win.grid_columnconfigure(2,minsize = 60)
win.grid_columnconfigure(3,minsize = 60)
win.grid_columnconfigure(4,minsize = 60)


win.grid_rowconfigure(1,minsize = 60)
win.grid_rowconfigure(2,minsize = 60)
win.grid_rowconfigure(3,minsize = 60)
win.grid_rowconfigure(4,minsize = 60)
win.grid_rowconfigure(5,minsize = 60)

win.mainloop()
