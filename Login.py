name = input("Enter Your New name:")
fo = open(name, "w+")
password = input("Enter Your New password:")
fo.write(name)
fo.write(password)
fo.close()
a = open(name, "r+")
str = a.read(100)
login = input("Enter your username:")
loginpass = input("Enter your password:")
login = login + loginpass
if login == str:
    print("Welcome")
else:
    print("error")

