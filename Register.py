from tkinter import *
import cx_Oracle
from tkinter import messagebox
root=Tk()
root.title("Tkinter")
root.configure(bg="light blue")
root.geometry("200x425")
def register():
    username="J-Component"
    userpwd="password"
    host="DESKTOP-EEH7CHG/XE"
    mydb=connection=cx_Oracle.connect(username,userpwd,host)
    mycursor=mydb.cursor()
    com="insert into customer values(:1,:2,:3,:4)"
    data=[(str(e_adhaar.get()),str(e_mob.get()),str(e_name.get()),str(e_email.get()))]
    mycursor.executemany(com,data)
    com="insert into login values(:1,:2)"
    data=[(str(e_user.get()),str(e_password.get()))]
    mycursor.executemany(com,data)
    mydb.commit()
    mydb.close()
    messagebox.showinfo("Registration Details","You have been successfully registered")
def login():
    root.destroy()
    import Tkinter10
name=Label(root,text="Type your Name").pack(pady=5)
e_name=Entry()
e_name.pack(pady=5)
adhaar=Label(root,text="Type your Adhaar").pack()
e_adhaar=Entry()
e_adhaar.pack(pady=5)
mob=Label(root,text="Type your Mobile Number").pack(pady=5)
e_mob=Entry()
e_mob.pack(pady=5)
email=Label(root,text="Type your E-mail Address").pack(pady=5)
e_email=Entry()
e_email.pack(pady=5)
user=Label(root,text="Type your User-id").pack(pady=5)
e_user=Entry()
e_user.pack(pady=5)
password=Label(root,text="Type Your Password").pack(pady=5)
e_password=Entry()
e_password.pack(pady=5)
button=Button(root,text="REGISTER",command=register)
button.pack(pady=5)   
button1=Button(root,text="Return to LOGIN",command=login)
button1.pack(pady=5)

