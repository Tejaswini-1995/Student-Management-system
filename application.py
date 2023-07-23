from flask import Flask, render_template, request, redirect, url_for, session
# from database import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'student_management'


mysql = MySQL(app)

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select * from Student where username=%s AND paasword =%s', (username, password))
        student = cursor.fetchone()
        if student:
            session['loggedin'] = True
            session['id'] = student['id']
            session['username'] = student['username']
            msg = 'Loggen in Successfully'
            return render_template('index.html', msg=msg)
        else:
            msg = "Incorrect username / password!" 
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method =="POST" and 'username' in request.form and 'password' in request.form and 'email_id' in request.form:
        id = request.form['id']
        First_Name = request.form['First_Name']
        Last_Name = request.form['Last_Name']
        Mobile_Number = request.form['Mobile_Number']
        Aadhar_Card = request.form['Aadhar_Card']
        DOB = request.form['DOB']
        email_Id = request.form['email_Id']
        Gender = request.form['Gender']
        Address = request.form['Address']
        city = request.form['city']
        pincode = request.form['pincode']
        state = request.form['state']
        country = request.form['country']
        Qualification = request.form['Qualification']
        Course_Applied = request.form['Course_Applied']
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        student = student.fetchone()
        if student:
            msg = 'Student is already registered'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = "Please enter correct mail Id"
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = "Username contain only characters and numbers"
        else:
            cursor.execute('INSERT INTO accounts VALUES \
            (NULL, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, NULL, % s)',
                           (id,First_Name,Last_Name,Mobile_Number,Aadhar_Card,DOB,
                           email_Id,Gender,Address,city,pincode,state,country,Qualification,
                           Course_Applied,Username,paasword, ))
            mysql.connection.commit()
            msg = 'You have registered successfully!!'
    elif request.method == "POST":
        msg = "Please fill required details!"
    return render_template('register.html', msg=msg)



@app.route("/index")
def index():
    if 'loggedin' in session:
        return render_template('index.html')
    return redirect(url_for('login'))    

                                                                                     


if __name__ == "__main__":
    app.run(host="localhost", port=int("3000"))
