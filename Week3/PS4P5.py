#input phase
lname = input("Enter the user's last name")
dependents = int(input("Enter the number of dependents"))
grossincome = float(input("Enter gross income"))

#process phase
adjustedgrossincome = grossincome - dependents * 12000
if adjustedgrossincome <= 50000:
    tax = 0.10
else:
    tax = 0.20

incometax = adjustedgrossincome * tax
if incometax < 0:
    incometax = 100

#outputphase
print("Last name:",lname)
print("Gross income: $",format(grossincome, ".2f"))
print("Number of dependents:",dependents)
print("Adjusted gross income: $",format(adjustedgrossincome, ".2f"))
print("Income tax: $",format(incometax, ".2f"))

#pause so window stays open
input("\nPress Enter to exit")
