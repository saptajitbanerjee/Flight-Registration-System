from tkinter import *
from tkinter import ttk
import cx_Oracle
from tkinter import messagebox
root=Tk()
root.title("Administration")
tree=ttk.Treeview(root)
root.geometry("1270x400")
root.configure(bg="light blue")
l1=Label(root,text="Table of Tickets Booked by Customers:",bg='blue',fg='white')
l1.place(x=10,y=5)
l2=Label(root,text="Table of Tickets Cancelled by Customers:",bg='blue',fg='white')
l2.place(x=1000,y=5)
style=ttk.Style()
style.theme_use("clam")
frame=Frame(root)
frame.place(x=10,y=30)
scroll=Scrollbar(frame)
scroll.pack(side="right",fill='y')
tree=ttk.Treeview(frame,yscrollcommand=scroll.set)
scroll.config(command=tree.yview)
style.map('Treeview',background=[('selected','blue')])
tree['columns']=("price","source","destination","company","passenger","t_id","s_no")
tree.column("#0",anchor=W,width=120,minwidth=25)
tree.column("price",anchor=W,width=120,minwidth=25)
tree.column("source",anchor=W,width=120,minwidth=25)
tree.column("destination",anchor=W,width=120,minwidth=25)
tree.column("company",anchor=W,width=120,minwidth=25)
tree.column("passenger",anchor=W,width=120,minwidth=25)
tree.column("t_id",anchor=W,width=120,minwidth=25)
tree.column("s_no",anchor=W,width=120,minwidth=25)
tree.heading("#0",text="Sno.",anchor=W)
tree.heading("price",text="Price",anchor=CENTER)
tree.heading("source",text="Source",anchor=W)
tree.heading("destination",text="Destination",anchor=W)
tree.heading("company",text="Airlines",anchor=W)
tree.heading("passenger",text="Name of Passenger",anchor=W)
tree.heading("t_id",text="Ticket-id",anchor=W)
tree.heading("s_no",text="Seat Number",anchor=W)
tree.pack(pady=20)
userpwd="password"
mydb=connection=cx_Oracle.connect("J-Component",userpwd,"DESKTOP-EEH7CHG/XE")
mycursor=mydb.cursor()
mycursor.execute("select * from tickets")
row=mycursor.fetchall()
count1=0
tree.tag_configure('oddrow',background='grey89')#grey89#steelblue#steelblue2
tree.tag_configure('evenrow',background='lightblue')
for record in row:
    if count1%2==0:
        tree.insert(parent="",index='end',iid=count1,text=count1+1,values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]),tags=('evenrow'))
    elif count1%2!=0:
        tree.insert(parent="",index='end',iid=count1,text=count1+1,values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]),tags=('oddrow'))
    count1+=1
mydb.commit()
mydb.close()
frame1=Frame(root)
frame1.place(x=1000,y=30)
scroll=Scrollbar(frame1)
scroll.pack(side="right",fill='y')
tree1=ttk.Treeview(frame1,yscrollcommand=scroll.set)
scroll.config(command=tree1.yview)
style.map('Treeview',background=[('selected','blue')])
tree1['columns']=("t_id")
tree1.column("#0",anchor=W,width=120,minwidth=25)
tree1.column("t_id",anchor=W,width=120,minwidth=25)
tree1.heading("#0",text="Sno.",anchor=W)
tree1.heading("t_id",text="Ticket-id",anchor=W)
tree1.pack(pady=20)
userpwd="password"
mydb=connection=cx_Oracle.connect("J-Component",userpwd,"DESKTOP-EEH7CHG/XE")
mycursor=mydb.cursor()
mycursor.execute("select * from tickets_cancelled")
row1=mycursor.fetchall()
count=0
tree1.tag_configure('oddrow',background='grey89')#grey89#steelblue#steelblue2
tree1.tag_configure('evenrow',background='lightblue')
for record in row1:
    if count%2==0:
        tree1.insert(parent="",index='end',iid=count,text=count+1,values=(record[0]),tags=('oddrow'))
    elif count%2!=0:
        tree1.insert(parent="",index='end',iid=count,text=count+1,values=(record[0]),tags=('evenrow'))
    count+=1
mydb.commit()
mydb.close()
def add():
    if e_a1.get()!='' and e_a2.get()!='' and e_a3.get()!='' and e_a4.get()!='' and e_a5.get()!='' and e_a6.get()!='' and e_a7.get()!='':
        global count1
        tree.insert(parent="",index='end',iid=count1,text=count1+1,values=(e_a1.get(),e_a2.get(),e_a3.get(),e_a4.get(),e_a5.get(),e_a6.get(),e_a7.get()))
        count1+=1
        userpwd="password"
        mydb=connection=cx_Oracle.connect("J-Component",userpwd,"DESKTOP-EEH7CHG/XE")
        mycursor=mydb.cursor()
        com="insert into tickets values(:1,:2,:3,:4,:5,:6,:7)"
        data1=[(int(e_a1.get()),str(e_a2.get()),str(e_a3.get()),str(e_a4.get()),str(e_a5.get()),str(e_a6.get()),int(e_a7.get()))]
        mycursor.executemany(com,data1)
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Row Addition","Data has been successfully inserted")
    if e_a1.get()=='' or e_a2.get()=='' or e_a3.get()=='' or e_a4.get()=='' or e_a5.get()=='' or e_a6.get()=='' or e_a7.get()=='':
        messagebox.showinfo("Error","Please fill all fields for addition of data")
def add1():
    if e_b.get()!='':
        global count
        tree1.insert(parent='',index='end',iid=count,text=count+1,values=(e_b.get()))
        count+=1
        userpwd="password"
        mydb=connection=cx_Oracle.connect("J-Component",userpwd,"DESKTOP-EEH7CHG/XE")
        mycursor=mydb.cursor()
        com="insert into tickets_cancelled values(:1)"
        data3=[str(e_b.get())]
        mycursor.execute(com,data3)
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Row Addition","Data has been successfully inserted")
    if e_b.get()=='':
        messagebox.showinfo("Error","Please fill all fields for addition on data")
def delete1():
    if e_b.get()!='' and e_c.get()!='':
        global a
        a=e_c.get()
        y=int(a)-1
        tree1.delete(str(y))
        userpwd="password"
        mydb=connection=cx_Oracle.connect("J-Component",userpwd,"DESKTOP-EEH7CHG/XE")
        mycursor=mydb.cursor()
        com="delete from tickets_cancelled where ticket_id=:1"
        data2=[(str(e_b.get()))]
        mycursor.execute(com,data2)
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Deletion Details","Data has been successfully deleted")
    if e_b.get()=='' and e_c.get()=='':
        messagebox.showinfo("Errot","Please enter all fields for deletion of data")
def delete():
    if e_d1.get()!='' and e_d2.get()!='':
        global x
        x=e_d1.get()
        y=int(x)-1
        tree.delete(str(y))
        userpwd="password"
        mydb=connection=cx_Oracle.connect("J-Component",userpwd,"DESKTOP-EEH7CHG/XE")
        mycursor=mydb.cursor()
        com="delete from food_available where p_id=:1"
        data2=[(str(e_d2.get()))]
        mycursor.execute(com,data2)
        com="delete from passengers where p_id=:1"
        data2=[(str(e_d2.get()))]
        mycursor.execute(com,data2)
        com="delete from payment where ticket_id=:1"
        data2=[(str(e_d2.get()))]
        mycursor.execute(com,data2)
        com="delete from tickets where ticket_id=:1"
        data2=[(str(e_d2.get()))]
        mycursor.execute(com,data2)
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Deletion Details","Data has been successfully deleted")
    if e_d1.get()=='' or e_d2.get()=='':
        messagebox.showinfo('Error','Please fill all fields for deletion of data')
l3=Label(root,text="Price   Source   Destination   Company    Name    Ticket-id   Seat Number").place(x=10,y=310)
e_a1=Entry(width=4)
e_a1.place(x=10,y=335)
e_a2=Entry(width=7)
e_a2.place(x=45,y=335)
e_a3=Entry(width=7)
e_a3.place(x=95,y=335)
e_a4=Entry(width=8)
e_a4.place(x=155,y=335)
e_a5=Entry(width=8)
e_a5.place(x=215,y=335)
e_a6=Entry(width=6)
e_a6.place(x=275,y=335)
e_a7=Entry(width=2)
e_a7.place(x=320,y=335)
button=Button(root,text="ADD",command=add).place(x=10,y=365)
l4=Label(root,text="Ticket-id").place(x=1000,y=310)
l7=Label(root,text="Sno.:").place(x=1060,y=310)
button2=Button(root,text="ADD",command=add1).place(x=1000,y=365)
e_b=Entry(width=8)
e_b.place(x=1000,y=335)
l5=Label(root,text="Sno.:").place(x=100,y=365)
e_d1=Entry(width=2)
e_d1.place(x=135,y=365)
l6=Label(root,text="Ticket-id:").place(x=155,y=365)
e_d2=Entry(width=8)
e_d2.place(x=215,y=365)
e_c=Entry(width=2)
e_c.place(x=1060,y=335)
#l2=Label(root,text="Dno  Cid  Amount").place(x=140,y=290)
#e_d1=Entry(width=3)
#e_d1.place(x=140,y=310)
#e_d2=Entry(width=3)
#e_d2.place(x=170,y=310)
#e_d3=Entry(width=5)
#e_d3.place(x=200,y=310)
button1=Button(root,text="Delete",command=delete).place(x=50,y=365)
button3=Button(root,text="Delete",command=delete1).place(x=1040,y=365)
