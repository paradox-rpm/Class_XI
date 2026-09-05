price = float(input("Product Price: "))
qty = int(input("Quantity: "))
disc = float(input("Discount %: "))
gst = float(input("GST %: "))
subtotal = price * qty
after_disc = subtotal - (subtotal * disc / 100)
final_bill = after_disc + (after_disc * gst / 100)
print("Final Bill Amount:", final_bill)
