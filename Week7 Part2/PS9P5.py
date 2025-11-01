def CompAssessedValue(county, marketvalue):
    if county == "Cook":
        AVper = 0.90
    elif county == "Dupage":
        AVper = 0.80
    elif county == "McHenry":
        AVper = 0.75
    elif county == "Kane":
        AVper = 0.60
    else:
        AVper = 0.70

    assessedValue = marketvalue * AVper
    return assessedValue 

sumofAssessedValues = 0 
sumofMarketValues = 0

r = input("Do you want to calculate your home's assessed value (yes or no)?")
while r == "yes":
    county = input("Enter county:")
    marketvalue = float(input("Enter your home's market value: $"))
    assessedValue = CompAssessedValue(county, marketvalue)
    print("County:",county)
    print(f"Market Value: ${marketvalue:,.2f}")
    print(f"Assessed Value: ${assessedValue:,.2f}")

    sumofAssessedValues = sumofAssessedValues + assessedValue
    sumofMarketValues = sumofMarketValues + marketvalue
    r = input("Do you want to calculate your home's assessed value (yes or no)?")

print(f"Sum of all Market Values: ${sumofMarketValues:,.2f}")
print(f"Sum of all Assessed Values: ${sumofAssessedValues:,.2f}")
