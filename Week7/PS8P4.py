def CompPayRate(jobcode, hoursworked):
    if jobcode == "L":
        payrate = 25
    elif jobcode == "A":
        payrate = 30
    elif jobcode == "J":
        payrate = 50

    if hoursworked > 40:
        grosspay = ((payrate * 40) + (hoursworked - 40) * (payrate * 1.5))
    else:
        grosspay = payrate * hoursworked

    return grosspay 

totalgrosspay = 0

r = input("Do you want to calculate pay (yes or no)?")
while r == "yes":
    lname = input("Enter last name:")
    jobcode = input("Enter job code L, A, or J:")
    hoursworked = float(input("Enter the amount of hours worked:"))
    
    grosspay = CompPayRate(jobcode, hoursworked)
    totalgrosspay = totalgrosspay + grosspay

    print("Employee Last Name:",lname)
    print(f"Employee Gross Pay: ${grosspay:.2f}")
    r = input("Do you want to calculate pay (yes or no)?")

print(f"The total amount of gross pay calculated: ${totalgrosspay:,.2f}")