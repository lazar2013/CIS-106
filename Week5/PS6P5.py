#Before the loop - set the sum of all of the discounts to 0
sumdiscount = 0

#Ask the user if they want to run the program
r = input("Do you want to run this program (Yes or No)?")

#In the loop - 
while(r == "Yes"):
    quantity = int(input("Enter the quantity of the item you want to purchase:"))
    price = float(input("Enter the price of the item you want to purchase: $"))
    extendedprice = quantity * price

    #determine if the user will receive 25% off or 10% off
    if extendedprice > 10000.00: 
        discount = 0.25
    else:
        discount = 0.10

    #calculate the discount amount and the order total
    discountamount = extendedprice * discount
    total = extendedprice - discountamount 

    #display extended price, discount amount, and the total
    print("Extended price: ${:,.2f}".format(extendedprice, ".2f"))
    print("Discount amount: ${:,.2f}".format(discountamount, ".2f"))
    print("Order total: ${:,.2f}".format(total, ".2f"))

    sumdiscount = sumdiscount + discountamount

    r = input("Do you want to run this program (Yes or No)?")

#After the loop - display the sum of all the discounts 
print("Sum of all the discounts: ${:,.2f}".format(sumdiscount, ".2f"))

#Pause so the window stays open 
input("\nPress Enter to exit")