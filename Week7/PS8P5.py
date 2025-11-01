def compTuition(credithours,districtcode):
    if districtcode == "I":
        pricepercredit = 250
    elif districtcode == "O":
        pricepercredit = 550
    
    tuition = credithours * pricepercredit

    return tuition

totaltuition = 0

r = input("Do you want to calculate tuition (yes or no)?")
while r == "yes":
    lname = input("Enter Last Name:")
    credithours = float(input("Enter credit hours:"))
    districtcode = input("Enter I for in district or enter O for out of district.")
    tuition = compTuition(credithours,districtcode)
    totaltuition = totaltuition + tuition 
    print("Last name:",lname)
    print(f"Tuition Owed: ${tuition:.2f}")
    r = input("Do you want to calculate tuition (yes or no)?")

print(f"Sum of all tuition calculated: ${totaltuition:.2f}")

