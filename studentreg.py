"""
student_registration.py
A simple student registration form using Tkinter and ttk.
Widgets used:
 - Label widgets for field names
 - Entry widgets for text input (Name, Age, Email)
 - Combobox for selecting Course
 - Buttons to Submit and Clear
Displays a confirmation message on successful submission.
"""

import tkinter as tk
from tkinter import ttk, messagebox

class StudentRegistration(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Registration Form")
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

        # Course (Combobox)
        ttk.Label(self, text="Course:").grid(row=3, column=0, sticky="w", **pad)
        courses = ["B.Sc", "B.Tech", "BCA", "M.Sc", "M.Tech", "MBA", "Other"]
        self.course_cb = ttk.Combobox(self, values=courses, state="readonly", width=27)
        self.course_cb.grid(row=3, column=1, **pad)
        self.course_cb.set(courses[0])

        # Gender (optional radio) to show more widgets
        ttk.Label(self, text="Gender:").grid(row=4, column=0, sticky="w", **pad)
        self.gender_var = tk.StringVar(value="Other")
        gender_frame = ttk.Frame(self)
        gender_frame.grid(row=4, column=1, sticky="w", **pad)
        ttk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, value="Male").pack(side="left")
        ttk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, value="Female").pack(side="left")
        ttk.Radiobutton(gender_frame, text="Other", variable=self.gender_var, value="Other").pack(side="left")

        # Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=(6,10))
        ttk.Button(btn_frame, text="Submit", command=self.submit).grid(row=0, column=0, padx=8)
        ttk.Button(btn_frame, text="Clear", command=self.clear).grid(row=0, column=1, padx=8)

    def clear(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.course_cb.set(self.course_cb["values"][0])
        self.gender_var.set("Other")
        self.name_entry.focus()

    def submit(self):
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        email = self.email_entry.get().strip()
        course = self.course_cb.get().strip()
        gender = self.gender_var.get()

        # Basic validations
        if not name:
            messagebox.showerror("Validation Error", "Name is required.")
            return
        if not age.isdigit() or not (1 <= int(age) <= 120):
            messagebox.showerror("Validation Error", "Please enter a valid age (1-120).")
            return
        if email and "@" not in email:
            messagebox.showerror("Validation Error", "Please enter a valid email address.")
            return

        # If all OK, show a summary
        summary = f"Name: {name}\nAge: {age}\nEmail: {email or 'N/A'}\nCourse: {course}\nGender: {gender}"
        messagebox.showinfo("Registration Successful", f"Student registered successfully:\n\n{summary}")
        # Optionally clear after successful submission
        self.clear()

if __name__ == "__main__":
    app = StudentRegistration()
    app.mainloop()