from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import tkinter
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
def Accountdeposit():
   def exitfun():
      window.destroy()
   def display(event):
      aa=cb.get()
      t1.delete(0,END)
      t2.delete(0,END)
      t3.delete(0,END)
      t4.delete(0,END)
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
   def save():
      aa=cb.get()
      a=t1.get()
      b=t2.get()
      #c=t3.get("1.0",tkinter.END)
      c=t3.get()
      d=t4.get()
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
      elif(f==""):
        messagebox.showwarning('Status',"Enter Deposit Amt.")
      elif(g==""):
         messagebox.showwarning('Status',"Enter Deposit Date")
      else:
        mycursor=mydb.cursor()
        sql="INSERT INTO deposit VALUES(%s,%s,%s,%s,%s,%s)"
        val=(a,b,c,d,f,g)
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo("Record Updated Successfully")
        sql="SELECT * FROM balance where AccountNumber=(%s)"
        val=(aa,)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchall()
        for x in myresult:
            amt=x[1]
        ab=int(amt)+int(f)
        sql="update balance set Amount=(%s) where AccountNumber=(%s)"
        val=(str(ab),aa)
        mycursor.execute(sql,val)
        mydb.commit()
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
        t4.delete(0,END)
        t6.delete(0,END)
        t7.delete(0,END)
   window=tkinter.Tk()
   window.geometry("1700x800+0+0")
   window.title("Amount Deposit Form")
   frame=tk.Frame(window,bg='grey')
   frame.pack(fill='both',expand='yes')
   '''load = Image.open("b2.jpg")
   render = ImageTk.PhotoImage(load)
   img = Label(frame, image=render)
   img.image = render
   img.place(x=260, y=200)'''
   heading=tk.Label(frame,text="Amount Deposit Form", bg='grey', font=("Times New Roman", 20),fg='yellow')
   heading.place(x=340, y=30)
   an=tk.Label(frame,text='Select Account Number',bg='grey',fg='blue',font=("Times New Roman", 12))
   an.place(x=200,y=100)
   cb = ttk.Combobox(frame, values=("Select"))
   cb.place(x=390, y=100)
   cb.current(0)
   cb.bind("<<ComboboxSelected>>",display)
    #t1=tk.Entry(frame,text="")
    #t1.place(x=400,y=100)
   ann=tk.Label(frame,text='Account Number',bg='grey',font=("Times New Roman", 12),fg='blue')
   ann.place(x=950,y=100)
   t1=tk.Entry(frame,text="",width=25)
   t1.place(x=1100,y=100)
   cn=tk.Label(frame,text="Customer Name",bg='grey',font=("Times New Roman", 12),fg='blue')
   cn.place(x=950,y=150)
   t2=tk.Entry(frame,text="",width=25)
   t2.place(x=1100,y=150)
   address=tk.Label(frame,text="Address",bg='grey',font=("Times New Roman", 12),fg='blue')
   address.place(x=950,y=200)
   t3=tk.Entry(frame,text="",width=25)
   t3.place(x=1100,y=200)
   #t3=scrolledtext.ScrolledText(frame,width=15,height=7)
   #t3.place(x=1200,y=200)
   pn=tk.Label(frame,text="Phone number",bg='grey',font=("Times New Roman", 12),fg='blue')
   pn.place(x=950,y=330)
   t4=tk.Entry(frame,text="",width=25)
   t4.place(x=1100,y=330)
   da=tk.Label(frame,text="Deposit Amt.",bg='grey',font=("Times New Roman", 12),fg='blue')
   da.place(x=950,y=380)
   t6=tk.Entry(frame,text="",width=25)
   t6.place(x=1100,y=380)
   vb=tk.Label(frame,text="Deposit Date",bg='grey',font=("Times New Roman", 12),fg='blue')
   vb.place(x=950,y=430)
   t7=tk.Entry(frame,text="",width=25)
   t7.place(x=1100,y=430)
   bt=tk.Button(frame, text="Save",width='6',fg='blue',font=('Times New Roman',12),command=save)
   bt.place(x=1100,y=520)
   bt1=tk.Button(frame, text="Exit",width='6',fg='blue',font=('Times New Roman',12),command=exitfun)
   bt1.place(x=1190,y=520)
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
