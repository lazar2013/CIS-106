def discount(qty,price,discrate):
    total = qty * price
    discamt = discrate * total
    discprice = total - discamt 

    return discamt, discprice

qty = float(input("Enter quantity:"))
price = float(input("Enter unit price: $"))
discrate = float(input("Enter the discount rate:"))
discamt,discprice = discount(qty,price,discrate)

print("Quantity:")
print("Unit Price: $", format(float(price), '10,.2f'))
print("Discount amount: $", format(float(discamt), '10,.2f'))
print("Discounted price: $", format(float(discprice), '10,.2f'))