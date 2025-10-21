response = input("Do you want to calculate interest rate (Yes or No)?")

while response == "Yes":

    p = float(input("Enter Principle"))
    r = float(input("Enter interest rate"))

    total_interest = 0.0

    print("Year", "Beginning Balance", "Ending Balance")
    for count in range(1,6):
        i = p * r
        total_interest = total_interest + i
        endingbalance = p + i
        print(count, "       ", p, "       ", endingbalance)
        p = endingbalance 

    response = input("Do you want to calculate interest rate (Yes or No)?")

print("Total interest earned:",total_interest)
