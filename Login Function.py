username = ""
new_username = ""
password = ""
new_password = ""


def accountcreation():
    global new_username
    global new_password
    global username
    global password
    print("Welcome")
    new_username = input("What is your new username: ")
    fo = open(new_username, "w+")
    new_password = input("What is you new password: ")
    fo.write(new_username)
    fo.write(new_password)
    fo.close()


def accountlogin():
    global new_username
    global new_password
    login = input("Enter your username:")
    loginpass = input("Enter your password:")
    a = open(login, "r+")
    str = a.read(100)
    login = login + loginpass
    if login == str:
        print("Welcome")
    else:
        print("Wrong Password or Username.")


choice = input("Would you like to login or make a new account: ")
if choice == "login":
    accountlogin()
elif choice == "new account":
    accountcreation()
else:
    print("Error")
