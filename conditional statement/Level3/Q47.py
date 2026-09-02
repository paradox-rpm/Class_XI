age = int(input("Enter age: "))
income = float(input("Enter monthly income: ₹"))
credit_score = int(input("Enter credit score: "))

if age >= 21 and age <= 60 and income >= 30000 and credit_score >= 700:
    if credit_score >= 800:
        print("Premium Loan Eligible")
    else:
        print("Loan Eligible")
else:
    print("Loan Not Eligible")