name = input("Student Name: ")
m1 = float(input("Sub 1: "))
m2 = float(input("Sub 2: "))
m3 = float(input("Sub 3: "))
m4 = float(input("Sub 4: "))
m5 = float(input("Sub 5: "))
total = m1 + m2 + m3 + m4 + m5
avg = total / 5
per = (total / 500) * 100
hi = max(m1, m2, m3, m4, m5)
lo = min(m1, m2, m3, m4, m5)
print(f"Student: {name}")
print("Total:", total)
print("Average:", avg)
print("Percentage:", per)
print("Highest Possible Total: 500")
print("Percentage of Total:", per)
print("Diff between Highest and Lowest:", hi - lo)
