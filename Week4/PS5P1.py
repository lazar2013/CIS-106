#input phase
widgetsqty = int(input("Quantity of widgets"))

#process phase
if widgetsqty > 10000:
    price = 10
elif widgetsqty >= 5000 and widgetsqty <= 10000:
    price = 20
elif widgetsqty < 5000:
    price = 30

extendedprice = widgetsqty * price
taxamount = extendedprice * 0.07
total = extendedprice + taxamount

#output phase
print("Extended price: ${:,.2f}".format(extendedprice))
print("Tax amount:     ${:,.2f}".format(taxamount))
print("Total:          ${:,.2f}".format(total))

#pause so window stays open
input("\nPress Enter to exit")