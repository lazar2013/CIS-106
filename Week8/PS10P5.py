total = 0.0
tax = 0.0
def comptotal(qty,price):
    global total
    total = qty * price
    global tax
    tax = total * 0.07
    
qty = float(input("Item quantity:"))
price = float(input("Unit Price: $"))
comptotal(qty,price)
    
print("Total: $", format(float(total), '10,.2f'))
print("Tax: $", format(float(tax), '10,.2f'))