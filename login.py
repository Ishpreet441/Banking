import tkinter
import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox
from menubar import *
from PIL import Image, ImageTk
def login():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bankingdb"
  )
  a=t1.get()
  b=t2.get()
  if(a==""):
      messagebox.showinfo("Enter Username")
  elif(b==""):
      messagebox.showwarning("Enter Password")
  else:
      mycursor = mydb.cursor()
      sql=("SELECT * FROM login where Username=%s and Password=%s")
      val=(a,b)
      mycursor.execute(sql,val)
      myresult = mycursor.fetchall()
      ab=mycursor.rowcount
      if ab>0:
          messagebox.showinfo('Status',"Username/Passowrd accepted....")
          window.destroy()
          MainMenu()
      else:
          messagebox.showinfo('Status',"Invalid Username/Passowrd...")
window=tkinter.Tk()
window.geometry("750x400+300+100")
window.title("Login Form")
frame=tk.Frame(window,bg='yellow')
frame.pack(fill='both',expand='yes')
'''
load = Image.open("login.jpg")
render = ImageTk.PhotoImage(load)
img = Label(frame, image=render)
img.image = render
img.place(x=40, y=180)
'''
heading=tk.Label(frame,text="LogIn Form", bg='yellow', font=("Times New Roman", 18),fg='black')
heading.place(x=340, y=40)
un=tk.Label(frame,text='Username',bg='yellow')
un.place(x=300,y=110)
t1=tk.Entry(frame,text="")
t1.place(x=400,y=110)
pwd=tk.Label(frame,text="Password",bg='yellow')
pwd.place(x=300,y=150)
t2=tk.Entry(frame,text="")
t2.place(x=400,y=150)
bt=Button(text="LogIn",width='6',fg='blue',font=('Times New Roman',12),command=login)
bt.place(x=430,y=200)
window.mainloop()
