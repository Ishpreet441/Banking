import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
def AccountEditing():
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
      t9.delete(0,END)
      t11.delete(0,END)
      t12.delete(0,END)
      mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="bankingdb")
      mycursor= mydb.cursor()
      sql="SELECT * FROM accountopening where accountnumber=(%s)"
      val=(aa,)
      mycursor.execute(sql,val,)
      myresult=mycursor.fetchall()
      for x in myresult:
        t1.insert(INSERT,x[0])
        t2.insert(INSERT,x[1])
        t3.insert(INSERT,x[2])
        t4.insert(INSERT,x[3])
        t5.insert(INSERT,x[4])
        t6.insert(INSERT,x[5])
        t7.insert(INSERT,x[6])
        t9.insert(INSERT,x[8])
        t11.insert(INSERT,x[10])
        t12.insert(INSERT,x[11])
    def Update():
      abc=cb.get()
      d=t1.get()
      e=t2.get()
      f=t3.get()
      g=t4.get()
      #h=t5.get("1.0",tkinter.END)
      h=t5.get()
      i=t6.get()
      j=t7.get()
      k=t9.get()
      l=t11.get()
      m=t12.get()
      #n=tt.get()
      if(d==""):
        messagebox.showwarning('Status',"Enter Account Number")
      elif(e==""):
        messagebox.showwarning('Status',"Enter Customer Name")
      elif(f==""):
        messagebox.showwarning('Status',"Enter Father name")
      elif(g==""):
        messagebox.showwarning('Status',"Enter Mother name")
      elif(h==""):
        messagebox.showwarning('Status',"Enter Address")
      elif(i==""):
        messagebox.showwarning('Status',"Enter Phone Number")
      elif(j==""):
        messagebox.showwarning('Status',"Enter Age")
      elif(k==""):
        messagebox.showwarning('Status',"Enter Nominee")
      elif(l==""):
        messagebox.showwarning('Status',"Enter Verified by")
      elif(m==""):
        messagebox.showwarning('Status',"Enter Security number")
      else:
        mycursor=mydb.cursor()
        sql="update accountopening set accountnumber=(%s), customername=(%s),fathername=(%s),mothername=(%s),address=(%s),phonenumber=(%s),age=(%s),nominee=(%s),verifiedby=(%s),securitynumber=(%s) where accountnumber=(%s)"
        val=(d,e,f,g,h,i,j,k,l,m,abc)
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo("Record Updated Successfully")
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
        t4.delete(0,END)
        t5.delete(0,END)
        t6.delete(0,END)
        t7.delete(0,END)
        t9.delete(0,END)
        t11.delete(0,END)
        t12.delete(0,END)
      #tt.delete(0,END)
    window=tkinter.Tk()
    window.geometry("1200x800+0+0")
    window.title("Account Editing")
    w, h = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry("%dx%d+0+0" % (w, h))
    frame=tk.Frame(window,bg='grey')
    frame.pack(fill='both',expand='yes')
    heading=tk.Label(frame,text="Account Editing Form", bg='grey', font=("Times New Roman", 20),fg='black')
    heading.place(x=340, y=30)
    an=tk.Label(frame,text='Select Account Number',bg='grey',font=("Times New Roman", 13),fg='blue')
    an.place(x=150,y=100)
    cb = ttk.Combobox(frame, values=("Select"))
    cb.place(x=350, y=100)
    cb.current(0)
    cb.bind("<<ComboboxSelected>>",display)
    #t1=tk.Entry(frame,text="")
    #t1.place(x=400,y=100)
    ann=tk.Label(frame,text='Account Number',bg='grey',font=("Times New Roman", 13),fg='blue')
    ann.place(x=950,y=100)
    t1=tk.Entry(frame,text="",width=25)
    t1.place(x=1100,y=100)
    cn=tk.Label(frame,text="Customer Name",bg='grey',font=("Times New Roman", 13),fg='blue')
    cn.place(x=950,y=150)
    t2=tk.Entry(frame,text="",width=25)
    t2.place(x=1100,y=150)
    fn=tk.Label(frame,text="Father Name",bg='grey',font=("Times New Roman", 13),fg='blue')
    fn.place(x=950,y=200)
    t3=tk.Entry(frame,text="",width=25)
    t3.place(x=1100,y=200)
    mn=tk.Label(frame,text="Mother Name",bg='grey',font=("Times New Roman", 13),fg='blue')
    mn.place(x=950,y=250)
    t4=tk.Entry(frame,text="",width=25)
    t4.place(x=1100,y=250)
    address=tk.Label(frame,text="Address",bg='grey',font=("Times New Roman", 13),fg='blue')
    address.place(x=950,y=300)
    #t5=tk.Entry(frame,text="",width=25)
    #t5.place(x=1200,y=300)
    t5=tk.Entry(frame,text="",width=25)
    t5.place(x=1100,y=300)
    #t5=scrolledtext.ScrolledText(frame,width=15,height=5)
    #t5.place(x=1100,y=300)
    pn=tk.Label(frame,text="Phone number",bg='grey',font=("Times New Roman", 13),fg='blue')
    pn.place(x=950,y=400)
    t6=tk.Entry(frame,text="",width=25)
    t6.place(x=1100,y=400)
    ag=tk.Label(frame,text="Age",bg='grey',font=("Times New Roman", 13),fg='blue')
    ag.place(x=950,y=450)
    t7=tk.Entry(frame,text="",width=25)
    t7.place(x=1100,y=450)
    nn=tk.Label(frame,text="Nominee",bg='grey',font=("Times New Roman", 13),fg='blue')
    nn.place(x=950,y=500)
    t9=tk.Entry(frame,text="",width=25)
    t9.place(x=1100,y=500)
    vb=tk.Label(frame,text="Verified By",bg='grey',font=("Times New Roman", 13),fg='blue')
    vb.place(x=950,y=550)
    t11=tk.Entry(frame,text="",width=25)
    t11.place(x=1100,y=550)
    sn=tk.Label(frame,text="Security Number",bg='grey',font=("Times New Roman", 13),fg='blue')
    sn.place(x=950,y=600)
    t12=tk.Entry(frame,text="",width=25)
    t12.place(x=1100,y=600)
    bt=tk.Button(frame, text="Update",width='6',fg='blue',font=('Times New Roman',13),command=Update)
    bt.place(x=1100,y=650)
    bt1=tk.Button(frame, text="Exit",width='6',fg='blue',font=('Times New Roman',12),command=exitfun)
    bt1.place(x=1190,y=650)
    '''load = Image.open("b6.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(frame, image=render)
    img.image = render
    img.place(x=60, y=130)'''
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
#      if x not in cb['values']:
          cb['values']+=(x[0],)
    window.mainloop()
