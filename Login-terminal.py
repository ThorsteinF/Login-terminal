#Copyright 2020 thorsteinsoftware.com All right reserved

import os

userlist = []

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def main():
    options = input("Log in: 1\nSign up: 2\nList of users: 3\n>")  
    
    if options == "1":
        os.system("cls")
        login()
    elif options == "2":
        os.system("cls")
        signup()
    elif options == "3":
        os.system("cls")
        reveal_users()
    else:
        os.system("cls")
        main()

def login():
    username = input("Input your username: ")
    password = input("Input password for " + username + ": ")

    for i in range(len(userlist)):
        if userlist[i].username == username and userlist[i].password == password:
            os.system("cls")
            welcome(userlist[i].username)
            
    os.system("cls")
    print("Incorrect password or username.")
    main()

def signup():
    username = input("Create a username: ")
    password = input("Create a password: ")

    for i in range(len(userlist)):
        if userlist[i].username == username:
            os.system("cls")
            print("Username already in use.")
            main()
        elif userlist[i].password == password:
            os.system("cls")
            print("Password already in use.")
            main()

    userlist.append(User(username, password))
    os.system("cls")
    print("Account created.")
    main()

def welcome(username):
    print("Welcome,", username + ".")
    options = input("Type q to log out.\nType d to delete account\n>")

    if options == "q":
        os.system("cls")
        main()
    elif options == "d":
        os.system("cls")
        confirmation = input("Are you sure you want to delete you account?\nYes: 1\nNo: 2\n>")
        if confirmation == "1":
            os.system("cls")
            deleteuser(username)
        else:
            os.system("cls")
            welcome(username)
    else:
        os.system("cls")
        welcome(username)

def deleteuser(username):
    for i in range(len(userlist)):
        if userlist[i].username == username:
            del userlist[i]
            break

    print('Account "' + username + '" deleted.' )
    main()

def reveal_users():
    if len(userlist):
        for i in range(len(userlist)):
            pw_censored = ""
            print("User:", i+1)
            print("Username:", userlist[i].username)
            for j in range(len(userlist[i].password)):
                pw_censored+= "*"
            print("Password:", pw_censored)
            print()
    else:
        os.system("cls")
        input("There are no users. Press any key to return\n>")
        os.system("cls")
        main()

    input("Press any button to return\n>")
    os.system("cls")
    main()

os.system("cls")
print("Copyright \u00A9 2020 thorsteinsoftware.com All right reserved\n")
print("Welcome to the login terminal!")
main()