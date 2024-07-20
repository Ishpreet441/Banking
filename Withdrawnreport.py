import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
def Withdrawnreport():
    report = tk.Tk()
    report.geometry("1170x500+30+100")
    report.title("Amount Withdrawn Report")
    report.resizable(0,0)
    report.configure(bg='pink')
    def exitfun():
        report.destroy()
    label = tk.Label(report, text="Withdrawn Report", font=("Times New Roman",20), bg='pink')
    label.place(x=550, y=50)
    bt1=tk.Button(report, text="Exit",width='6',fg='red',font=('Times New Roman',12),command=exitfun)
    bt1.place(x=600,y=340)
    cols = ('Account Name', 'Customer Name','Phone Number','Withdrawn Amount','Date')
    listBox = ttk.Treeview(report, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.place(x=100, y=100)
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="bankingdb")
    try:
        mycursor = mydb.cursor()
        sql = "select * from withdraw"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            listBox.insert("", "end", values=(x[0], x[1],x[3],x[4],x[6]))
    except Error as error:
        messagebox.showinfo("Confirmation", error)
    report.mainloop()
