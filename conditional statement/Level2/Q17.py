age = int(input("Enter your age: "))
citizenship = input("Enter your citizenship: ")

if age >= 18 and citizenship == "Indian":
    print("Eligible to vote")
else:
    print("Not eligible to vote")