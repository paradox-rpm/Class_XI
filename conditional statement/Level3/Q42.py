a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a >= b and a <= c) or (a >= c and a <= b):
    print("Middle value:", a)
elif (b >= a and b <= c) or (b >= c and b <= a):
    print("Middle value:", b)
else:
    print("Middle value:", c)