amount = float(input("Enter shopping amount: "))

if amount >= 5000:
    discount = amount * 20 / 100
elif amount >= 2000:
    discount = amount * 10 / 100
else:
    discount = 0

final_amount = amount - discount

print("Discount:", discount)
print("Final amount:", final_amount)