import tkinter as tk
from .. import *


class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.expression = ""

    def create_widgets(self):
        self.display = tk.Entry(self, font=(
            'Arial', 18), borderwidth=2, relief="sunken")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self, text=button, font=('Arial', 18), command=lambda b=button: self.button_click(
                b)).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(1, 5):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

    def button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Ошибка")
                self.expression = ""
        else:
            self.expression += str(char)
            self.display.insert(tk.END, char)

def run(app):
    app.create_window(title="Calculator", content=Calculator,
                      size=(50, 200, 500, 300), flags=WindowFlags.WN_RESIZABLE)
