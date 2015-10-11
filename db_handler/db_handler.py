#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite      # Using sqlite for now, port to mysql for improved security later
import sys
import datetime
import re

# print(sys.version_info) # <-- used it once for diagnostic purposes, just leaving it in for now.

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


# Main database handling class.
class Db(object):
    def __init__(self):
        d = 1
        self.con = con
        self.c = c
        pass


    def createTable(self):
        try:
            c.execute("CREATE TABLE Accounts_CV(ID INTEGER PRIMARY KEY NOT NULL, EntryDate TEXT, AccountName TEXT, Balance REAL, DefaultCurrency TEXT, Total REAL DEFAULT NULL);")
        except(lite.Error):
            pass                # Ignore table creation if it already exists.  Another (better) way might be to check if the table exists, if not, then create it.  But this works.
        c.execute("CREATE TABLE IF NOT EXISTS Currency(ID INTEGER, Currency TEXT);") # This works better, and is apparently the proper way to do things.  This table will be referenced for currency conversions.


    def readValue(self):
        c.execute("SELECT * FROM Accounts_CV;")
        self.rows = c.fetchall()
        print("\nDatabse ID; Date in month and year (default = todays date); Account name; Current balance; Default currency\n")
        for row in self.rows:
            row = str(row)                          # Convert to string
            row = re.sub('[\(\"\[\'\]\)]', '', row) # Remove special characters from result
            print(row)

    def writeToCurrencyDb(self, name):
        self.name = name
        self.sql = "SELECT ID FROM Accounts_CV WHERE AccountName=?;"
        c.execute(self.sql, (self.name,))
        self.result = str(c.fetchone())
        self.result = re.sub('[\(\)\,]', '', self.result)
        print(self.result)
        self.result = int(float(self.result))
        print(self.result)
        return self.result
        

    def dataEntry(self):
        self.a = current_date
        self.b = input("Please enter account name: ")
        self.c = input("Please enter account balance: ")
        while True:
            self.d = input("Please enter default currency: ")
            self.d = self.d.upper()
            if self.d in currencyList:
                break
            else:
                # print("Invalid entry.  Please enter the ISO 4217 currency code (three letter abbreviation)").
                continue
        self.sql = "INSERT INTO Accounts_CV VALUES(NULL, ?, ?, ?, ?, NULL);"
        c.execute(self.sql, (str(self.a), self.b, self.c, self.d))
        c.execute("INSERT INTO Currency VALUES(?, ?);", (int(self.writeToCurrencyDb(self.b)), self.d))
        while True:
            self.commit = input("Would you like to save your data? ")
            if self.commit.upper() == 'Y' or self.commit.upper() == 'N':
                break
        # Store default currency in Currency table.
        if self.commit.upper() == 'Y':
            con.commit()
        self.readValue()


    def deleteValue(self):
        self.sql = "DELETE FROM Accounts_CV WHERE ID=?;"
        self.x = input("Enter Account ID to delete: ")
        c.execute(self.sql, (self.x,))
        con.commit()
        self.readValue()

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

    def addColumn(self):    # Now added to the default table creation
        c.execute("ALTER TABLE Accounts_CV ADD COLUMN 'Total' REAL DEFAULT NULL;")

    def getTotal(self):
        c.execute("SELECT ID, EntryDate, AccountName, Balance, DefaultCurrency, (SELECT SUM(Balance) FROM Accounts_CV) Total FROM Accounts_CV;")
        self.total = c.fetchone()
        print("\n\nTotal =",self.total[5],self.total[4],"\n")
            
    def editEntry(self):
        print("\n\n\nAccount details:\n")
        self.readValue()
        self.choices = {'1':2,'2':3,'3':1}
        self.columns = {1:'AccountName',2:'Balance',3:'EntryDate'}
        self.editDate = []
        self.monthValue = True
        while True:
            self.chooseAccount = input("\nPlease enter account ID to edit; type exit to cancel: \n")
            self.isEqual = False
            c.execute("SELECT ID FROM Accounts_CV;")
            self.acct_id = c.fetchall()
            for i in self.acct_id:
                # print(self.isEqual)
                i = int(re.sub('[\,\(\)]','',str(i)))
                # print(i)
                if self.chooseAccount == str(i):
                    self.isEqual = True
                    self.chooseAccount == int(self.chooseAccount)
                    # print(self.isEqual)
                    break
                elif self.chooseAccount.upper() == 'EXIT':
                    break
                else:
                    continue
            if self.isEqual == True:
                print("\n\n\n     ***************************************\n     **                                   **\n     ** Please select field to edit:      **\n     **                                   **\n     ** 1. Account name.                  **\n     ** 2. Account balance.               **\n     ** 3. Entry date.                    **\n     ** 4. Exit.                          **\n     **                                   **\n     ***************************************\n")
                self.fieldtoedit = input("Please make an entry from 1-4: ")
                self.chosen = self.columns[int(self.fieldtoedit)]
                self.fetch = "SELECT * FROM Accounts_CV WHERE ID=?;"  #  <-- Aha!!!!  It's all wrong here...  It's asking for the ID while the input refers to the column heading.
                c.execute(self.fetch, (self.chooseAccount,))
                self.gathered = c.fetchone()[self.choices[self.fieldtoedit]]
                print(self.gathered)
                #
                #
                #  vvvv The bit below is the logic to get the formatting of the date correct vvvv
                #
                #
                if self.chosen == 'EntryDate':
                    for j in month_list:
                        print(j, month_list[j])
                    # Enter month and year, check for inconsistencies
                    while self.monthValue == True:
                        self.editDate.append(input("Please enter the numeric value of the month from 1-12: "))
                        print(month_list[int(self.editDate[0])])
                        for k in list(range(1,13)):
                            # print(k)
                            if int(k) == int(self.editDate[0]):
                                self.monthValue = False
                                self.editDate[0] = month_list[k]
                                break
                            else:
                                continue
                    while True:
                        self.editDate.append(input("Please enter the 4-digit year: "))
                        if len(list(str(self.editDate[1]))) == 4 and int(self.editDate[1]) <= year:
                            break
                        else:
                            del self.editDate[-1]    # Remove appended 
                            continue
                    self.editDate = str(self.editDate)
                    self.edited = re.sub('[\[\]\']','',self.editDate)
                else:
                    self.edited = input("Please enter new value: ")
                #
                # ^^^^ The above input is for all other data types besides date ^^^^
                #
                self.sql = "UPDATE Accounts_CV SET %s=? WHERE ID=?;" % (self.chosen)
                c.execute(self.sql, (self.edited, self.chooseAccount,))
                con.commit()
                self.readValue()
                break
            break
            
