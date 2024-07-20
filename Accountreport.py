import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
def Accountreport():
        report = tk.Tk()
        report.geometry("1160x500+100+100")
        report.title("Account Report")
        report.resizable(0,0)
        report.configure(bg='pink')
        def exitfun():
            report.destroy()
        label = tk.Label(report, text="Account Report", font=("Times New Roman",22), bg='pink')
        label.place(x=530, y=50)
        bt1=tk.Button(report, text="Exit",width='6',fg='red',font=('Times New Roman',12),command=exitfun)
        bt1.place(x=600,y=340)
        cols = ('Account Name', 'Customer Name','Phone Number','Amount','Nominee')
        listBox = ttk.Treeview(report, columns=cols, show='headings')
        for col in cols:
            listBox.heading(col, text=col)
        listBox.place(x=100, y=100)
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="bankingdb")
        try:
            mycursor = mydb.cursor()
            sql = "select * from accountopening"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for x in myresult:
                listBox.insert("", "end", values=(x[0], x[1],x[5],x[7],x[8]))
        except Error as error:
            messagebox.showinfo("Confirmation", error)
        report.mainloop()
