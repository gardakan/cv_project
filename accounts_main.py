from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import db_handler


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


class mainWindow(object):
    
    def __init__(self,master):
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
        subMenu.add_command(label="Delete Account", command=db.deleteRow)
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
        self.printButt = Button(toolbar, text="Delete Account", command=self.doNothing)
        printButt = self.printButt
        printButt.pack(side=LEFT, padx=2,pady = 2)
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

    def enterNew(self):
        self.ena = EnterNewWindow(self.master)  # Popup window with entry fields
        self.master.wait_window(self.ena.top)
        self.result = self.ena.value
        print(self.result)
        db.dataEntry(self.result[0],float(self.result[1]),float(self.result[2]),self.result[3])
        a.set("Entry %s succesfully added." % self.result[0])
        db.readValue()

    def valuesTree(self):
        
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
        a.set("This will do more later...")

    def deleteValue(self):
        pass

root = Tk()
db = db_handler.Db()
a = StringVar()
m = mainWindow(root)
root.mainloop()
