units = int(input("Enter units consumed: "))
senior = input("Are you a senior citizen? (yes/no): ")

# Calculate basic bill
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

original_bill = bill

# Calculate surcharge
if bill > 3000:
    surcharge = bill * 5 / 100
    bill = bill + surcharge
else:
    surcharge = 0

# Calculate senior citizen discount
if senior == "yes":
    discount = bill * 10 / 100
    bill = bill - discount
else:
    discount = 0

print("Units consumed:", units)
print("Bill before adjustments: ₹", original_bill)
print("Surcharge: ₹", surcharge)
print("Discount: ₹", discount)
print("Final bill: ₹", bill)