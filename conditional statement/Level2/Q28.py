ch = input("Enter a character: ")

if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    print("Vowel")
elif ch >= "0" and ch <= "9":
    print("Digit")
else:
    print("Something else")