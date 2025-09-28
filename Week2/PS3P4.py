#input phase
make = input("Enter the make of the car")
model = input("Enter the model of the car")
msrpamt = float(input("Enter the MSRP amount"))
discountpercent = float(input("Enter the discount percent of the car as a decimal"))

#process phase
amtoff = msrpamt * discountpercent
discountprice = msrpamt - amtoff

#output phase
print("Make",make)
print("Model",model)
print("MSRP amount $",msrpamt)
print("Discount percent",discountpercent)
print("Amount off $",amtoff)
print("Final price after discount $",discountprice)

#pause so the window stays open
input("\nPress Enter to exit")
