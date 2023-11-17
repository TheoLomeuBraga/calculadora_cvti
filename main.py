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

start = True
variable_selected = 0
variables = ["",""]
operator = ""
result = ""

def clean_variables():
    global variable_selected,variables,operator,result
    variable_selected = 0
    variables = ["",""]
    operator = ""
    result = ""

def calculate():
    
    print("calculate",variables[0],operator,variables[1])

    input_value.set(result)
    clean_variables()


def last_pressed_key(value):
    global variable_selected,start,operator

    str_value = str(value)

    if start:
        input_value.set(str_value)
        start = False
    else:
        input_value.set(input_value.get() + str_value)
    
    
    if str_value.isdigit() :
        variables[variable_selected] = variables[variable_selected] + str_value
    else:
        print(str_value)
        operator = str_value
        if variable_selected < 1:
            variable_selected = 1
    print(variables[variable_selected])





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