username = input("Enter username: ")
password = input("Enter password: ")
status = input("Is the account active? (yes/no): ")

if username == "admin" and password == "1234":
    if status == "yes":
        print("Login Successful")
    else:
        print("Account Disabled")
else:
    print("Invalid Credentials")