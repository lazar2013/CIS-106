def CompExtPrice(qty, unitprice):
    extprice = qty * unitprice

    if extprice > 10000.00:
        discountamt = extprice * 0.10
    else:
        discountamt = 0.0

    return extprice

totalExtPrice = 0.0
r = input("Do you want to compute extended price (yes or no)?")

while r == "yes":
    qty = float(input("Enter quantity: "))
    unitprice = float(input("Enter unit price: "))
    extprice = CompExtPrice(qty, unitprice)
    print("Extended Price is $:",extprice)
    totalExtPrice = totalExtPrice + extprice
    r = input("Do you want to compute extended price (yes or no)?")

    print("Total Extended Price is $:", totalExtPrice)