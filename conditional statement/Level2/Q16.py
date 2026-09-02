age = int(input("Enter your age: "))
has_id = input("Do you have a valid voter ID? ")

if age >= 18 and has_id == "yes":
    print("Eligible to vote")
else:
    print("Not eligible to vote")