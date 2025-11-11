"""
simple_calculator.py
A simple Tkinter calculator that demonstrates:
 - Labels for text
 - Entry widgets for number input
 - Buttons for operations (+, -, *, /)
 - A Label to display the result
 - Clear button and basic input validation
Works with Python 3.x
"""

import tkinter as tk
from tkinter import ttk, messagebox

def safe_float(s):
    try:
        return float(s)
    except ValueError:
        return None

class SimpleCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        pad = {"padx": 8, "pady": 6}

        # Label + Entry for first number
        ttk.Label(self, text="Number 1:").grid(row=0, column=0, sticky="w", **pad)
        self.num1_entry = ttk.Entry(self, width=20)
        self.num1_entry.grid(row=0, column=1, **pad)
        self.num1_entry.focus()

        # Label + Entry for second number
        ttk.Label(self, text="Number 2:").grid(row=1, column=0, sticky="w", **pad)
        self.num2_entry = ttk.Entry(self, width=20)
        self.num2_entry.grid(row=1, column=1, **pad)

        # Operation buttons
        buttons_frame = ttk.Frame(self)
        buttons_frame.grid(row=2, column=0, columnspan=2, pady=(0,8))
        btn_specs = [
            ("+", self.add),
            ("−", self.sub),
            ("×", self.mul),
            ("÷", self.div),
            ("Clear", self.clear)
        ]
        for i,(txt, cmd) in enumerate(btn_specs):
            b = ttk.Button(buttons_frame, text=txt, command=cmd, width=6)
            b.grid(row=0, column=i, padx=4)

        # Result label
        ttk.Label(self, text="Result:").grid(row=3, column=0, sticky="w", **pad)
        self.result_var = tk.StringVar(value="")
        self.result_label = ttk.Label(self, textvariable=self.result_var, width=20, relief="sunken", anchor="center")
        self.result_label.grid(row=3, column=1, **pad)

        # Bind Enter to addition (or you can change)
        self.bind("<Return>", lambda e: self.add())

    def get_inputs(self):
        a = safe_float(self.num1_entry.get().strip())
        b = safe_float(self.num2_entry.get().strip())
        if a is None or b is None:
            messagebox.showerror("Invalid input", "Please enter valid numbers in both fields.")
            return None, None
        return a, b

    def add(self):
        a, b = self.get_inputs()
        if a is None: return
        self.result_var.set(str(a + b))

    def sub(self):
        a, b = self.get_inputs()
        if a is None: return
        self.result_var.set(str(a - b))

    def mul(self):
        a, b = self.get_inputs()
        if a is None: return
        self.result_var.set(str(a * b))

    def div(self):
        a, b = self.get_inputs()
        if a is None: return
        if b == 0:
            messagebox.showerror("Math error", "Cannot divide by zero.")
            return
        self.result_var.set(str(a / b))

    def clear(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result_var.set("")
        self.num1_entry.focus()

if __name__ == "__main__":
    app = SimpleCalculator()
    app.mainloop()