#This is the programme of inserting student data in database using tkinter and crud
import tkinter as tk
from tkinter import messagebox
import mysql.connector

#------- Database server connection------
conn = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "1234",
    port = "3306"
    )

cursor = conn.cursor()

if conn.is_connected():
    print("Server Connection is succesfull")


#--------creating database------
cursor.execute("create database if not exists tk")
conn.commit()
print("Data Base created successfully")

#--------creating table-----------
cursor.execute("use tk")
cursor.execute("create table if not exists student(ID int auto_increment primary key , Name varchar(100),age int,course varchar(100))")
conn.commit()
print("Table Created succesfully")

#-----creating insert function----------
def insert_data():
    name = n.get()
    age = a.get()
    course = c.get()

    #-----validating here that user was not left empty field----
    if name=="" or age =="" or course == "":
        messagebox.showerror("Error","All fields are required to field")
        return

    query = "insert into student(name , age,course) values(%s,%s,%s)"
    values = (name , age,course)

    cursor.execute(query,values)
    conn.commit()

    messagebox.showinfo("Success","Data Inserted Successfull")

    n.set("")
    a.set("")
    c.set("")#again empty the field

#----- Main Code---
#----Main GUI CODE -----
root = tk.Tk()
root.title("Student Rgistation Window")
root.geometry("400x300")

n = tk.StringVar()
a = tk.StringVar()
c = tk.StringVar()

tk.Label(root , text = 'Name').pack(pady=5)#verticall top down pady->vertical padx->horizontal
tk.Entry(root , textvariable=n).pack()

tk.Label(root , text = 'Age').pack(pady=5)
tk.Entry(root , textvariable=a).pack()

tk.Label(root , text = 'Course').pack(pady=5)
tk.Entry(root , textvariable=c).pack()

tk.Button(root , text = 'Add Data', command= insert_data).pack(pady = 20)

root.mainloop()
