import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def myl():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('400x400')
window.resizable(False, False)

button_add = tk.Button(window, text='+', width=5, height=3, command=add)
button_add.place(x=20, y=300)
button_sub = tk.Button(window, text='-', width=5, height=3, command=sub)
button_sub.place(x=120, y=300)

button_myl = tk.Button(window, text='x', width=5, height=3, command=myl)
button_myl.place(x=220, y=300)
button_div = tk.Button(window, text=':', width=5, height=3, command=div)
button_div.place(x=320, y=300)

number1_entry = tk.Entry(window, width=50)
number1_entry.place(x=50, y=50)
number1 = tk.Label(window, text='Первое число')
number1.place(x=50, y=20)

number2_entry = tk.Entry(window, width=50)
number2_entry.place(x=50, y=100)
number2 = tk.Label(window, text='Второе число')
number2.place(x=50, y=75)

answer_entry = tk.Entry(window, width=50)
answer_entry.place(x=50, y=200)
answer = tk.Label(window, text='Сумма')
answer.place(x=50, y=170)

window.mainloop()
