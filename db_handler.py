#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite      # Using sqlite for now, port to mysql for improved security later
import sys
import datetime
import re

print(sys.version_info)

con = lite.connect('account_cv.db') # Connect to database

c = con.cursor()

month_list = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

date = datetime.datetime.now()
year = date.year
month = date.month
current_date = [month_list[month], year]



class Db(object):
    def __init__(self):
        d = 1
        self.con = con
        self.c = c
        pass


    def createTable(self):
        try:
            c.execute("CREATE TABLE Accounts_CV(ID INTEGER PRIMARY KEY NOT NULL, EntryDate TEXT, AccountName TEXT, Balance REAL);")
        except(lite.Error):
            pass                # Ignore table creation if it already exists.  Another (better) way might be to check if the table exists, if not, then create it.  But this works.


    def readValue(self):
        c.execute("SELECT * FROM Accounts_CV;")
        self.rows = c.fetchall()
        print("\nDatabse ID; Date in month and year (default = todays date); Account name; Current balance:\n")
        for row in self.rows:
            row = str(row)                          # Convert to string
            row = re.sub('[\(\"\[\'\]\)]', '', row) # Remove special characters from result
            print(row)
        

    def dataEntry(self):
        self.a = current_date
        self.b = input("Please enter account name: ")
        self.c = input("Please enter account balance: ")
        self.sql = "INSERT INTO Accounts_CV VALUES(NULL, ?, ?, ?);"
        c.execute(self.sql, (str(self.a), self.b, self.c))
        while True:
            self.commit = input("Would you like to save your data? ")
            if self.commit.upper() == 'Y' or self.commit.upper() == 'N':
                break
        if self.commit.upper() == 'Y':
                con.commit()
        self.readValue()


    def deleteValue(self):
        self.sql = "DELETE FROM Accounts_CV WHERE ID=?;"
        self.x = input("Enter Account ID to delete: ")
        c.execute(self.sql, (self.x))
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

            
    def editEntry(self):
        print("\n\n\nAccount details:\n")
        self.readValue()
        self.choices = {'1':2,'2':3,'3':1}
        self.columns = {1:'AccountName',2:'Balance',3:'EntryDate'}
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
                self.fetch = "SELECT * FROM Accounts_CV WHERE ID=?;"
                c.execute(self.fetch, (self.fieldtoedit))
                print(c.fetchone()[self.choices[self.fieldtoedit]])
                self.edited = input("Please enter new value: ")
                self.sql = "UPDATE Accounts_CV SET ?=? WHERE ID=?;"
                c.execute(self.sql, self.chosen, self.edited, self.chooseAccount)
                self.readValue()
                break
            break
            
