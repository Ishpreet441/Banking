import mysql.connector
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
def Accountwithdrawn():
   def exitfun():
      window.destroy()
   def display(event):
      aa=cb.get()
      t1.delete(0,END)
      t2.delete(0,END)
      t3.delete(0,END)
      t4.delete(0,END)
      t5.delete(0,END)
      t6.delete(0,END)
      t7.delete(0,END)
      #t9.delete(0,END)
      #t11.delete(0,END)
      #t12.delete(0,END)
      mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="bankingdb")
      mycursor= mydb.cursor()
      sql="SELECT * FROM accountopening where accountnumber=(%s)"
      val=(aa,)
      mycursor.execute(sql,val)
      myresult=mycursor.fetchall()
      for x in myresult:
        t1.insert(INSERT,x[0])
        t2.insert(INSERT,x[1])
        t3.insert(INSERT,x[4])
        t4.insert(INSERT,x[5])
      sql="SELECT * FROM balance where accountnumber=(%s)"
      val=(aa,)
      mycursor.execute(sql,val)
      myresult=mycursor.fetchall()
      for x1 in myresult:
        t5.insert(INSERT,x1[1])
   def save():
      aa=cb.get()
      a=t1.get()
      b=t2.get()
      c=t3.get()
      d=t4.get()
      e=t5.get()
      f=t6.get()
      g=t7.get()
      if(a==""):
        messagebox.showwarning('Status',"Enter Account Number")
      elif(b==""):
        messagebox.showwarning('Status',"Enter Customer Name")
      elif(c==""):
        messagebox.showwarning('Status',"Enter Address")
      elif(d==""):
        messagebox.showwarning('Status',"Enter Phone Number")
      elif(e==""):
        messagebox.showwarning('Status',"Enter Amount.")
      elif(f==""):
         messagebox.showwarning('Status',"Enter Withdrawn Amt.")
      elif(g==""):
         messagebox.showwarning('Status',"Enter Withdrawn Date")
      else:
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="bankingdb")
        mycursor=mydb.cursor()
        sql="INSERT INTO withdraw VALUES(%s,%s,%s,%s,%s,%s,%s)"
        val=(a,b,c,d,e,f,g)
        mycursor.execute(sql,val)
        mydb.commit()
        if(mycursor.rowcount>0):
           sql="SELECT * FROM balance where AccountNumber=(%s)"
           val=(aa,)
           mycursor.execute(sql,val)
           myresult=mycursor.fetchall()
           for x in myresult:
              amt=x[1]
           ab=int(amt)-int(f)
           sql="update balance set Amount=(%s) where AccountNumber=(%s)"
           val=(str(ab),aa)
           mycursor.execute(sql,val)
           mydb.commit()
           t1.delete(0,END)
           t2.delete(0,END)
           t3.delete(0,END)
           t4.delete(0,END)
           t5.delete(0,END)
           t6.delete(0,END)
           t7.delete(0,END)
           cb.delete(0,END)
           messagebox.showinfo("Record Updated Successfully")
   window=tkinter.Tk()
   window.geometry("1700x800+0+0")
   window.title("Amount Withdrawn Form")
   frame=tk.Frame(window,bg='green')
   frame.pack(fill='both',expand='yes')
   '''load = Image.open("b10.jpg")
   render = ImageTk.PhotoImage(load)
   img = Label(frame, image=render)
   img.image = render
   img.place(x=260, y=200)'''
   heading=tk.Label(frame,text="Amount Withdrawn Form", bg='green', font=("Times New Roman", 20),fg='white')
   heading.place(x=340, y=30)
   an=tk.Label(frame,text='Select Account Number',bg='green',fg='blue',font=("Times New Roman", 14))
   an.place(x=180,y=100)
   cb = ttk.Combobox(frame, values=("Select"))
   cb.place(x=400, y=100)
   cb.current(0)
   cb.bind("<<ComboboxSelected>>",display)
    #t1=tk.Entry(frame,text="")
    #t1.place(x=400,y=100)
   ann=tk.Label(frame,text='Account Number',bg='green',font=("Times New Roman", 13),fg='black')
   ann.place(x=950,y=100)
   t1=tk.Entry(frame,text="",width=25)
   t1.place(x=1100,y=100)
   cn=tk.Label(frame,text="Customer Name",bg='green',font=("Times New Roman", 13),fg='black')
   cn.place(x=950,y=150)
   t2=tk.Entry(frame,text="",width=25)
   t2.place(x=1100,y=150)
   address=tk.Label(frame,text="Address",bg='green',font=("Times New Roman", 13),fg='black')
   address.place(x=950,y=200)
   t3=tk.Entry(frame,text="",width=25)
   t3.place(x=1100,y=200)
   #t5=scrolledtext.ScrolledText(frame,width=10,height=5)
   #t5.place(x=400,y=300)
   pn=tk.Label(frame,text="Phone number",bg='green',font=("Times New Roman", 13),fg='black')
   pn.place(x=950,y=330)
   t4=tk.Entry(frame,text="",width=25)
   t4.place(x=1100,y=330)
   at=tk.Label(frame,text="Amount",bg='green',font=("Times New Roman", 13),fg='black')
   at.place(x=950,y=380)
   t5=tk.Entry(frame,text="",width=25)
   t5.place(x=1100,y=380)
   da=tk.Label(frame,text="Withdrawn Amt.",bg='green',font=("Times New Roman", 13),fg='black')
   da.place(x=950,y=430)
   t6=tk.Entry(frame,text="",width=25)
   t6.place(x=1100,y=430)
   vb=tk.Label(frame,text="Withdrawn Date",bg='green',font=("Times New Roman", 13),fg='black')
   vb.place(x=950,y=480)
   t7=tk.Entry(frame,text="",width=25)
   t7.place(x=1100,y=480)
   bt=tk.Button(frame, text="Save",width='6',fg='red',font=('Times New Roman',12),command=save)
   bt.place(x=1100,y=550)
   bt1=tk.Button(frame, text="Exit",width='6',fg='red',font=('Times New Roman',12),command=exitfun)
   bt1.place(x=1190,y=550)
   mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       passwd="",
       database="bankingdb"
       )
   mycursor = mydb.cursor()
   mycursor.execute("SELECT * FROM accountopening")
   myresult = mycursor.fetchall()
   for x in myresult:
     cb['values']+=(x[0],)
   window.mainloop()
