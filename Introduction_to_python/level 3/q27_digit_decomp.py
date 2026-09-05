n = int(input("Enter a three-digit number: "))
h = n // 100
t = (n // 10) % 10
u = n % 10
print("Hundreds:", h, "Tens:", t, "Units:", u)
print("Sum:", h + t + u)
print("Product:", h * t * u)
