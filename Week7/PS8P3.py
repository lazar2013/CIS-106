def CompMPG(travelledmiles, gallons):
    mpg = travelledmiles / gallons
    return mpg

totaltrips = 0

r = input("Do you want to calculate miles per gallon (yes or no)?")
while r == "yes":
    city = input("Enter the destination city:")
    travelledmiles = float(input("Enter the amount of miles:"))
    gallons = float(input("Enter the amount of gallons used:"))
    mpg = CompMPG(travelledmiles, gallons)
    print("City:",city)
    print(f"Travelled miles:", travelledmiles)
    print(f"The MPG is {mpg:,.2f}")

    totaltrips = totaltrips + 1 

    r = input("Do you want to calculate miles per gallon (yes or no)?")

print("The total amount of trips counted", totaltrips)