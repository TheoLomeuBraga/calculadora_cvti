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

restart = True
variable_selected = 0
variables = ["",""]
operator = ""
result = ""

def clean_variables():
    global variable_selected,variables,operator,result,restart
    variable_selected = 0
    variables = ["",""]
    operator = ""
    result = ""
    restart = True

def calculate():
    
    print("calculate",variables[0],operator,variables[1])

    input_value.set(result)
    clean_variables()


def last_pressed_key(value):
    global variable_selected,restart,operator

    str_value = str(value)

    if restart:
        input_value.set(str_value)
        restart = False
    else:
        input_value.set(input_value.get() + str_value)
    
    
    if str_value.isdigit() :
        variables[variable_selected] = variables[variable_selected] + str_value
    else:
        operator = str_value
        if variable_selected < 1:
            variable_selected = 1



def set_style():
    window.tk_setPalette(background='#1E1E1E', foreground='#FFFFFF')
    style = ttk.Style()
    style.theme_use('clam')  # Escolha um tema base para personalizar (pode variar dependendo do sistema operacional)
    style.configure('.', background='#1E1E1E', foreground='#FFFFFF')
    style.configure('TButton', background='#333333', foreground='#FFFFFF')
    style.configure('TLabel', background='#1E1E1E', foreground='#FFFFFF')
    style.map('TButton', background=[('active', '#555555')])

def on_button_click(b):
    print(b)
            
    if b == '=': 
        calculate()
    elif  b == 'C': 
        clean_variables()
        input_value.set("")
    else:
        last_pressed_key(b) 
    

def start_window():

    
    set_style()

    row_val = 1
    col_val = 0

    input = tk.Label(window, textvariable=input_value, justify='right', font=('Arial', 14))
    input.grid(row=0, column=0, columnspan=4)

    for btn in buttons:

        #lf = lambda b=btn: last_pressed_key(b) if b != '=' else  calculate()
        
                    

        #tk.Button(window, text=btn, width=7, height=2,command=on_button_click).grid(row=row_val, column=col_val)
        tk.Button(window, text=btn, width=7, height=2,command=lambda b=btn: on_button_click(b)).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    



start_window()

window.mainloop()