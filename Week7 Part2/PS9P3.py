def CompPrice(make,model,electric,msrp):
    if make == "Honda" and model == "Accord":
        msrpPercent = 0.10
    elif make == "Toyota" and model == "Rav4":
        msrpPercent = 0.15
    elif electric == "yes":
        msrpPercent = 0.30
    else: 
        msrpPercent = 0.05

    amtoff = msrp * msrpPercent
    newmsrp = msrp - amtoff
    tax = newmsrp * 0.07
    total = newmsrp + tax
    return total

totaloldmsrp = 0
totalsellprice = 0

r = input("Do you want to compute the MSRP (yes or no)?")
while r == "yes":
    make = input("Enter make of car:")
    model = input("Enter model:")
    electric = input("Is car electric (yes or no)?")
    msrp = float(input("Enter MSRP:"))

    total = CompPrice(make,model,electric,msrp)
    print(f"Total owed: ${total:,.2f}")

    totaloldmsrp = totaloldmsrp + msrp
    totalsellprice = totalsellprice + total 

    r = input("Do you want to compute the MSRP (yes or no)?")

print("Sum of all MSRPs: $", totaloldmsrp)
print("Sum of all sales prices: $", totalsellprice)