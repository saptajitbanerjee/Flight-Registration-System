from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import os
import requests
from io import BytesIO
from tkinter import messagebox
import cx_Oracle
root=Tk()
root.title("Tkinter")
root.configure(bg="light blue")
#frame=LabelFrame(root,text="")
style=ttk.Style()
img_url = "https://i.pinimg.com/564x/f5/cb/08/f5cb08e4739a1cf0bfe0c358037b860b.jpg"
root.geometry("600x475")
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
panel = Label(root, image=img)
panel.pack()
login=Label(root,text="Username",bg="white")
login.pack(pady=5)
e_login=Entry(root,bg="light gray")
e_login.pack(pady=5)
password=Label(root,text="Password",bg="white")
password.pack(pady=5)
e_password=Entry(root,bg="light grey")
e_password.pack(pady=5)
def insert():
    global x
    global y
    x=0
    y=0
    a=str(e_login.get())
    b=str(e_password.get())
    username="J-Component"
    userpwd="password"
    host="DESKTOP-EEH7CHG/XE"
    mydb=connection=cx_Oracle.connect(username,userpwd,host)
    mycursor=mydb.cursor()
    mycursor.execute("select * from login")
    row=mycursor.fetchall()
    for i in range (len(row)):
        if a==row[i][0]:
            x=1
            if b==row[i][1]:
                root.destroy()
                import Tkinter12
            #else:
             #   x=1
        #else:
         #   y=1
    if x!=1:
        messagebox.showinfo("Error","Invalid Username or Password ")
    mydb.close()
def register():
    root.destroy()
    import Register
insert=Button(root,text="LOGIN",command=insert).pack(pady=5)
register=Button(root,text="REGISTER HERE",command=register).pack(pady=5)

