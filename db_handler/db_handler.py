#!/usr/bin/python

import sqlite3 as lite      
import sys
import datetime
import re
from tkinter import *
import tkinter.messagebox
import requests

__author__ = "John Tamm-Buckle"
__credits__ = "John Tamm-Buckle"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "John Tamm-Buckle"
__email__ = "jtammbuckle@gmail.com"
__status__ = "Development"

con = lite.connect('account_cv.db') # Connect to database

c = con.cursor()

month_list = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

date = datetime.datetime.now()
year = date.year
month = date.month
current_date = [month_list[month], year]

currencyList = {"AED":"United Arab Emirates Dirham",
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

# Currency conversion class
class CurrencyFunctions(object):

    def __init__(self):
        pass

    # Iterate over the available currencies (not all of which are supported, IndexError may be thrown).
    def showCurrencies(self):
        self.a = sorted(currencyList.keys())
        print("Available currencies:")
        for i in a:
            print(i,currencyList[i])

    # Method for entering currency by ISO 4217 standards.  Not all official standards are supported by the conversion API's, and IndexError is thrown in such cases.
    def getCurrency(self):
        self.x = input("Please enter ISO 4217 currency code for the amount to enter, or type 'list' to see a list of available choices: ")
        if self.x.upper() == "LIST":
            self.showCurrencies()
            return self.getCurrency()
        elif self.x.upper() in currencyList:
            return self.x.upper()
        else:
            print("Invalid entry; ")
            return self.getCurrency()

    # Currency conversion method
    def enterConvert(self, entered, converted, cValue):
        self.entered = entered
        self.converted = converted
        self.cValue = cValue

        self.url = ('https://currency-api.appspot.com/api/%s/%s.json') % (self.entered,self.converted)
        print("Getting exchange rate for %s to %s from: %s." % (self.entered, self.converted, self.url))

        r = requests.get(self.url)

        print("Current exchange rate: ", r.json()['rate'])
        print("Account value in %s: %f" % (self.entered, self.cValue*float(r.json()['rate'])))

        try:   # Watch for exceptions
            self.urlalt = ('http://themoneyconverter.com/%s/%s.aspx') % (self.entered,self.converted)
            print("Secondary conversion rates from %s." % (self.urlalt))

            # split and strip
            self.split1 = ('>%s/%s =') % (self.converted, self.entered)
            self.strip1 = ('</textarea>')

            self.ralt = requests.get(self.urlalt)
            self.d = float(self.ralt.text.split(self.split1)[1].split(self.strip1)[0].strip())
            print("Current exchange rate: ", self.d)

            print("Account value in %s: %f" % (self.entered, (self.cValue * self.d)))
            return (self.cValue * self.d)
        
        except(IndexError):
            print("Unsupported currency.  Please try again. ")
            pass
        
        

CFunc = CurrencyFunctions() # Instantiate the CurrencyFunctions class

# Main database handling class.
class Db(object):
    def __init__(self):
        d = 1
        self.con = con
        self.c = c
        self.createTable()
        
        pass

    # Create the tables if they don't already exist.
    def createTable(self):
        try:
            c.execute("CREATE TABLE Accounts_CV(ID INTEGER PRIMARY KEY NOT NULL, EntryDate TEXT, AccountName TEXT, Balance REAL, TaxPaid REAL, DefaultCurrency TEXT, Total REAL DEFAULT NULL);")
        except(lite.Error):
            pass                # Ignore table creation if it already exists.  Another (better) way might be to check if the table exists, if not, then create it.  But this works.
        c.execute("CREATE TABLE IF NOT EXISTS Currency(ID INTEGER, Currency TEXT);") # This works better, and is apparently the proper way to do things.  This table will be referenced for currency conversions.
        # c.execute("CREATE TABLE IF NOT EXISTS DateTime(ID INTEGER, EntryDate TEXT, Balance REAL);")

    # Iterates over the Accounts_CV table and outputs all account info
    def readValue(self):
        self.allRows = []
        c.execute("SELECT * FROM Accounts_CV;")
        self.rows = c.fetchall()
        # print("\nDatabase ID; Date in month and year (default = todays date); Account name; Current balance; Default currency\n")
        for row in self.rows:
            row = str(row)                          # Convert to string
            row = re.sub('[\(\"\[\'\]\)\,]', '', row) # Remove special characters from result
            row = row.split()
            row[1:3] = [' '.join(row[1:3])]
            self.allRows.append(row)
        return self.allRows             # Returns all values

    # Method for getting the primary key ID of an account.
    def writeToCurrencyDb(self, name):
        self.name = name
        self.sql = "SELECT ID FROM Accounts_CV WHERE AccountName=?;"
        c.execute(self.sql, (self.name,))
        self.result = str(c.fetchone())
        self.result = re.sub('[\(\)\,]', '', self.result)
        self.result = int(float(self.result))
        return self.result

    # Method for adding new accounts.
    def dataEntry(self, b, x, e, d):
        self.b = b  # account name
        self.c = x  # account balance
        self.d = d  # default currency
        self.e = e  # tax paid
        self.a = current_date
        while True:
            self.d = self.d.upper()
            if self.d in currencyList:
                break
            else:
                continue
        self.sql = "INSERT INTO Accounts_CV VALUES(NULL, ?, ?, ?, ?, ?, NULL);"
        c.execute(self.sql, (str(self.a), self.b, self.c, self.e, self.d))
        print("Executed")
        c.execute("INSERT INTO Currency VALUES(?, ?);", (int(self.writeToCurrencyDb(self.b)), self.d)) # Store currency in separate table for conversion purposes
        '''while True:
            self.commit = tkinter.messagebox.askquestion('Commit Values', 'Would you like to save your data?')
            
        # Store default currency in Currency table.
        if self.commit == 'yes':'''
        con.commit()
        print("\n\nCommitted.\n\n")
        self.readValue()

    # Method used by deleteRow, should ideally be combined into one method.  This method does the actual SQL deletion.
    def deleteValue(self, y):
        self.sql = "DELETE FROM Accounts_CV WHERE ID=?;"
        self.x = y
        if y == 'cancel':
            pass
        else:
            c.execute(self.sql, (self.x,))
            con.commit()
            self.readValue()

    # Delete an account
    def deleteRow(self):
        while True:
            del_opt = input("Would you like to delete an entry (y/n)? ")
            if del_opt.upper() == "Y":
                self.deleteValue()
                break
            elif del_opt.upper() =="N":
                break
            else:
                continue

    # Method to get the total balance of all accounts in given currency
    def getTotal(self, choice):
        """Check current exchange rates and convert current account balance to chosen currency, and display the total"""

        self.totalCurrency = choice
        self.totalCurrency = self.totalCurrency.upper()

        c.execute("SELECT DefaultCurrency FROM Accounts_CV;")
        self.currencies = c.fetchall()
        self.totalList = []
        self.cValue = []
        for i in range(len(self.currencies)):
            for rowVal in c.execute("SELECT Balance FROM Accounts_CV;"):
                self.cValue.append(re.sub('[\(\)\,\']', '', str(rowVal)))
            self.currencies[i] = re.sub('[\(\)\,\']', '', str(self.currencies[i]))
            
            # Call on enterConvert
            self.statusmessage = ("Converting from %s to %s with an account balance of %f. " % (self.currencies[i], self.totalCurrency, float(self.cValue[i])))
            self.totalList.append(CFunc.enterConvert(self.currencies[i], self.totalCurrency, float(self.cValue[i])))
        for j in range(len(self.totalList)):
            try:
                self.totalList[j] = float(self.totalList[j])
            except(TypeError):
                self.statusmessage = ("\n\nUnable to get total in selected currency.  Please try again.\n")
                break
        try:
            self.statusmessage = ("\n\nTotal = :", sum(self.totalList), self.totalCurrency, "\n")
        except(TypeError):
            pass
        finally:
            return sum(self.totalList), self.totalCurrency

    def editEntryValues(self, z):
        c.execute("SELECT EntryDate, AccountName, Balance, TaxPaid FROM Accounts_CV WHERE ID=?;", (z,))
        self.editResult = c.fetchone()
        return self.editResult

    def editEntry(self, editedFields, acctID):
        '''print("\n\n\nAccount details:\n")
        self.readValue()
        self.choices = {'1':2,'2':3,'3':1,'4':4}
        self.columns = {1:'AccountName',2:'Balance',0:'EntryDate',3:'TaxPaid'}'''
        self.individualItems = {}
        self.k = 0

        # Start of edit prompt:

        for self.k in range(len(editedFields)):
            key = self.k
            self.individualItems[self.k] = editedFields[self.k]
            self.k+=1

        print(self.individualItems[0][0])
        self.individualItems[0] = re.sub('[\[\]\']','',str(self.individualItems[0]))
        self.sqlEdit = "UPDATE Accounts_CV SET EntryDate=?, AccountName=?, Balance=?, TaxPaid=? WHERE ID=?;"
        c.execute(self.sqlEdit, (self.individualItems[0],self.individualItems[1],self.individualItems[2],self.individualItems[3],acctID,))
        con.commit()

    def dateCheck(self, dateTime):
        dateTime = re.sub('[\[\]\'\,]','',dateTime)
        dateTime = dateTime.split()
        self.editDate = ""
        self.monthValue = True
        for k in list(range(1,13)):
            try:
                if k == int(dateTime[0]) and len(list(str(dateTime[1]))) == 4 and len(dateTime) == 2:
                    self.editDate = month_list[k]
                    return self.editDate
            except(ValueError):
                continue
        for l in list(range(1,13)):
            if dateTime[0].upper() == month_list[l].upper():
                self.editDate = dateTime[0]
                return self.editDate
        return "error"
