#input phase
partnumber = int(input("Enter the part number"))
qty = input("Enter the quantity to purchase")

#process phase 
if partnumber == 10 or partnumber == 55:
    unitprice = 1.00
elif partnumber == 99:
    unitprice == 2.00
elif partnumber == 70 or partnumber == 80:
    unitprice = 3.00
else:
    unitprice = 5.00

total = float(qty) * unitprice

#output phase
print("Part number:  ",partnumber)
print("Unit price:   ",unitprice)
print("Total:        ",total)

#pause so window stays open
input("\nPress Enter to exit")