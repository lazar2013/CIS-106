#input phase
item = input("Do you have item A or item B?")
quantity = int(input("Enter the quantity of the item"))

#process phase
if item == "A":
    unitprice = 10.00
else:
    unitprice = 20.00

extendedprice = quantity * unitprice

#output phase
print("Item:",item)
print("Unit price: $",format(unitprice, ".2f"))
print("Extended price: $",format(extendedprice, ".2f"))

#pause so window stays open
input("\nPress Enter to exit")