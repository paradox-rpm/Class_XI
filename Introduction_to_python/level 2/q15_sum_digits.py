n = int(input("Enter a three-digit number: "))
print("Sum of digits:", (n // 100) + ((n // 10) % 10) + (n % 10))
