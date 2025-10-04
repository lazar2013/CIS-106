#input phase
books = int(input("Enter the number of books to order"))
cost = float(input("Enter the cost per book"))

#process phase
total = books * cost
if total > 50.00:
    shipping = 0.00
else:
    shipping = 25.00
ordertotal = total + shipping

#output phase
print("Total cost for books $",format(total, ".2f"))
print("Total cost for shipping $",format(shipping, ".2f"))
print("The order total is $",format(ordertotal, ".2f"))

#pause so window stays open
input("\nPress Enter to exit")