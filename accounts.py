#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite      # Using sqlite for now, port to mysql for improved security later
import sys
import datetime

connect = lite.connect('account_db.db') # Connect to database

current = connect.cursor()


# If the table already exists, which it does by now, the next line will be ignored
try:
    current.execute("CREATE TABLE Accounts(Month TEXT, Account TEXT, Balance REAL)")

except(lite.Error):
    pass            # Ignore the table creation


# Insert data into the database, save prompt.
def insert_value(a, b, c):
    sql = "INSERT INTO Accounts VALUES(?, ?, ?);"
    current.execute(sql, (str(a), b, c))
    while True:
        commit = input("Would you like to save your data? ")
        if commit.upper() == 'Y' or commit.upper() == 'N':
            break
    if commit == "y" or commit == "Y":
        connect.commit()


# Read from the database.  Functions should be combined into a class, possibly called database.
def read_value():
    current.execute("SELECT * FROM Accounts;")
    rows = current.fetchall()
    for row in rows:
        print(row)

# Delete a row.  Need to work on this.
def delete_value():
    sql = "DELETE FROM Accounts WHERE Account=?;"
    x = input("Enter account name to delete: ")
    current.execute(sql, (x,))
    connect.commit()

month_list = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

date = datetime.datetime.now()
year = date.year
month = date.month
current_date = [month_list[month], year]


account_name = input("Please enter the name of the account: ")
account_balance = input("Please enter the current account balance: ")

insert_value(current_date,account_name,account_balance)

read_value()        # need to remove quotes around string values


# testing the delete value function which doesn't work yet
while True:
    del_opt = input("Would you like to delete a table (y/n)? ")
    if del_opt.upper() == "Y":
        delete_value()
        break
    elif del_opt.upper() == "N":
        break
    else:
        continue
