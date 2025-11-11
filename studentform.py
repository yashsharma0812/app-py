import tkinter as tk
from tkinter import ttk, messagebox

class StudentForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Form with Validation")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        pad = {"padx": 8, "pady": 6}

        # Name
        ttk.Label(self, text="Name:").grid(row=0, column=0, sticky="w", **pad)
        self.name_entry = ttk.Entry(self, width=30)
        self.name_entry.grid(row=0, column=1, **pad)

        # Age
        ttk.Label(self, text="Age:").grid(row=1, column=0, sticky="w", **pad)
        self.age_entry = ttk.Entry(self, width=10)
        self.age_entry.grid(row=1, column=1, sticky="w", **pad)

        # Email
        ttk.Label(self, text="Email:").grid(row=2, column=0, sticky="w", **pad)
        self.email_entry = ttk.Entry(self, width=30)
        self.email_entry.grid(row=2, column=1, **pad)

        # Submit button
        ttk.Button(self, text="Submit", command=self.validate_form).grid(row=3, column=0, columnspan=2, pady=10)

    def validate_form(self):
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        email = self.email_entry.get().strip()

        # Validation checks
        if not name:
            messagebox.showerror("Validation Error", "Name cannot be empty.")
            return
        if not age.isdigit() or not (10 <= int(age) <= 100):
            messagebox.showerror("Validation Error", "Age must be a number between 10 and 100.")
            return
        if "@" not in email:
            messagebox.showerror("Validation Error", "Invalid email address. Must contain '@'.")
            return

        # If all valid
        messagebox.showinfo("Success", f"Form submitted successfully!\n\nName: {name}\nAge: {age}\nEmail: {email}")

if __name__ == "__main__":
    app = StudentForm()
    app.mainloop()