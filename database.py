import mysql.connector
# from model import *


def Mysql_connection():
    cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database="student_management")
    cur = cnx.cursor()

    # cur.execute("Create table Student (id INT,First_Name VARCHAR(255), Last_Name VARCHAR(255), Mobile_Number INT, Aadhar_Card INT PRIMARY KEY,DOB VARCHAR(15),email_Id VARCHAR(100),Gender VARCHAR(10),Address VARCHAR(255),city VARCHAR(20),pincode INT,state VARCHAR(100),country VARCHAR(100),Qualification VARCHAR(25),Course_Applied VARCHAR(100))")

    query = "select * from student"
    cur.execute(query)
    result = cur.fetchone()
    for i in result:
        print(i)
    cnx.close()

Mysql_connection()

