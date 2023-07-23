import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import mysql.connector


mysql_conn = mysql.connector.connect(host='localhost', user='root', password='root', database='student_management')
cur = mysql_conn.cursor()


my_w = tk.Tk()
my_w.geometry("400x300")  # Size of the window 
my_w.title('www.plus2net.com')
my_font1=('times', 18, 'bold')

l1 = tk.Label(my_w,text='Add Student Data with Photo',font=my_font1)  
l1.grid(row=1,column=1,columnspan=5)

l2 = tk.Label(my_w,  text='Name', width=10 )  # added one Label 
l2.grid(row=2,column=1)

e1 = tk.Entry(my_w,width=10,bg='yellow') # added one Entry box
e1.grid(row=2,column=2)

my_list = [1,2,3,4] # options to appear for selection
options = tk.StringVar(my_w)

options.set(my_list[1]) # default value selected
om1 =tk.OptionMenu(my_w, options, *my_list)


om1.grid(row=2,column=3) # displaying option Menu
b2 = tk.Button(my_w, text='Upload File', 
   command = lambda:upload_file())
b2.grid(row=2,column=4) 
my_font=('times', 12, 'bold')
b3 = tk.Button(my_w, text='Add data', font=my_font,
   command = lambda:add_data())
b3.grid(row=2,column=5,padx=20) 


global filename # Access this from both functions

def upload_file(): # Image upload and display
    global filename,img
    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    print(filename)
    img = ImageTk.PhotoImage(file=filename)
    b2 =tk.Button(my_w,image=img) # using Button 
    b2.grid(row=4,column=1,columnspan=2)#display uploaded photo


def add_data(): # Add data to MySQL table 
    global filename,img 
    fob=open(filename,'rb') # filename from upload_file()
    fob=fob.read()
    data=(options.get(),e1.get(),fob) # tuple with data 
    id=cur.execute("INSERT INTO  student_photo (id,student,PICTURE) VALUES (%s,%s,%s)",data)
    # print("Row Added  = ",id.rowcount) # displayed in console 
    my_w.destroy() # close window after adding data

# add_data()
upload_file()
my_w.mainloop()  # Keep the window open