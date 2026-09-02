pin = int(input("Enter PIN: "))

if pin == 1234:
    balance = float(input("Enter available balance: "))
    amount = float(input("Enter withdrawal amount: "))

    if amount <= balance:
        print("Withdrawal successful")
        print("Remaining balance:", balance - amount)
    else:
        print("Insufficient balance")
else:
    print("Incorrect PIN")