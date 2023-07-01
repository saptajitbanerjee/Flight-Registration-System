from tkinter import *
from tkinter import messagebox
import cx_Oracle
root=Tk()
root.title("Tkinter")
root.configure(bg="light blue")
root.geometry("280x400")
name=Label(root,text="Name").place(x=10,y=5)
e_name=Entry(width=40)
e_name.place(x=10,y=30)
click=StringVar()#;click.set("")
click1=StringVar()
click2=StringVar()
click3=StringVar()
click4=StringVar()
click5=StringVar();click5.set("None")
c=0
def price():
   global c
   global label1
   c=dict1[str(click2.get())]+dict2[str(click3.get())]+dict3[str(click.get())]+dict4[str(click1.get())]+dict5[str(click5.get())]
   label1=Label(root,text=c)
   label1.place(x=10,y=330)
def book():
   global t_id
   global s_no
   global data
   if str(e_id.get())!="" and str(e_pin.get())!="":
      username="J-Component"
      userpwd="password"
      host="DESKTOP-EEH7CHG/XE"
      mydb=connection=cx_Oracle.connect(username,userpwd,host)
      mycursor=mydb.cursor()
      mycursor.execute("select ticket_id from tickets")
      row=mycursor.fetchall()
      n=int(row[len(row)-1][0][3:])+1
      t_id="ABC"+str(n)
      if(str(click2.get())=='Air India'):
         mycursor.execute("select max(seat_no) from tickets where company in('Air India')")
         row=mycursor.fetchall()
      if(str(click2.get())=='Indigo'):
         mycursor.execute("select max(seat_no) from tickets where company in('Indigo')")
         row=mycursor.fetchall()
      if(str(click2.get())=='Vistara'):
         mycursor.execute("select max(seat_no) from tickets where company in('Vistara')")
         row=mycursor.fetchall()
      s_no=row[len(row)-1][0]+1
      com="insert into tickets values(:1,:2,:3,:4,:5,:6,:7)"
      data=[(c,str(click.get()),str(click1.get()),str(click2.get()),str(e_name.get()),str(t_id),s_no)]
      mycursor.executemany(com,data)
      mydb.commit()
      #com="inser into class values(:1,:2,:3)"
      #data=[(str(click3.get()),dict2[str(click3.get())],)]
      #mydb.commit()
      mycursor.execute("select recipt_no from payment")
      row=mycursor.fetchall()
      r_no=int(row[len(row)-1][0])+1
      com="insert into payment values(:1,:2,:3,:4,:5)"
      data=[(str(e_id.get()),str(e_pin.get()),str(click4.get()),str(r_no),str(t_id))]
      mycursor.executemany(com,data)
      mydb.commit()
      messagebox.showinfo("Flight Ticket Details","Your Ticket has been successfully booked\n"+"Your Flight number is :"+str(t_id)+"\nYour Seat Number is :"+str(s_no)+"\nReceipt Number of Payment is:"+str(r_no))
      mydb.close()
      click.set("");click1.set("");click2.set("");click3.set("");click4.set("");click5.set("None")
      e_id.delete(0,END);e_id.insert(0,"");e_pin.delete(0,END);e_pin.insert(0,"")
      e_name.delete(0,END);e_name.insert(0,"");label1.config(text="")
   elif str(e_id.get())=="" or str(e_pin.get())=="":
      messagebox.showinfo("Invalid Payment Details","Please enter your Card_id and PIN for payment")
l1=Label(root,text="Source").place(x=10,y=55)
source=OptionMenu(root,click,"Mumbai","New York","Chennai","Delhi","Kolkata")
source.place(x=10,y=80)
l2=Label(root,text="Destination").place(x=10,y=115)
destination=OptionMenu(root,click1,"Mumbai","New York","Chennai","Delhi","Kolkata")
destination.place(x=10,y=140)
l3=Label(root,text="Airlines").place(x=10,y=175)
company=OptionMenu(root,click2,"Indigo","Air India","Vistara")
company.place(x=10,y=200)
l4=Label(root,text="Class").place(x=10,y=235)
seat=OptionMenu(root,click3,"Economy Class","First Class","Buisiness Class")
seat.place(x=10,y=260)
l5=Label(root,text="Payment").place(x=140,y=55)
l6=Label(root,text="Mode of Payment").place(x=140,y=80)
mode=OptionMenu(root,click4,"Debit Card","Credit Card","Bitcoin")
mode.place(x=140,y=105)
l7=Label(root,text="Card-id").place(x=140,y=140)
e_id=Entry()
e_id.place(x=140,y=165)
l8=Label(root,text="Enter PIN").place(x=140,y=190)
e_pin=Entry()
e_pin.place(x=140,y=215)
l9=Label(root,text="Airline Meal").place(x=140,y=240)
food=OptionMenu(root,click5,"None","Veg","Non-veg")
food.place(x=140,y=265)
dict1={"Indigo":2000,"Air India":1500,"Vistara":2500}
dict2={"Economy Class":100,"First Class":200,"Buisiness Class":250}
dict3={"Mumbai":120,"New York":250,"Chennai":100,"Delhi":110,"Kolkata":95}
dict4={"Mumbai":120,"New York":250,"Chennai":100,"Delhi":110,"Kolkata":95}
dict5={"None":0,"Veg":250,"Non-veg":300}
button=Button(root,text="See Price",command=price).place(x=10,y=300)
button1=Button(root,text="Book Ticket",command=book).place(x=10,y=360)
boutton2=Button(root,text="  Exit  ",command=exit).place(x=140,y=360)
