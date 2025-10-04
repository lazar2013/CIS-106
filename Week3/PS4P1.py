#input phase
quantity = int(input("Enter the quantity of an item"))

#process phase
if quantity >= 1000:
    unitprice = 3.00
else:
    unitprice = 5.00

extendedprice = quantity * unitprice
tax = extendedprice * 0.07
total = extendedprice + tax

#output phase
print("Item quantity",quantity)
print("The price per unit is $",format(unitprice, ".2f"))
print("The extended price is $",format(extendedprice, ".2f"))
print("The tax amount is $",format(tax, ".2f"))
print("The total price is $",format(total, ".2f"))

#pause so window stays open
input("\nPress Enter to exit")