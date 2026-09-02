age = int(input("Enter age: "))
day = input("Enter day (weekday/weekend): ")
student = input("Are you a student? (yes/no): ")

if age < 5:
    price = 0
elif age <= 17:
    price = 100
else:
    price = 150

if price > 0:
    if day == "weekend":
        price = price + 50

    if student == "yes":
        price = price - (price * 20 / 100)

print("Final ticket price: ₹", price)