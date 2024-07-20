import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
def Depositreport():
    report = tk.Tk()
    report.geometry("1220x600+30+100")
    report.title("Account Report")
    report.resizable(0,0)
    report.configure(bg='pink')
    def exitfun():
        report.destroy()
    label = tk.Label(report, text="Deposit Report", font=("Times New Roman",22), bg='pink')
    label.place(x=590, y=50)
    bt1=tk.Button(report, text="Exit",width='6',fg='red',font=('Times New Roman',12),command=exitfun)
    bt1.place(x=600,y=340)
    cols = ('Account No', 'Customer Name','Phone No','Deposit Amount','Deposit Date')
    listBox = ttk.Treeview(report, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.place(x=100, y=100)
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="bankingdb")
    try:
        mycursor = mydb.cursor()
        sql = "select * from deposit"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            listBox.insert("", "end", values=(x[0], x[1],x[3],x[4],x[5]))
    except Error as error:
        messagebox.showinfo("Confirmation", error)
    report.mainloop()
