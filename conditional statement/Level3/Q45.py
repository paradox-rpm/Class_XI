age = int(input("Enter age: "))
percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance percentage: "))

if age >= 17 and percentage >= 60 and attendance >= 75:
    if percentage >= 90:
        print("Eligible - Scholarship Consideration")
    else:
        print("Eligible")
else:
    print("Not Eligible")