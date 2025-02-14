print("Please enter your user and password below to login")

user = input("Enter Username here: ")
password = input("Enter Password here: ")

if user == "admin" and password == 1234:
    print("Access Granted")
else:
    print("Access Denied")