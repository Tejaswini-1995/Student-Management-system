import xlwt
import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox
import mysql.connector
from datetime import date
import pandas.io.sql as sql
# from PIL import ImageTk, Image 
from xlsxwriter.workbook import Workbook

mysql_conn = mysql.connector.connect(host='localhost', user='root', password='root', database='student_management')
cur = mysql_conn.cursor()

window = tk.Tk()
window.geometry("1350x700")
# img =Image.open("image.jpg")
# bg = ImageTk.PhotoImage(img)
window.title("Eknath Patil Academy")

# # Add image
# label = tk.Label(window, image=bg)
# label.place(x=0, y=0)

Label_Heading = tk.Label(window, text="Eknath Patil Academy", font=("Times new roman", 35, "bold"), bg="blue", 
foreground="yellow", border=12, relief=tk.GROOVE)
Label_Heading.pack(side=tk.TOP, fill=tk.X)

Frame_Details =  tk.LabelFrame(window, text="Registration Form", font = ("Times new roman", 22,"bold"), bd=12, 
relief=tk.GROOVE, bg="#e3f4f1")
Frame_Details.place(x=20, y=100, width=400, height=575)

Frame_Data = tk.Frame(window, bd=12, relief=tk.GROOVE, bg="#e3f4f1")
Frame_Data.place(x=440 , y=100, width=890, height=575)



First_Name = tk.StringVar()
Last_Name = tk.StringVar()
Mobile_Number = tk.StringVar()
Aadhar_Card_Number = tk.StringVar()
Subject = tk.StringVar()
StudentAdmissionDate = date.today()
Fees_Paid = tk.IntVar()
Total_Fees  = tk.IntVar()
Remaining_Fees  = tk.IntVar()
search_box = tk.StringVar()


Label_First_Name = tk.Label(Frame_Details, text="First Name", font=("Times new roman", 17), bg="#e3f4f1")
Label_First_Name.grid(row=0, column=0, padx=2, pady=2)
Entry_First_Name = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17,textvariable=First_Name)
Entry_First_Name.grid(row=0, column=1, padx=2, pady=2)

Label_Last_Name = tk.Label(Frame_Details, text="Last Name", font=("Times new roman", 17), bg="#e3f4f1")
Label_Last_Name.grid(row=1, column=0, padx=2, pady=2)
Entry_Last_Name = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17,textvariable=Last_Name)
Entry_Last_Name.grid(row=1, column=1, padx=2, pady=2)

Label_Mobile_Number = tk.Label(Frame_Details, text="Mobile Number", font=("Times new roman", 17), bg="#e3f4f1")
Label_Mobile_Number.grid(row=2, column=0, padx=2, pady=2)
Entry_Mobile_Number = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17,textvariable=Mobile_Number)
Entry_Mobile_Number.grid(row=2, column=1, padx=2, pady=2)

Label_Aadhar_Card_Number = tk.Label(Frame_Details, text="Aadhar Card Number", font=("Times new roman", 17), bg="#e3f4f1")
Label_Aadhar_Card_Number.grid(row=3, column=0, padx=2, pady=2)
Entry_Aadhar_Card_Number = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17,textvariable=Aadhar_Card_Number)
Entry_Aadhar_Card_Number.grid(row=3, column=1, padx=2, pady=2)

Label_Subject = tk.Label(Frame_Details, text="Subject", font=("Times new roman", 17), bg="#e3f4f1")
Label_Subject.grid(row=4, column=0, padx=2, pady=2)
Entry_Subject = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17,textvariable=Subject)
Entry_Subject.grid(row=4, column=1, padx=2, pady=2)

Label_StudentAdmissionDate = tk.Label(Frame_Details, text=f"StudentAdmissionDate", font=("Times new roman", 17), bg="#e3f4f1")
Label_StudentAdmissionDate.grid(row=5, column=0, padx=2, pady=2)
Entry_StudentAdmissionDate = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17,textvariable=StudentAdmissionDate)
Entry_StudentAdmissionDate  .grid(row=5, column=1, padx=2, pady=2)

Label_Fees_Paid = tk.Label(Frame_Details, text="Fees Paid", font=("Times new roman", 17), bg="#e3f4f1")
Label_Fees_Paid.grid(row=6, column=0, padx=2, pady=2)
Entry_Fees_Paid = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17,textvariable=Fees_Paid)
Entry_Fees_Paid  .grid(row=6, column=1, padx=2, pady=2)

# Database Frame
Frame_Database = tk.Frame(Frame_Data, bg="#e3f4f1", bd=11, relief=tk.GROOVE)
Frame_Database.pack(fill=tk.BOTH, expand=True)

Scroll_X = tk.Scrollbar(Frame_Database, orient=tk.HORIZONTAL)
Scroll_Y = tk.Scrollbar(Frame_Database, orient=tk.VERTICAL)


student = ttk.Treeview(Frame_Database, columns=("First_Name","Last_Name","Mobile_Number",
"Aadhar_Card_Number","Subject","StudentAdmissionDate","Fees_Paid","Remaining_Fees"), yscrollcommand= Scroll_Y.set,xscrollcommand= Scroll_X.set)

def get_data():
    mysql_conn = mysql.connector.connect(host='localhost', user='root', password='root', database='student_management')
    cur = mysql_conn.cursor()
    cur.execute("SELECT s1.First_Name, s1.Last_Name, s1.Mobile_Number, s1.Aadhar_Card_Number,s1.Subject, s1.StudentAdmissionDate, s1.Fees_Paid, concat(s2.Total_Fees-s2.Fees_Paid) AS Remaining_Fees FROM student_Details AS s1 , student_Details AS s2 WHERE s1.Aadhar_Card_Number = s2.Aadhar_Card_Number;")
    rows = cur.fetchall()
    if len(rows) != 0:
        student.delete(*student.get_children())
        for row in rows:
            student.insert('',tk.END, values=row)
    mysql_conn.commit()
    mysql_conn.close()




def add_student():
    if Aadhar_Card_Number.get()=="":
        messagebox.showerror('Error','All Fields required!')
    else:
        sql = "INSERT INTO student_Details (First_Name,Last_Name,Mobile_Number,Aadhar_Card_Number,Subject,StudentAdmissionDate, Fees_Paid) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = [First_Name.get(),Last_Name.get(),Mobile_Number.get(),Aadhar_Card_Number.get(),Subject.get(),StudentAdmissionDate,Fees_Paid.get()]
        mysql_conn = mysql.connector.connect(host='localhost', user='root', password='root', database='student_management')
        cur = mysql_conn.cursor()
        cur.execute(sql, val)   
        mysql_conn.commit()
        mysql_conn.close()
        get_data()
        clear()
        messagebox.showinfo("Record has been saved successfully")


def add_data_excel():

    mysql_conn = mysql.connector.connect(host='localhost', user='root', password='root', database='student_management')
    cur = mysql_conn.cursor()
    cur.execute("SELECT s1.First_Name, s1.Last_Name, s1.Mobile_Number, s1.Aadhar_Card_Number,s1.Subject, s1.StudentAdmissionDate, s1.Fees_Paid, concat(s2.Total_Fees-s2.Fees_Paid) AS Remaining_Fees FROM student_Details AS s1 , student_Details AS s2 WHERE s1.Aadhar_Card_Number = s2.Aadhar_Card_Number;")
    rows = cur.fetchall()
    # #output in bytes
    # output = io.BytesIO()
    workbook = xlwt.Workbook()
    sh = workbook.add_sheet('Student Report')

    sh.write(0, 0, 'First Name')
    sh.write(0, 1, 'Last Name')
    sh.write(0, 2, 'Mobile Number')
    sh.write(0, 3, 'Aadhar Card Number')
    sh.write(0, 4, 'Subject')
    sh.write(0, 5, 'Admission Date')
    sh.write(0, 6, 'Paid Fees')
    sh.write(0, 7, 'Remaining Fees')

    idx = 0
    for row in rows:
        print(row[5])
        sh.write(idx+1, 0, str(row[0]))
        sh.write(idx+1, 1, row[1])
        sh.write(idx+1, 2, row[2])
        sh.write(idx+1, 3, row[3])
        sh.write(idx+1, 4, row[4])
        sh.write(idx+1, 5, row[5])
        sh.write(idx+1, 6, row[6])
        sh.write(idx+1, 7, row[7])
        idx += 1

    workbook.save(f"student_report_{date.today()}.xls")
    # output.seek(0)
    # return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename=student_report.xls"})

    cur.close() 
    mysql_conn.close()

def UPDATE_DATA():
    mysql_conn = mysql.connector.connect(host='localhost', user='root', password='root', database='student_management')
    cur = mysql_conn.cursor()
    sql = ("Update student_Details set First_Name=%s,Last_Name=%s,Mobile_Number=%s,Aadhar_Card_Number=%s,Subject=%s,StudentAdmissionDate=%s,Fees_Paid=%s where Mobile_Number=%s", First_Name.get(),Last_Name.get(),Mobile_Number.get(),Aadhar_Card_Number.get(),
    Subject.get(),StudentAdmissionDate,Fees_Paid.get())
    print(sql)
    cur.execute(sql)
    mysql_conn.commit()
    mysql_conn.close()
    get_data()
    clear()


def DELETE():
    con=mysql.connector.connect(host='localhost', user='root', password='root', database='student_management')
    cur=con.cursor()
    sql = ('DELETE FROM student_Details where Aadhar_Card_Number=%s')
    val = [Aadhar_Card_Number.get()]
    cur.execute(sql, val)   
    con.commit()
    con.close()
    get_data()
    clear()
    messagebox.showinfo('Success','Record has been deleted')

def clear():
    First_Name.set("")
    Last_Name.set("")
    Mobile_Number.set("")
    Aadhar_Card_Number.set("")
    Subject.set("")
    Fees_Paid.set("")
    Total_Fees.set("")
    Remaining_Fees.set("")

Frame_Btn = tk.Frame(Frame_Details, bg="#e3f4f1", bd=7, relief=tk.GROOVE)
Frame_Btn.place(x=15, y=390, width=348, height=120)

Add_Button = tk.Button(Frame_Btn, bg="#e3f4f1", text="Add", bd=7, font=("Times new roman", 15), width=13, command=add_student)
Add_Button.grid(row=0, column=0, padx=2, pady=2)

Delete_Button = tk.Button(Frame_Btn, bg="#e3f4f1", text="Delete", bd=7, font=("Times new roman", 15), width=13, command=DELETE)
Delete_Button.grid(row=0, column=1, padx=2, pady=2)

Update_Button = tk.Button(Frame_Btn, bg="#e3f4f1", text="Update", bd=7, font=("Times new roman", 15), width=13, command=UPDATE_DATA)
Update_Button.grid(row=1, column=0, padx=2, pady=2)

Add_Excel = tk.Button(Frame_Btn, bg="#e3f4f1", text="Export", bd=7, font=("Times new roman", 15), width=13, command=add_data_excel)
Add_Excel.grid(row=1, column=1, padx=2, pady=2)


Frame_Search = tk.Frame(Frame_Data, bg="#e3f4f1" , bd=10, relief=tk.GROOVE)
Frame_Search.pack(side=tk.TOP, fill=tk.X)

Label_Search = tk.Label(Frame_Search, text="Search", bg="#e3f4f1", font=("Times new roman", 16))
Label_Search.grid(row=0, column=0, padx=12, pady=2)

Search_Box = ttk.Combobox(Frame_Search, font=("Times new roman", 16), state="readonly", textvariable=search_box)
Search_Box['values'] = ("Aadhar_Card_Number")
Search_Box.grid(row=0, column=1, padx=12, pady=2)

Search_Button = tk.Button(Frame_Search, bg="#e3f4f1", text="Search", bd=7, font=("Times new roman", 15), width=14)
Search_Button.grid(row=0, column=2, padx=12, pady=2)


Scroll_X.config(command=student.xview)
Scroll_X.pack(side=tk.BOTTOM, fill=tk.X)
Scroll_Y.config(command=student.yview)
Scroll_Y.pack(side=tk.RIGHT, fill=tk.Y)


student.heading("First_Name", text="First Name")
student.heading("Last_Name", text="Last Name")
student.heading("Mobile_Number", text="Mobile Number")
student.heading("Aadhar_Card_Number", text="Aadhar Card Number")
student.heading("Subject", text="Subject")
student.heading("StudentAdmissionDate", text="StudentAdmissionDate")
student.heading("Fees_Paid", text="Fees Paid")
student.heading("Remaining_Fees", text="Remaining Fees")

 
student['show']='headings'
student.column("First_Name", width= 100)
student.column("Last_Name", width= 100)
student.column("Mobile_Number", width= 100)
student.column("Aadhar_Card_Number", width= 100)
student.column("Subject", width= 100)
student.column("StudentAdmissionDate", width= 100)
student.column("Fees_Paid", width= 100)
student.column("Remaining_Fees", width= 100)
 
student.pack(fill=tk.BOTH, expand=True)

student.tag_configure("Total_Fees", background='green')
student.tag_configure("Remaining_Fees", background='red')
def hightlight_record():
    my_tag = 'normal'
    cur.execute("SELECT s1.First_Name, s1.Last_Name, s1.Mobile_Number, s1.Aadhar_Card_Number,s1.Subject, s1.StudentAdmissionDate, s1.Fees_Paid, concat(s2.Total_Fees-s2.Fees_Paid) AS Remaining_Fees FROM student_Details AS s1 , student_Details AS s2 WHERE s1.Aadhar_Card_Number = s2.Aadhar_Card_Number;")
# print(r_set)
    rows = cur.fetchall()
    if len(rows) != 0:
        for dt in rows:
            my_tag = "Remaining_Fees" if dt[6] < 8000 else 'Total_Fees'
            student.insert("",'end',text=dt[0],values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7]),tags=(my_tag)) 

Show_Button = tk.Button(Frame_Search, bg="#e3f4f1", text="Show", bd=7, font=("Times new roman", 15), width=14, command=hightlight_record)
Show_Button.grid(row=0, column=3, padx=12, pady=2)

window.mainloop() 