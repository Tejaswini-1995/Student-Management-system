import tkinter as tk
import mysql.connector
from tkinter import messagebox

# MySQL Configuration
db = mysql.connector.connect(
    host='localhost', user='root', password='root', database='student_management'
)
cursor = db.cursor()

# GUI Configuration
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x300")

# Page 1: Home
home_frame = tk.Frame(root)

def go_to_add_page():
    home_frame.pack_forget()
    add_frame.pack()

def go_to_view_page():
    home_frame.pack_forget()
    view_frame.pack()
    display_students()

add_button = tk.Button(home_frame, text="Add Student", command=go_to_add_page)
add_button.pack(pady=10)

view_button = tk.Button(home_frame, text="View Students", command=go_to_view_page)
view_button.pack(pady=10)

home_frame.pack()

# Page 2: Add Student
add_frame = tk.Frame(root)

def add_student():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()

    sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)

    cursor.execute(sql, values)
    db.commit()

    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

    name_entry.focus()

    messagebox.showinfo("Success", "Student added successfully!")

def go_to_home_page():
    add_frame.pack_forget()
    home_frame.pack()

name_label = tk.Label(add_frame, text="Name:")
name_label.pack()
name_entry = tk.Entry(add_frame)
name_entry.pack(pady=5)

age_label = tk.Label(add_frame, text="Age:")
age_label.pack()
age_entry = tk.Entry(add_frame)
age_entry.pack(pady=5)

grade_label = tk.Label(add_frame, text="Grade:")
grade_label.pack()
grade_entry = tk.Entry(add_frame)
grade_entry.pack(pady=5)

add_student_button = tk.Button(add_frame, text="Add", command=add_student)
add_student_button.pack(pady=10)

back_button = tk.Button(add_frame, text="Back", command=go_to_home_page)
back_button.pack(pady=10)

# Page 3: View Students
view_frame = tk.Frame(root)

def display_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    for student in students:
        student_label = tk.Label(view_frame, text=f"Name: {student[0]}, Age: {student[1]}, Grade: {student[2]}")
        student_label.pack()

def go_to_home_page_from_view():
    view_frame.pack_forget()
    home_frame.pack()

back_button_from_view = tk.Button(view_frame, text="Back", command=go_to_home_page_from_view)
back_button_from_view.pack(pady=10)

# Run the GUI
root.mainloop()
