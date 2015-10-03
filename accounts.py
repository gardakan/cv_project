#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import datetime

connect = lite.connect('account_db.db')

current = connect.cursor()

try:
    current.execute("CREATE TABLE Accounts(Month TEXT, Account TEXT, Balance REAL)")

except(lite.Error):
    pass

def insert_value(a, b, c):
    sql = "INSERT INTO Accounts VALUES(?, ?, ?);"
    current.execute(sql, (str(a), b, c))

def read_value():
    current.execute("SELECT * FROM Accounts;")
    rows = current.fetchall()
    for row in rows:
        print(row)

month_list = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

date = datetime.datetime.now()
year = date.year
month = date.month
current_date = [month_list[month], year]


account_name = input("Please enter the name of the account: ")
account_balance = input("Please enter the current account balance: ")

insert_value(current_date,account_name,account_balance)

read_value()        # need to remove quotes around string values
