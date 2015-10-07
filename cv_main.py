import db_handler       # Contains class Db with all the database functions

db = db_handler.Db()    # Class Db() now referenced as db

db.createTable()        # Calls on createTable method, creates table Accounts_CV, unless it already exists.  Throws exception in this case



#  Main loop of the application
def mainLoop():
    while True:
        print("\n\n\n     ***************************************\n     **                                   **\n     ** Please select from the following: **\n     **                                   **\n     ** 1. Add entry.                     **\n     ** 2. Delete entry.                  **\n     ** 3. Edit entry.                    **\n     ** 4. Show accounts.                 **\n     ** 5. Get total.                     **\n     ** 6. Exit.                          **\n     **                                   **\n     ***************************************\n")
        while True:
            choice = input("Make your choice: ")
            if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6":
                break
            else:
                print("Invalid command.  Only numeric values between 1-6 inclusive allowed.\n")
        if choice == "1":       # if-elif block contains cases for methods to enter new data, check current data, delete an entry, and exit the application.
            db.dataEntry()
        elif choice == "2":
            db.deleteRow()
        elif choice == "3":
            db.editEntry()
        elif choice == "4":
            db.readValue()
        elif choice == "5":
            db.getTotal()
        elif choice == "6":
            while True:
                save = input("Save changes (y/n)? ")
                if save.upper() == "Y":
                    db.con.commit()
                    print("Changes saved.")
                    db.con.close()
                    print("\nGoodbye!\n")
                    break
                elif save.upper() == "N":
                    db.con.close()
                    print("\nGoodbye!\n")
                    break
            break

mainLoop()
