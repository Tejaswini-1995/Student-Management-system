import tkinter as tk
import mysql.connector
from tkinter import messagebox

# MySQL Configuration
db = mysql.connector.connect(
    host='localhost',
    user='root', 
    password='root', 
    database='student_management'
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

def go_to_update_page():
    home_frame.pack_forget()
    update_frame.pack()

def go_to_delete_page():
    home_frame.pack_forget()
    delete_frame.pack()

def go_to_search_page():
    home_frame.pack_forget()
    search_frame.pack()

add_button = tk.Button(home_frame, text="Add Student", command=go_to_add_page)
add_button.pack(pady=10)

view_button = tk.Button(home_frame, text="View Students", command=go_to_view_page)
view_button.pack(pady=10)

update_button = tk.Button(home_frame, text="Update Student", command=go_to_update_page)
update_button.pack(pady=10)

delete_button = tk.Button(home_frame, text="Delete Student", command=go_to_delete_page)
delete_button.pack(pady=10)

search_button = tk.Button(home_frame, text="Search Student", command=go_to_search_page)
search_button.pack(pady=10)

home_frame.pack()

# Page 2: Add Student
add_frame = tk.Frame(root)

def add_student():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    mobile_number = mobile_number_entry.get()
    Aadhar_Card_Number = Aadhar_Card_Number_entry.get()
    Total_Fees = Total_Fees_entry.get()
    Fees_Paid = Fees_Paid_entry.get()
    Remaining_Fees = int(Total_Fees) - int(Fees_Paid)

    sql = "INSERT INTO student_Details (first_name, last_name, mobile_number, Aadhar_Card_Number, Total_Fees, Fees_Paid, Remaining_Fees) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (first_name, last_name, mobile_number, Aadhar_Card_Number, Total_Fees, Fees_Paid, Remaining_Fees)

    cursor.execute(sql, values)
    db.commit()

    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    mobile_number_entry.delete(0, tk.END)
    Aadhar_Card_Number_entry.delete(0, tk.END)
    Total_Fees_entry.delete(0, tk.END)
    Fees_Paid_entry.delete(0, tk.END)

    first_name_entry.focus()

    tk.messagebox.showinfo("Success", "Student added successfully!")

def go_to_home_page():
    add_frame.pack_forget()
    home_frame.pack()

first_name_label = tk.Label(add_frame, text="First Name:")
first_name_label.pack()
first_name_entry = tk.Entry(add_frame)
first_name_entry.pack(pady=5)

last_name_label = tk.Label(add_frame, text="Last Name:")
last_name_label.pack()
last_name_entry = tk.Entry(add_frame)
last_name_entry.pack(pady=5)

mobile_number_label = tk.Label(add_frame, text="Mobile Number:")
mobile_number_label.pack()
mobile_number_entry = tk.Entry(add_frame)
mobile_number_entry.pack(pady=5)

Aadhar_Card_Number_label = tk.Label(add_frame, text="Aadhar Card:")
Aadhar_Card_Number_label.pack()
Aadhar_Card_Number_entry = tk.Entry(add_frame)
Aadhar_Card_Number_entry.pack(pady=5)

Total_Fees_label = tk.Label(add_frame, text="Total Fees:")
Total_Fees_label.pack()
Total_Fees_entry = tk.Entry(add_frame)
Total_Fees_entry.pack(pady=5)

Fees_Paid_label = tk.Label(add_frame, text="Paid Fees:")
Fees_Paid_label.pack()
Fees_Paid_entry = tk.Entry(add_frame)
Fees_Paid_entry.pack(pady=5)

add_student_button = tk.Button(add_frame, text="Add", command=add_student)
add_student_button.pack(pady=10)

back_button = tk.Button(add_frame, text="Back", command=go_to_home_page)
back_button.pack(pady=10)

# Page 3: View Students
view_frame = tk.Frame(root)

def display_students():
    cursor.execute("SELECT * FROM student_Details")
    students = cursor.fetchall()

    for student in students:
        student_label = tk.Label(view_frame, text=f"First Name: {student[0]}, Last Name: {student[1]}, Mobile Number: {student[2]}, Aadhar Card: {student[3]}, Total Fees: {student[4]}, Paid Fees: {student[5]}, Remaining Fees: {student[6]}")
        student_label.pack()

def go_to_home_page_from_view():
    view_frame.pack_forget()
    home_frame.pack()

back_button_from_view = tk.Button(view_frame, text="Back", command=go_to_home_page_from_view)
back_button_from_view.pack(pady=10)

# Page 4: Update Student
update_frame = tk.Frame(root)

def update_student():
    Aadhar_Card_Number = Aadhar_Card_Number_entry_update.get()
    first_name = first_name_entry_update.get()
    last_name = last_name_entry_update.get()
    mobile_number = mobile_number_entry_update.get()
    Total_Fees = Total_Fees_entry_update.get()
    Fees_Paid = Fees_Paid_entry_update.get()
    Remaining_Fees = float(Total_Fees) - float(Fees_Paid)

    sql = "UPDATE student_Details SET first_name = %s, last_name = %s, mobile_number = %s, Aadhar_Card_Number = %s, Total_Fees = %s, Fees_Paid = %s, Remaining_Fees = %s WHERE Aadhar_Card_Number = %s"
    values = (first_name, last_name, mobile_number, Aadhar_Card_Number, Total_Fees, Fees_Paid, Remaining_Fees,Aadhar_Card_Number)

    cursor.execute(sql, values)
    db.commit()

    Aadhar_Card_Number_entry_update.delete(0, tk.END)
    first_name_entry_update.delete(0, tk.END)
    last_name_entry_update.delete(0, tk.END)
    mobile_number_entry_update.delete(0, tk.END)
    Total_Fees_entry_update.delete(0, tk.END)
    Fees_Paid_entry_update.delete(0, tk.END)

    Aadhar_Card_Number_entry.focus()

    tk.messagebox.showinfo("Success", "Student updated successfully!")

def go_to_home_page_from_update():
    update_frame.pack_forget()
    home_frame.pack()

# student_id_label = tk.Label(update_frame, text="Student ID:")
# student_id_label.pack()
# student_id_entry = tk.Entry(update_frame)
# student_id_entry.pack(pady=5)

Aadhar_Card_Number_label_update = tk.Label(update_frame, text="Aadhar Card:")
Aadhar_Card_Number_label_update.pack()
Aadhar_Card_Number_entry_update = tk.Entry(update_frame)
Aadhar_Card_Number_entry_update.pack(pady=5)

first_name_label_update = tk.Label(update_frame, text="First Name:")
first_name_label_update.pack()
first_name_entry_update = tk.Entry(update_frame)
first_name_entry_update.pack(pady=5)

last_name_label_update = tk.Label(update_frame, text="Last Name:")
last_name_label_update.pack()
last_name_entry_update = tk.Entry(update_frame)
last_name_entry_update.pack(pady=5)

mobile_number_label_update = tk.Label(update_frame, text="Mobile Number:")
mobile_number_label_update.pack()
mobile_number_entry_update = tk.Entry(update_frame)
mobile_number_entry_update.pack(pady=5)


Total_Fees_label_update = tk.Label(update_frame, text="Total Fees:")
Total_Fees_label_update.pack()
Total_Fees_entry_update = tk.Entry(update_frame)
Total_Fees_entry_update.pack(pady=5)

Fees_Paid_label_update = tk.Label(update_frame, text="Paid Fees:")
Fees_Paid_label_update.pack()
Fees_Paid_entry_update = tk.Entry(update_frame)
Fees_Paid_entry_update.pack(pady=5)

update_student_button = tk.Button(update_frame, text="Update", command=update_student)
update_student_button.pack(pady=10)

back_button_from_update = tk.Button(update_frame, text="Back", command=go_to_home_page_from_update)
back_button_from_update.pack(pady=10)

# Page 5: Delete Student
delete_frame = tk.Frame(root)

def delete_student():
    Aadhar_Card_Number = Aadhar_Card_Number_entry_delete.get()

    sql = "DELETE FROM student_Details WHERE Aadhar_Card_Number = %s"
    value = (Aadhar_Card_Number,)

    cursor.execute(sql, value)
    db.commit()

    Aadhar_Card_Number_entry_delete.delete(0, tk.END)

    Aadhar_Card_Number_entry_delete.focus()

    tk.messagebox.showinfo("Success", "Student deleted successfully!")

def go_to_home_page_from_delete():
    delete_frame.pack_forget()
    home_frame.pack()

Aadhar_Card_Number_label_delete = tk.Label(delete_frame, text="Aadhar Card Number:")
Aadhar_Card_Number_label_delete.pack()
Aadhar_Card_Number_entry_delete = tk.Entry(delete_frame)
Aadhar_Card_Number_entry_delete.pack(pady=5)

delete_student_button = tk.Button(delete_frame, text="Delete", command=delete_student)
delete_student_button.pack(pady=10)

back_button_from_delete = tk.Button(delete_frame, text="Back", command=go_to_home_page_from_delete)
back_button_from_delete.pack(pady=10)

# Page 6: Search Student
search_frame = tk.Frame(root)

def search_student():
    Aadhar_Card_Number = Aadhar_Card_Number_entry_search.get()

    sql = "SELECT * FROM student_Details WHERE Aadhar_Card_Number = %s"
    value = (Aadhar_Card_Number,)

    cursor.execute(sql, value)
    student = cursor.fetchone()

    if student:
        student_label = tk.Label(search_frame, text=f"First Name: {student[0]}, Last Name: {student[1]}, Mobile Number: {student[2]}, Aadhar Card: {student[3]}, Total Fees: {student[4]}, Paid Fees: {student[5]}, Remaining Fees: {student[6]}")
        student_label.pack()
    else:
        tk.messagebox.showinfo("Not Found", "Student not found!")

    Aadhar_Card_Number_entry_search.delete(0, tk.END)

def go_to_home_page_from_search():
    search_frame.pack_forget()
    home_frame.pack()

Aadhar_Card_Number_label_search = tk.Label(search_frame, text="Aadhar Card Number:")
Aadhar_Card_Number_label_search.pack()
Aadhar_Card_Number_entry_search = tk.Entry(search_frame)
Aadhar_Card_Number_entry_search.pack(pady=5)

search_student_button = tk.Button(search_frame, text="Search", command=search_student)
search_student_button.pack(pady=10)

back_button_from_search = tk.Button(search_frame, text="Back", command=go_to_home_page_from_search)
back_button_from_search.pack(pady=10)

# Run the GUI
root.mainloop()
