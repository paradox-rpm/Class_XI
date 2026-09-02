num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
elif num % 2 == 0:
    print("Divisible only by 2")
elif num % 3 == 0:
    print("Divisible only by 3")
else:
    print("Divisible by neither")