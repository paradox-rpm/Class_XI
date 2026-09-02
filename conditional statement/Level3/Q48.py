maths = int(input("Enter Mathematics marks: "))
physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
entrance = int(input("Enter entrance exam score: "))

total = maths + physics + chemistry

if (maths >= 60 and
    physics >= 50 and
    chemistry >= 50 and
    total >= 180 and
    entrance >= 70):

    if entrance >= 90:
        print("Eligible for Scholarship")
    else:
        print("Eligible for Admission")
else:
    print("Not Eligible")