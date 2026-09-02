num = int(input("Enter a number: "))

if (num >= 10 and num <= 99) or (num <= -10 and num >= -99):
    print("Two-digit number")
else:
    print("Not a two-digit number")