#!/usr/bin/python

from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import db_handler

__author__ = "John Tamm-Buckle"
__credits__ = "John Tamm-Buckle"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "John Tamm-Buckle"
__email__ = "jtammbuckle@gmail.com"
__status__ = "Development"


# Dropdown menu - generate reports.
# Tooltip bar - print status when executing functions (i.e. currency conversions)

output1 = "test"
output2 = "also a test but it's long"

'''tkinter.messagebox.showinfo('Window Title', 'Monkeys can live up to 300 years')

answer = tkinter.messagebox.askquestion('What is a thing', 'Is it not a thing that isn\'t a non-thing?')

if answer == 'yes':
    print("fwuifl gufl w7f yf7wly389gwul8902ddshi d . ... . .....")'''

class EnterNewWindow(object):
    def __init__(self, master):
        """Edit window for adding new accounts to the database.  4 text fields to enter name, balance, tax paid and default currency"""
        top = self.top = Toplevel(master)
        self.frameNew=Frame(top)
        self.frameNew.pack(side=TOP)
        self.l = Label(self.frameNew, text = "Please enter account information")
        self.l.pack()
        self.frameNew2=Frame(top)
        self.frameNew2.pack(side=TOP)
        self.anlab = Label(self.frameNew2, text = "Account Name:")
        self.anlab.grid(row = 0, column = 0, sticky=E)
        self.aname = Entry(self.frameNew2)
        self.aname.grid(row = 0, column = 1)
        self.ablab = Label(self.frameNew2, text = "Account Balance:")
        self.ablab.grid(row = 1, column = 0, sticky = E)
        self.abal = Entry(self.frameNew2)
        self.abal.grid(row = 1, column = 1)
        self.atlab = Label(self.frameNew2, text = "Tax Paid:")
        self.atlab.grid(row = 2, column = 0, sticky = E)
        self.atax = Entry(self.frameNew2)
        self.atax.grid(row = 2, column = 1)
        self.aclab = Label(self.frameNew2, text = "Default Currency:")
        self.aclab.grid(row = 3, column = 0, sticky = E)
        self.acur = Entry(self.frameNew2)
        self.acur.grid(row = 3, column = 1)
        self.frameNew3=Frame(top)
        self.frameNew3.pack(side=BOTTOM)
        self.b=Button(self.frameNew3,text='Submit',command=self.cleanup)
        self.b.pack()
        
    def cleanup(self):
        self.name = self.aname.get()
        self.bal = self.abal.get()
        self.tax = self.atax.get()
        self.cur = self.acur.get()
        self.nonvalue = True
        self.value = [self.name, self.bal, self.tax, self.cur]
        # Avoid TypeErrors vvvvvvv
        while self.nonvalue == True:
            for i in range(len(self.value)):
                if not self.value[i]:
                    tkinter.messagebox.showinfo('Please complete all fields', 'All fields must be filled.')
                    self.nonvalue = False
                    break
            while self.nonvalue == True:
                try:
                    self.baltest = float(self.bal)
                except(ValueError):
                    tkinter.messagebox.showinfo('ValueError: Account Balance', 'Only characters 0-9 and the decimal point "." may be used in this field.')
                    self.nonvalue = False
                    break
                try:
                    self.taxtest = float(self.tax)
                except(ValueError):
                    tkinter.messagebox.showinfo('ValueError: Tax Paid', 'Only characters 0-9 and the decimal point "." may be used in this field.')
                    self.nonvalue = False
                    break
                self.nonvalue = False
                self.top.destroy()


class DeleteAccount(object):
    def __init__(self, master):
        """Enter the ID of the account to delete"""
        top2 = self.top2 = Toplevel(master)
        self.delFrameNew=Frame(top2)
        self.delFrameNew.pack(side=TOP)
        self.delLabel = Label(self.delFrameNew, text = "Please ente the ID of the account to delete: ")
        self.delLabel.pack()
        self.delFrameNew2=Frame(top2)
        self.delFrameNew2.pack(side=TOP)
        self.deLab = Label(self.delFrameNew2, text = "Account ID: ")
        self.deLab.grid(row = 0, column = 0, sticky=E)
        self.delName = Entry(self.delFrameNew2)
        self.delName.grid(row = 0, column = 1)
        self.delFrameNew3=Frame(top2)
        self.delFrameNew3.pack(side=BOTTOM)
        self.b=Button(self.delFrameNew3,text='Submit',command=self.delCleanup)
        self.b.pack()

    def delCleanup(self):
        self.deletedID = self.delName.get()
        self.deletedVar = True
        while self.deletedVar == True:
            self.verify = tkinter.messagebox.askquestion('Delete Account', 'Are you sure you want to continue?  This action cannot be undone.')
            if self.verify == 'no':
                self.deletedID = "cancel"
                self.top2.destroy()
            if not self.deletedID:
                tkinter.messagebox.showinfo('Please complete all fields', 'All fields must be filled.')
                self.deletedVar = False
                break
            else:
                try:
                    self.deletedID = int(self.deletedID)
                except(ValueError):
                    tkinter.messagebox.showinfo('ValueError', 'Only integer values between 0-9 may be used in this field.')
                    self.deletedVar = False
                    break
            self.deletedVar = False
            self.top2.destroy()
            

class mainWindow(object):
    
    def __init__(self,master):
        """Main display - shows database contents as well as status messages, and button shortcuts to add and delete accounts."""
        self.master=master

        # status bar
        self.status = Label(master, textvariable=a, bd=1, relief=SUNKEN, anchor=W)
        status = self.status
        status.pack(side=BOTTOM, fill=X)
        a.set("This will be displayed below ???")

        # main menu
        self.menu = Menu(root)  
        menu = self.menu
        root.config(menu=menu)

        self.subMenu = Menu(menu)
        subMenu = self.subMenu
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Add New...", command=self.enterNew)
        subMenu.add_command(label="Delete Account", command=self.deleteValue)
        subMenu.add_separator()
        subMenu.add_command(label="Arse about on the internet...", command=self.doNothing)
        subMenu.add_command(label="Quit", command=self.quitProgram)

        self.editMenu = Menu(menu)
        editMenu = self.editMenu
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Edit Account...", command = db.editEntry)

        self.reportsMenu = Menu(menu)
        reportsMenu = self.reportsMenu
        menu.add_cascade(label="Reports", menu=reportsMenu)
        reportsMenu.add_command(label="Generate monthly report...", command=self.doNothing)

        # the toolbar
        self.toolbar = Frame(root, bg="light slate grey")
        toolbar = self.toolbar

        self.insertButt = Button(toolbar, text="Add New...", command=self.enterNew)
        insertButt = self.insertButt
        insertButt.pack(side=LEFT, padx=2,pady = 2)
        self.delButt = Button(toolbar, text="Delete Account", command=self.deleteValue)
        delButt = self.delButt
        delButt.pack(side=LEFT, padx=2,pady = 2)
        self.refreshButt = Button(toolbar, text="Refresh", command=self.valuesTree)
        refreshButt = self.refreshButt
        refreshButt.pack(side=LEFT, padx=2,pady = 2)

        toolbar.pack(side=TOP, fill=X)

        self.frame1 = Frame(root)
        frame1 = self.frame1

        # View database contents
        self.tree = ttk.Treeview(frame1)

        self.tree["columns"]=("one","two","three","four","five","six")
        self.tree.column("one", width=100)
        self.tree.column("two", width=200)
        self.tree.column("three", width=150)
        self.tree.column("four", width=100)
        self.tree.column("five", width=100)
        self.tree.column("six", width=100)
        self.tree.heading("one", text="Account ID")
        self.tree.heading("two", text="Entry Date")
        self.tree.heading("three", text="Account Name")
        self.tree.heading("four", text="Account Balance")
        self.tree.heading("five", text="Tax paid")
        self.tree.heading("six", text="Default Currency")

        '''tree.insert("" , 0, text="Line 1", values=("1A","1B","1C","1D","1E","1F"))  # Return values for db.readValue() method here.

        self.id2 = tree.insert("", 1, "dir2", text="Dir 2")                      # A directory, probably won't be needed for this unless previous months are listed here...
        tree.insert(self.id2, 3, text=" sub dir 2", values=(list(range(6))))'''

        self.tree.pack()

        frame1.pack(side=TOP)
        self.valuesTree()

    def enterNew(self):
        """Add new account"""
        self.ena = EnterNewWindow(self.master)  # Popup window with entry fields
        self.master.wait_window(self.ena.top)
        self.result = self.ena.value
        db.dataEntry(self.result[0],float(self.result[1]),float(self.result[2]),self.result[3])
        a.set("Entry %s succesfully added." % self.result[0])
        db.readValue()

    def deleteValue(self):
        """Delete account"""
        self.delAccount = DeleteAccount(self.master)
        self.master.wait_window(self.delAccount.top2)
        self.delRes = self.delAccount.deletedID
        db.deleteValue(self.delRes)
        a.set("Entry deleted.")
        db.readValue()

    def valuesTree(self):
        """Display current database"""
        try:
            self.row = db.readValue()
            row = self.row
            self.tree.delete(*self.tree.get_children())
            for i in row:
                self.tree.insert("" , int(i[0])-1, text=i[0], values=(i[1:6]))
            a.set("Database updated.")
        except(TypeError):
            a.set("Database is empty.")

    def doNothing(self):
        """Test function which doesn't do anything useful"""
        a.set("Nothing here...")
    
    def quitProgram(self):
        quitYN = tkinter.messagebox.askquestion("Exit", "Save changes?")
        if quitYN == 'yes':
            db.con.commit()
            a = "Changes saved."
            db.con.close()
            root.destroy()
        else:
            root.destroy()

    def setStatus(self):
        """Displays status message"""
        a.set("This will do more later...")

root = Tk()
db = db_handler.Db()
a = StringVar()
m = mainWindow(root)
root.mainloop()
