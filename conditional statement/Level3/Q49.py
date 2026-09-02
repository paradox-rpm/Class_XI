length = int(input("Enter password length: "))

digit = input("Contains a digit? (yes/no): ")
uppercase = input("Contains an uppercase letter? (yes/no): ")
special = input("Contains a special character? (yes/no): ")

if length >= 8 and digit == "yes" and uppercase == "yes" and special == "yes":
    print("Strong Password")

elif length >= 8:
    if digit == "yes" and uppercase == "yes":
        print("Medium Password")
    elif digit == "yes" and special == "yes":
        print("Medium Password")
    elif uppercase == "yes" and special == "yes":
        print("Medium Password")
    else:
        print("Weak Password")
else:
    print("Weak Password")