#!/usr/bin/python

from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import db_handler
from collections import OrderedDict
from collections import OrderedDict
from functools import partial

__author__ = "John Tamm-Buckle"
__credits__ = "John Tamm-Buckle"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "John Tamm-Buckle"
__email__ = "jtammbuckle@gmail.com"
__status__ = "Development"


# Dropdown menu - generate reports.
# Tooltip bar - print status when executing functions (i.e. currency conversions)

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


class EditAccount(object):
    def __init__(self, master):
        """Populates entry fields with data from selected account, user can edit and click submit to confirm changes."""
        top3 = self.top3 = Toplevel(master)
        self.editFrame = Frame(top3)
        self.editFrame.pack(side=TOP)
        self.editLabel = Label(self.editFrame, text = "Please enter the account ID of the account you to edit: ")
        self.editLabel.pack()
        self.editFrame2 = Frame(top3)
        self.editFrame2.pack(side=TOP)
        self.editLabelID = Label(self.editFrame2, text = "Account ID: ")
        self.editLabelID.grid(row = 0, column = 0, sticky = E)
        self.editID = Entry(self.editFrame2)
        self.editID.grid(row = 0, column = 1)
        self.editFrame3 = Frame(top3)
        self.editFrame3.pack(side=BOTTOM)
        self.b3 = Button(self.editFrame3, text = 'Submit', command = self.nextEdit)
        self.b3.pack()

    def nextEdit(self):
        self.editedID = self.editID.get()
        self.editVar = True
        while self.editVar == True:
            if not self.editedID:
                tkinter.messagebox.showinfo('Please complete all fields', 'All fields must be filled.')
                self.editVar = False
                break
            else:
                try:
                    self.editedID = int(self.editedID)
                except(ValueError):
                    tkinter.messagebox.showinfo('ValueError', 'Only integer values between 0-9 may be used in this field.')
                    self.editVar = False
                    break
            self.editVar = False
            self.top3.destroy()

class EditFieldPrepopulate(object):
    def __init__(self, master):
        """Prepopulate text fields with data from sqlite table, changes are saved"""
        top4 = self.top4 = Toplevel(master)
        self.questionFrame = Frame(top4)
        self.questionFrame.pack(side=TOP)
        self.a = {}
        self.k = 0
        self.newEdits = []
        self.dateLab = Label(self.questionFrame, text="Entry date (MM, YYYY): ")
        self.dateLab.grid(row = 0, column = 0, sticky = E)
        self.acctLab = Label(self.questionFrame, text="Account name: ")
        self.acctLab.grid(row = 1, column = 0, sticky = E)
        self.balaLab = Label(self.questionFrame, text="Account balance: ")
        self.balaLab.grid(row = 2, column = 0, sticky = E)
        self.taxpLab = Label(self.questionFrame, text="Tax paid: ")
        self.taxpLab.grid(row = 3, column = 0, sticky = E)
        self.editField(m.editList)
        self.submitFrame = Frame(top4)
        self.submitFrame.pack(side=BOTTOM)
        self.submit = Button(self.submitFrame, text = "Submit", command = self.getEditedFieldValues)
        self.submit.pack()
        
    def editField(self, results):
        while self.k < len(results):
            key = self.k
            self.a[self.k] = Text(self.questionFrame, height=1, width=30)
            self.a[self.k].insert(END, str(results[self.k]))
            self.a[self.k].grid(row=self.k,column = 1)
            self.k+=1
        self.binding()

    def default(self, event):
        for itemIndex in self.a:
            current = self.a[itemIndex].get("1.0",END)
            if current == "Default\n":
                self.a[itemIndex].delete("1.0",END)
            elif current == "\n":
                self.a[itemIndex].insert("1.0","Default")
                
    def binding(self):
        for itemIndex in self.a:
            self.a[itemIndex].bind("<FocusIn>", self.default)
            self.a[itemIndex].bind("<FocusOut>",self.default)

    def getEditedFieldValues(self):
        """Get edited values as close window"""
        editVar = True
        for itemIndex in self.a:
            editResults = self.a[itemIndex].get("1.0",END)
            editResults = re.sub('[\\n]','',editResults)
            self.newEdits.append(editResults)
            # Type checking here...
        datecheck = db.dateCheck(self.newEdits[0])
        self.newEdits[0] = re.sub('[\[\]\'\,]','',self.newEdits[0])
        self.newEdits[0] = self.newEdits[0].split()
        print(self.newEdits[0])
        print(len(self.newEdits[0]))
        while editVar == True:
            if datecheck == "error":
                tkinter.messagebox.showinfo('ValueError', 'Only integer values between 0-9 may be used in this field.  Month and year must be separated by a backslash ("/")')
                editVar = False
                break
            else:
                self.newEdits[0] = [datecheck, int(self.newEdits[0][1])]
                print(self.newEdits[0])
            try:
                self.newEdits[2] = float(self.newEdits[2])
                self.newEdits[3] = float(self.newEdits[3])
                editVar = False
                self.top4.destroy()
            except(ValueError):
                tkinter.messagebox.showinfo('ValueError: Account Balance/Tax Paid', 'Only characters 0-9 and the decimal point "." may be used in these fields.')
                editVar = False
                break
        
class GetTotal(object):
    def __init__(self, master):
        top5 = self.top5 = Toplevel(master)
        self.headerFrame = Frame(top5)
        self.headerFrame.pack(side=TOP)
        self.currencyList = {"AED":"United Arab Emirates Dirham",
            "AFN":"Afghanistan Afghani",
            "ALL":"Albania Lek",
            "AMD":"Armenia Dram",
            "ANG":"Netherlands Antilles Guilder",
            "AOA":"Angola Kwanza",
            "ARS":"Argentina Peso",
            "AUD":"Australia Dollar",
            "AWG":"Aruba Guilder",
            "AZN":"Azerbaijan New Manat",
            "BAM":"Bosnia and Herzegovina Convertible Marka",
            "BBD":"Barbados Dollar",
            "BDT":"Bangladesh Taka",
            "BGN":"Bulgaria Lev",
            "BHD":"Bahrain Dinar",
            "BIF":"Burundi Franc",
            "BMD":"Bermuda Dollar",
            "BND":"Brunei Darussalam Dollar",
            "BOB":"Bolivia Boliviano",
            "BRL":"Brazil Real",
            "BSD":"Bahamas Dollar",
            "BTN":"Bhutan Ngultrum",
            "BWP":"Botswana Pula",
            "BYR":"Belarus Ruble",
            "BZD":"Belize Dollar",
            "CAD":"Canada Dollar",
            "CDF":"Congo/Kinshasa Franc",
            "CHF":"Switzerland Franc",
            "CLP":"Chile Peso",
            "CNY":"China Yuan Renminbi",
            "COP":"Colombia Peso",
            "CRC":"Costa Rica Colon",
            "CUC":"Cuba Convertible Peso",
            "CUP":"Cuba Peso",
            "CVE":"Cape Verde Escudo",
            "CZK":"Czech Republic Koruna",
            "DJF":"Djibouti Franc",
            "DKK":"Denmark Krone",
            "DOP":"Dominican Republic Peso",
            "DZD":"Algeria Dinar",
            "EGP":"Egypt Pound",
            "ERN":"Eritrea Nakfa",
            "ETB":"Ethiopia Birr",
            "EUR":"Euro Member Countries",
            "FJD":"Fiji Dollar",
            "FKP":"Falkland Islands (Malvinas) Pound",
            "GBP":"United Kingdom Pound",
            "GEL":"Georgia Lari",
            "GGP":"Guernsey Pound",
            "GHS":"Ghana Cedi",
            "GIP":"Gibraltar Pound",
            "GMD":"Gambia Dalasi",
            "GNF":"Guinea Franc",
            "GTQ":"Guatemala Quetzal",
            "GYD":"Guyana Dollar",
            "HKD":"Hong Kong Dollar",
            "HNL":"Honduras Lempira",
            "HRK":"Croatia Kuna",
            "HTG":"Haiti Gourde",
            "HUF":"Hungary Forint",
            "IDR":"Indonesia Rupiah",
            "ILS":"Israel Shekel",
            "IMP":"Isle of Man Pound",
            "INR":"India Rupee",
            "IQD":"Iraq Dinar",
            "IRR":"Iran Rial",
            "ISK":"Iceland Krona",
            "JEP":"Jersey Pound",
            "JMD":"Jamaica Dollar",
            "JOD":"Jordan Dinar",
            "JPY":"Japan Yen",
            "KES":"Kenya Shilling",
            "KGS":"Kyrgyzstan Som",
            "KHR":"Cambodia Riel",
            "KMF":"Comoros Franc",
            "KPW":"Korea (North) Won",
            "KRW":"Korea (South) Won",
            "KWD":"Kuwait Dinar",
            "KYD":"Cayman Islands Dollar",
            "KZT":"Kazakhstan Tenge",
            "LAK":"Laos Kip",
            "LBP":"Lebanon Pound",
            "LKR":"Sri Lanka Rupee",
            "LRD":"Liberia Dollar",
            "LSL":"Lesotho Loti",
            "LYD":"Libya Dinar",
            "MAD":"Morocco Dirham",
            "MDL":"Moldova Leu",
            "MGA":"Madagascar Ariary",
            "MKD":"Macedonia Denar",
            "MMK":"Myanmar (Burma) Kyat",
            "MNT":"Mongolia Tughrik",
            "MOP":"Macau Pataca",
            "MRO":"Mauritania Ouguiya",
            "MUR":"Mauritius Rupee",
            "MVR":"Maldives (Maldive Islands) Rufiyaa",
            "MWK":"Malawi Kwacha",
            "MXN":"Mexico Peso",
            "MYR":"Malaysia Ringgit",
            "MZN":"Mozambique Metical",
            "NAD":"Namibia Dollar",
            "NGN":"Nigeria Naira",
            "NIO":"Nicaragua Cordoba",
            "NOK":"Norway Krone",
            "NPR":"Nepal Rupee",
            "NZD":"New Zealand Dollar",
            "OMR":"Oman Rial",
            "PAB":"Panama Balboa",
            "PEN":"Peru Nuevo Sol",
            "PGK":"Papua New Guinea Kina",
            "PHP":"Philippines Peso",
            "PKR":"Pakistan Rupee",
            "PLN":"Poland Zloty",
            "PYG":"Paraguay Guarani",
            "QAR":"Qatar Riyal",
            "RON":"Romania New Leu",
            "RSD":"Serbia Dinar",
            "RUB":"Russia Ruble",
            "RWF":"Rwanda Franc",
            "SAR":"Saudi Arabia Riyal",
            "SBD":"Solomon Islands Dollar",
            "SCR":"Seychelles Rupee",
            "SDG":"Sudan Pound",
            "SEK":"Sweden Krona",
            "SGD":"Singapore Dollar",
            "SHP":"Saint Helena Pound",
            "SLL":"Sierra Leone Leone",
            "SOS":"Somalia Shilling",
            "SPL":"Seborga Luigino",
            "SRD":"Suriname Dollar",
            "STD":"Sao Tome and Principe Dobra",
            "SVC":"El Salvador Colon",
            "SYP":"Syria Pound",
            "SZL":"Swaziland Lilangeni",
            "THB":"Thailand Baht",
            "TJS":"Tajikistan Somoni",
            "TMT":"Turkmenistan Manat",
            "TND":"Tunisia Dinar",
            "TOP":"Tonga Pa'anga",
            "TRY":"Turkey Lira",
            "TTD":"Trinidad and Tobago Dollar",
            "TVD":"Tuvalu Dollar",
            "TWD":"Taiwan New Dollar",
            "TZS":"Tanzania Shilling",
            "UAH":"Ukraine Hryvnia",
            "UGX":"Uganda Shilling",
            "USD":"United States Dollar",
            "UYU":"Uruguay Peso",
            "UZS":"Uzbekistan Som",
            "VEF":"Venezuela Bolivar",
            "VND":"Viet Nam Dong",
            "VUV":"Vanuatu Vatu",
            "WST":"Samoa Tala",
            "XAF":"CommunautÇ Financiäre Africaine (BEAC) CFA Franc BEAC",
            "XCD":"East Caribbean Dollar",
            "XDR":"International Monetary Fund (IMF) Special Drawing Rights",
            "XOF":"CommunautÇ Financiäre Africaine (BCEAO) Franc",
            "XPF":"Comptoirs Franáais du Pacifique (CFP) Franc",
            "YER":"Yemen Rial",
            "ZAR":"South Africa Rand",
            "ZMW":"Zambia Kwacha",
            "ZWD":"Zimbabwe Dollar"}
        self.currencyList = OrderedDict(sorted(self.currencyList.items(), key=lambda t: t[0]))
        self.instructions = Label(self.headerFrame, bd=1, text="Get totals for Account Balance and Tax Paid.", relief=RAISED)
        self.instructions.pack()
        self.totFrame = Frame(top5)
        self.totFrame.pack(side=TOP)
        self.curChoice = Label(self.totFrame, text = "Currency to display total (pick one):")
        self.curChoice.grid(row = 0,column = 0, sticky = E)
        
        global b
        b = StringVar()

        self.mb = Menubutton(self.totFrame, textvariable=b, relief=RAISED, width=11)
        self.mb.grid(row = 0, column = 1)
        self.mb.menu  =  Menu(self.mb, tearoff = 0)
        self.mb["menu"]  =  self.mb.menu
        b.set("Select currency")

        for key in self.currencyList:
            self.mb.menu.add_checkbutton ( label="%s, (%s)" % (key,self.currencyList[key]),variable=key, command=partial(self.setValue,key))   # previously command=partial(self.total,key)

        self.menuChoice = b
        self.b3=Button(self.totFrame,text='Submit',command=lambda: self.total(self.menuChoice))
        '''if b=="Select currency":
            self.b3(state=DISABLED)
        elif b!="currencies":
            self.b3(state="normal")'''
        self.b3.grid(row=1,column=0, columnspan=2)

    def setValue(self, key):
        self.menuChoice = key
        b.set(self.menuChoice)

    def total(self, total):
        self.totaledCurrency = total
        self.total1 = db.getTotal(total)
        print(self.total1)
        self.top5.destroy()
        

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
        self.b2=Button(self.delFrameNew3,text='Submit',command=self.delCleanup)
        self.b2.pack()

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
        subMenu.add_command(label="Quit", command=self.quitProgram)

        self.editMenu = Menu(menu)
        editMenu = self.editMenu
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Edit Account...", command = self.editEntry)

        self.reportsMenu = Menu(menu)
        reportsMenu = self.reportsMenu
        menu.add_cascade(label="Reports", menu=reportsMenu)
        reportsMenu.add_command(label="Get monthly total", command=self.getTotals)

        # the toolbar
        self.toolbar = Frame(root, bg="light slate grey")
        toolbar = self.toolbar

        self.insertButt = Button(toolbar, text="Add New...", command=self.enterNew)
        insertButt = self.insertButt
        insertButt.pack(side=LEFT, padx=2,pady = 2)
        self.delButt = Button(toolbar, text="Delete Account", command=self.deleteValue)
        delButt = self.delButt
        delButt.pack(side=LEFT, padx=2,pady = 2)
        self.editButt = Button(toolbar, text="Edit Account", command=self.editEntry)
        editButt = self.editButt
        editButt.pack(side=LEFT, padx=2,pady = 2)

        toolbar.pack(side=TOP, fill=X)

        self.frame1 = Frame(root)
        frame1 = self.frame1

        # View database contents
        self.tree = ttk.Treeview(frame1)

        self.tree["columns"]=("one","two","three","four","five","six")
        self.tree.column("one", width=120)
        self.tree.column("two", width=200)
        self.tree.column("three", width=150)
        self.tree.column("four", width=100)
        self.tree.column("five", width=100)
        self.tree.column("six", width=100)
        self.tree.heading("one", text="Entry Date")
        self.tree.heading("two", text="Account Name")
        self.tree.heading("three", text="Account Balance")
        self.tree.heading("four", text="Tax paid")
        self.tree.heading("five", text="Default Currency")
        self.tree.heading("six", text="")

        '''tree.insert("" , 0, text="Line 1", values=("1A","1B","1C","1D","1E","1F"))  # Return values for db.readValue() method here.

        self.id2 = tree.insert("", 1, "dir2", text="Dir 2")                      # A directory, probably won't be needed for this unless previous months are listed here...
        tree.insert(self.id2, 3, text=" sub dir 2", values=(list(range(6))))'''

        self.tree.pack(fill=Y)

        frame1.pack(side=TOP)
        self.valuesTree()

    def enterNew(self):
        """Add new account"""
        self.ena = EnterNewWindow(self.master)  # Popup window with entry fields
        self.master.wait_window(self.ena.top)
        self.result = self.ena.value
        db.dataEntry(self.result[0],float(self.result[1]),float(self.result[2]),self.result[3])
        a.set("Entry %s succesfully added." % self.result[0])
        self.valuesTree()

    def getTotals(self):
        """Get total in chosen currency"""
        self.getCur = GetTotal(self.master)
        self.master.wait_window(self.getCur.top5)

    def deleteValue(self):
        """Delete account"""
        self.delAccount = DeleteAccount(self.master)
        self.master.wait_window(self.delAccount.top2)
        self.delRes = self.delAccount.deletedID
        db.deleteValue(self.delRes)
        a.set("Entry deleted.")
        self.valuesTree()

    def editEntry(self):
        """Edit the name, date, balance, and tax paid of an existing account"""
        self.editAccount = EditAccount(self.master)
        self.master.wait_window(self.editAccount.top3)
        try:
            self.editRes = int(self.editAccount.editedID)
            self.editList = db.editEntryValues(self.editRes)
            # self.editList[0] = re.sub('[\,\ ]','',', '.join(map(str, self.editList[0])))
            self.newEdit = EditFieldPrepopulate(self.master)
            self.master.wait_window(self.newEdit.top4)
            self.finalResult = self.newEdit.newEdits
            db.editEntry(self.finalResult, self.editRes)
            a.set("Edit saved")
            self.valuesTree()
        except(AttributeError):
            pass

    def valuesTree(self):
        """Display current database"""
        try:
            self.row = db.readValue()
            row = self.row
            self.tree.delete(*self.tree.get_children())
            print(row)
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
CFunc = db_handler.CurrencyFunctions()
a = StringVar()
m = mainWindow(root)
root.mainloop()
