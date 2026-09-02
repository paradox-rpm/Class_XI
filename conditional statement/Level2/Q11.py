a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    print("Smaller number:", a)
elif b < a:
    print("Smaller number:", b)
else:
    print("Both numbers are equal")