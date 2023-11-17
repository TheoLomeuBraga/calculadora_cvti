import tkinter as tk
from tkinter import ttk

window = tk.Tk()

buttons = [
    '7', '8', '9','+',
    '4', '5', '6','-',
    '1', '2', '3','/',
    '0', 'C', '=','*'
]

input_value = tk.StringVar()

variables = ["0","0"]
operator = "+"
result = "0"

def calculate():
    print("calculate")


def last_pressed_key(valor):
    input_value.set(input_value.get() + str(valor))
    print(valor)





def start_window():

    row_val = 1
    col_val = 0

    input = tk.Label(window, textvariable=input_value, justify='right', font=('Arial', 14))
    input.grid(row=0, column=0, columnspan=4)

    for btn in buttons:
        tk.Button(window, text=btn, width=7, height=2,command=lambda b=btn: last_pressed_key(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    



start_window()

window.mainloop()