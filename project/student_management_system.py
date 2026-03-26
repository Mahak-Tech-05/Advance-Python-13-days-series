import mysql.connector

#creating a connection
con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    port = "3306",
    )

#checking connection with server
if con.is_connected():
    print("Server Connected Succesfully!")

else:
    print("An error occur in the server connection")


cursor = con.cursor()

#creating database
cursor.execute("create database if not exists student")
con.commit()
print("Database Crested Succesfully plz procedd for further process........")

#creating table in database
cursor.execute("use student")
cursor.execute("create table if not exists student_details(ID int auto_increment primary key, Name varchar(100),Age int,branch varchar(50),year int,semester int)")
con.commit()
print("Table also created succesfully into database plz now process into main menu.......!")

#creating a function of adding a student
def add_student():
    name= input("Enter you're name :")
    age = int(input("Enter you're age:"))
    branch = input("Enter you're branch:")
    year = int(input("Enter you're current college year:"))
    semester = int(input("Enter You're current semester:"))
    query=("insert into student_details(Name,Age,branch,year,semester)values(%s,%s,%s,%s,%s)")
    values=(name,age,branch,year,semester)
    cursor.execute(query,values)
    con.commit()
    print("Student Data Inserted succesfully!")

# creating for showing all students record
def view_student():
    cursor.execute("select * from student_details")
    records = cursor.fetchall()
    print("--- Student Records-----")
    for row in records:
        print(row)

#creating a function for deletion of a record for database of particualar id
def delete_student():
    id = int(input("Enter id to delete"))
    query = ("delete from student_details where ID = %s")
    values = (id,)
    cursor.execute(query,values)
    con.commit()
    print("Given id delete succesfully !")

#creating a function for updating a data of a practicular id
def update_student():
    id = int(input("Enter id to update"))
    print("Select what do you want to update in it:")
    print("1:Name \n 2:Age \n 3:Branch \n 4:Year \n 5:Semester \n 6:Exit")
    up = input("Enter you're option here:!")
    if up == '1':
        new_name=input("Enter new name to update:")
        query = "update student_details set Name = %s where ID = %s"
        values=(new_name, id)
        cursor.execute(query,values)
        con.commit()
        print("Name update succesully!")

    elif up == '2':
        new_age=int(input("Enter new age to update:"))
        query = "update student_details set Age = %s where ID = %s"
        values=(new_age, id)
        cursor.execute(query,values)
        con.commit()
        print("Age update succesully!")

    elif up == '3':
        new_branch=input("Enter new branch to update:")
        query = "update student_details set branch = %s where ID = %s"
        values=(new_branch, id)
        cursor.execute(query,values)
        con.commit()
        print("Branch update succesully!")

    elif up == '4':
        new_year=int(input("Enter new year to update:"))
        query = "update student_details set year = %s where ID = %s"
        values=(new_year, id)
        cursor.execute(query,values)
        con.commit()
        print("Year update succesully!")

    elif up == '5':
        new_sem=int(input("Enter new sem to update:"))
        query = "update student_details set semester = %s where ID = %s"
        values=(new_sem, id)
        cursor.execute(query,values)
        con.commit()
        print("Year update succesully!")


    elif up == '6':
        print("----Exiting the programme -----!")
        return

    else:
        print("❌ Invalid Choice!")


#Main code from where all operation will been choosen by user and that operation will performed
while True:
    print("-------Main Mneu--------")
    print("1:Add Student \n 2:Update Student Detail \n 3:Read Records of all students \n 4:Delete Student \n5:Exit")
    c = input("Enter you're choice here plz:")

    #here we use elif for selection process!
    if c == '1':
        add_student()

    elif c == '2':
        update_student()

    elif c == '3':
        view_student()

    elif c == '4':
        delete_student()

    elif c == '5':
        print("Exiting the programe!")
        break

    else:
        print("Invalid choice")

