hour = int(input("Enter current hour (0-23): "))

if hour >= 5 and hour <= 11:
    print("Good Morning")
elif hour >= 12 and hour <= 16:
    print("Good Afternoon")
elif hour >= 17 and hour <= 20:
    print("Good Evening")
else:
    print("Good Night")