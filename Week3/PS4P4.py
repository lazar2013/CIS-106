#input phase
name = input("Enter the name of the appliance")
cost = float(input("Enter the cost of the appliance"))

#process phase
if cost <= 1000:
    warranty_price = cost * 0.05
else:
    warranty_price = cost * 0.10
total = cost + warranty_price

#output phase 
print("Name of appliance:",name)
print("Cost of appliance: $",format(cost, ".2f"))
print("Cost of warranty: $",format(warranty_price, ".2f"))
print("Appliance total: $",format(total, ".2f"))

#pause so window stays open
input("\nPress Enter to exit")
