marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))

if marks >= 40 and attendance >= 75:
    print("Eligible for exam")
else:
    print("Not eligible for exam")