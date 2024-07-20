from accountopening import *
from accountediting import *
from Accountdeposit import *
from Accountwithdrawn import *
from Accountclosing import *
from Accountreport import *
from Depositreport import *
from Withdrawnreport import *
from tkinter import *
from tkinter import Menu
def MainMenu():
  '''def ActOpen():
      AccountOpening()
  def ActEdit():
      AccountEditing()
  def ActDeposit():
      Accountdeposit()
  def ActWithdrawn():
      Accountwithdrawn()
  def ActClosing():
      AccountClosing()
  def ActReport():
      Accountreport()
  def DptReport():
      Depositreport()
  def WdnReport():
      Withdrawnreport()'''
  def show():
      messagebox.showinfo('About Me','Proect Developed in Python with Mysql database')
  def exitfun():
        title = 'Please Confirm'
        content = 'Really do you want to exit?'
        ans = messagebox.askquestion(title,content)
        if ans == 'yes':
            messagebox.showinfo('Status','Okay Bye Bye Visit Again......')
            quit()
        else:
            messagebox.showinfo('Status','Press enter to continue')
  window=Tk()
  window.title("Banking system")
  w, h = window.winfo_screenwidth(), window.winfo_screenheight()
  window.geometry("%dx%d+0+0" % (w, h))
  window.configure(bg="yellow")
  menubar = Menu(window)
  window.config(menu=menubar)
  a = Menu(menubar, tearoff=0)
  menubar.add_cascade(label="Information", menu=a)
  a.add_command(label="A/C Opening", command=AccountOpening)
  a.add_separator()
  a.add_command(label="A/C Editing", command=AccountEditing)
  b = Menu(menubar, tearoff=0)
  menubar.add_cascade(label="Transaction", menu=b)
  b.add_command(label="Deposit",command=Accountdeposit)
  b.add_separator()
  b.add_command(label="Withdrawn",command=Accountwithdrawn)
  b.add_separator()
  b.add_command(label="Closing balance",command=AccountClosing)
  c = Menu(menubar, tearoff=0)
  menubar.add_cascade(label="Reports", menu=c)
  c.add_command(label="All a/c report",command=Accountreport)
  c.add_separator()
  c.add_command(label="Deposits report",command=Depositreport)
  c.add_separator()
  c.add_command(label="Withdrawn reports",command=Withdrawnreport)
  d = Menu(menubar, tearoff=0)
  menubar.add_cascade(label="Help", menu=d)
  d.add_command(label="About Me",command=show)
  d.add_separator()
  d.add_command(label="Exit",command=exitfun)
  window.mainloop()
