marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60:
    if age >= 17:
        print("Eligible for admission")
    else:
        print("Not eligible: Age requirement not satisfied")
else:
    print("Not eligible: Marks requirement not satisfied")