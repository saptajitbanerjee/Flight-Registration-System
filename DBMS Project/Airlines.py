from tkinter import *
from tkinter import ttk
import cx_Oracle
from tkinter import messagebox
root=Tk()
root.title("Airlines Management")
tree=ttk.Treeview(root)
root.geometry("1310x600")
root.configure(bg="light blue")
style=ttk.Style()
style.theme_use("clam")
frame=Frame(root)
l1=Label(root,text="Table for Airlines:",fg='white',bg='blue').place(x=10,y=5)
frame.place(x=10,y=30)
scroll=Scrollbar(frame)
scroll.pack(side="right",fill='y')
tree=ttk.Treeview(frame,yscrollcommand=scroll.set)
scroll.config(command=tree.yview)
style.map('Treeview',background=[('selected','blue')])
tree['columns']=('id','name','city','country','type')
tree.column("#0",anchor=W,width=120,minwidth=25)
tree.column("id",anchor=W,width=120,minwidth=25)
tree.column("name",anchor=W,width=120,minwidth=25)
tree.column("city",anchor=W,width=150,minwidth=25)
tree.column("country",anchor=W,width=120,minwidth=25)
tree.column("type",anchor=W,width=120,minwidth=25)
tree.heading("#0",text="Sno.",anchor=W)
tree.heading("id",text="ID",anchor=W)
tree.heading("name",text="Name of Airlines",anchor=W)
tree.heading("city",text="City",anchor=W)
tree.heading("country",text="Country",anchor=W)
tree.heading("type",text="Type of Airlines",anchor=W)
tree.pack(pady=20)
userpwd='password'
mydb=connection=cx_Oracle.connect("J-Component",userpwd,"DESKTOP-EEH7CHG/XE")
mycursor=mydb.cursor()
mycursor.execute("select * from airlines")
row=mycursor.fetchall()
count1=0
tree.tag_configure('oddrow',background='grey89')#grey89#steelblue#steelblue2
tree.tag_configure('evenrow',background='lightblue')
for record in row:
    if count1%2==0:
        tree.insert(parent="",index='end',iid=count1,text=count1+1,values=(record[0],record[1],record[2],record[3],record[4]),tags=('evenrow'))
    elif count1%2!=0:
        tree.insert(parent="",index='end',iid=count1,text=count1+1,values=(record[0],record[1],record[2],record[3],record[4]),tags=('oddrow'))
    count1+=1
mydb.commit()
mydb.close()
frame1=Frame(root)
frame1.place(x=800,y=330)
l3=Label(root,text='Table for Airports:',fg='white',bg='blue').place(x=800,y=305)
scroll=Scrollbar(frame1)
scroll.pack(side="right",fill='y')
tree1=ttk.Treeview(frame1,yscrollcommand=scroll.set)
scroll.config(command=tree1.yview)
style.map('Treeview',background=[('selected','blue')])
tree1['columns']=('id','name','city')
tree1.column("#0",anchor=W,width=120,minwidth=25)
tree1.column("id",anchor=W,width=120,minwidth=25)
tree1.column("name",anchor=W,width=120,minwidth=25)
tree1.column("city",anchor=W,width=120,minwidth=25)
tree1.heading("#0",text="Sno.",anchor=W)
tree1.heading("id",text="ID",anchor=W)
tree1.heading("name",text="Name of Airport",anchor=W)
tree1.heading("city",text="City",anchor=W)
tree1.pack(pady=20)
userpwd='password'
mydb=connection=cx_Oracle.connect("J-Component",userpwd,"DESKTOP-EEH7CHG/XE")
mycursor=mydb.cursor()
mycursor.execute("select * from airport")
row=mycursor.fetchall()
count1=0
tree1.tag_configure('oddrow',background='grey89')#grey89#steelblue#steelblue2
tree1.tag_configure('evenrow',background='lightblue')
for record in row:
    if count1%2==0:
        tree1.insert(parent="",index='end',iid=count1,text=count1+1,values=(record[0],record[1],record[2]),tags=('evenrow'))
    elif count1%2!=0:
        tree1.insert(parent="",index='end',iid=count1,text=count1+1,values=(record[0],record[1],record[2]),tags=('oddrow'))
    count1+=1
mydb.commit()
mydb.close()
frame2=Frame(root)
frame2.place(x=10,y=330)
l4=Label(root,text='Table for Employees in Airport:',fg='white',bg='blue').place(x=10,y=305)
scroll=Scrollbar(frame2)
scroll.pack(side="right",fill='y')
tree2=ttk.Treeview(frame2,yscrollcommand=scroll.set)
scroll.config(command=tree2.yview)
style.map('Treeview',background=[('selected','blue')])
tree2['columns']=('id','name','age','job','salary')
tree2.column("#0",anchor=W,width=120,minwidth=25)
tree2.column("id",anchor=W,width=120,minwidth=25)
tree2.column("name",anchor=W,width=120,minwidth=25)
tree2.column("age",anchor=W,width=120,minwidth=25)
tree2.column("job",anchor=W,width=150,minwidth=25)
tree2.column("salary",anchor=W,width=120,minwidth=25)
tree2.heading("#0",text="Sno.",anchor=W)
tree2.heading("id",text="Employee-ID",anchor=W)
tree2.heading("name",text="Name of Employee",anchor=W)
tree2.heading("age",text="Age",anchor=W)
tree2.heading("job",text="Job",anchor=W)
tree2.heading("salary",text="Salary",anchor=W)
tree2.pack(pady=20)
userpwd='password'
mydb=connection=cx_Oracle.connect("J-Component",userpwd,"DESKTOP-EEH7CHG/XE")
mycursor=mydb.cursor()
mycursor.execute("select * from employees")
row=mycursor.fetchall()
count2=0
tree2.tag_configure('oddrow',background='grey89')#grey89#steelblue#steelblue2
tree2.tag_configure('evenrow',background='lightblue')
for record in row:
    if count2%2==0:
        tree2.insert(parent="",index='end',iid=count2,text=count2+1,values=(record[0],record[1],record[2],record[3],record[4]),tags=('evenrow'))
    elif count2%2!=0:
        tree2.insert(parent="",index='end',iid=count2,text=count2+1,values=(record[0],record[1],record[2],record[3],record[4]),tags=('oddrow'))
    count2+=1
mydb.commit()
mydb.close()
frame3=Frame(root)
l2=Label(root,text='Table for Flights:',bg='blue',fg='white').place(x=800,y=5)
frame3.place(x=800,y=30)#920,320
scroll=Scrollbar(frame3)
scroll.pack(side="right",fill='y')
tree3=ttk.Treeview(frame3,yscrollcommand=scroll.set)
scroll.config(command=tree3.yview)
style.map('Treeview',background=[('selected','blue')])
tree3['columns']=('f','l','n')
tree3.column("#0",anchor=W,width=120,minwidth=25)
tree3.column("f",anchor=W,width=120,minwidth=25)
tree3.column("l",anchor=W,width=120,minwidth=25)
tree3.column("n",anchor=W,width=120,minwidth=25)
tree3.heading("#0",text="Sno.",anchor=W)
tree3.heading("f",text="Flight Number",anchor=W)
tree3.heading("l",text="Luggage Limit",anchor=W)
tree3.heading("n",text="No. of Seats",anchor=W)
tree3.pack(pady=20)
userpwd='password'
mydb=connection=cx_Oracle.connect("J-Component",userpwd,"DESKTOP-EEH7CHG/XE")
mycursor=mydb.cursor()
mycursor.execute("select * from flights")
row=mycursor.fetchall()
count3=0
tree3.tag_configure('oddrow',background='grey89')#grey89#steelblue#steelblue2
tree3.tag_configure('evenrow',background='lightblue')
for record in row:
    if count3%2==0:
        tree3.insert(parent="",index='end',iid=count3,text=count3+1,values=(record[0],record[1],record[2]),tags=('evenrow'))
    elif count3%2!=0:
        tree3.insert(parent="",index='end',iid=count3,text=count3+1,values=(record[0],record[1],record[2]),tags=('oddrow'))
    count3+=1
mydb.commit()
mydb.close()
