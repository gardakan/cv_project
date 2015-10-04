#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite      # Using sqlite for now, port to mysql for improved security later
import sys
import datetime

print(sys.version_info)

connect = lite.connect('account_db.db') # Connect to database

current = connect.cursor()

month_list = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

date = datetime.datetime.now()
year = date.year
month = date.month
current_date = [month_list[month], year]

# If the table already exists, which it does by now, the next line will be ignored
try:
    current.execute("CREATE TABLE Accounts(Month TEXT, Account TEXT, Balance REAL)")

except(lite.Error):
    pass            # Ignore the table creation

# Database class with methods to insert and delete rows, return 
class db(object):
    def __init__(self, table_name):
        self.table_name = table_name   # <--- this was there and I can't remember why!

    def read_value(self):
        current.execute("SELECT * FROM Accounts;")
        self.rows = current.fetchall()
        self.output = []
        for row in self.rows:
            '''self.output.append(row)
            return(self.output)'''
            print(row)

    def insert_value(self):
        self.a = current_date
        self.b = input("Please enter account name: ")
        self.c = input("Please enter account balance: ")
        self.sql = None
        self.sql = "INSERT INTO Accounts VALUES(?, ?, ?);"
        current.execute(self.sql, (str(self.a), self.b, self.c))
        while True:
            self.commit = input("Would you like to save your data? ")
            if self.commit.upper() == 'Y' or self.commit.upper() == 'N':
                break
        if self.commit.upper() == 'Y':
                connect.commit()
        self.read_value()

    def delete_value(self):
        self.sql = "DELETE FROM Accounts WHERE Account=?;"
        self.x = input("Enter account name to delete: ")  # Eventually populate dropdown
        current.execute(self.sql, (self.x,))
        connect.commit()
        self.read_value()

    def delete_row(self):
        while True:
            del_opt = input("Would you like to delete a table (y/n)? ")
            if del_opt.upper() == "Y":
                self.delete_value()
                break
            elif del_opt.upper() == "N":
                break
            else:
                continue

tab = None
inst = db(tab)

while True:
    print("\n\n\n     ***************************************\n     **                                   **\n     ** Please select from the following: **\n     **                                   **\n     ** 1. Add entry.                     **\n     ** 2. Delete entry.                  **\n     ** 3. Show accounts.                 **\n     ** 4. Exit.                          **\n     **                                   **\n     ***************************************\n")
    while True:
        choice = input("Make your choice: ")
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            break
        else:
            print("Invalid command.  Only numeric values between 1-4 inclusive allowed.\n")
    if choice == "1":
        inst.insert_value()
    elif choice == "2":
        inst.delete_row()
    elif choice == "3":
        inst.read_value()
    elif choice == "4":
        print("\nGoodbye!\n")
        break
