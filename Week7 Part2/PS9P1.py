def CompSales(month, sales):
    if month == "Jan" or month == "Feb" or month == "March":
        forecastpercent = 0.10
    elif month == "April" or month == "May" or month == "June":
        forecastpercent = 0.15
    elif month == "July" or month == "Aug" or month == "Sept":
        forecastpercent = 0.20
    else:
        forecastpercent = 0.25

    nextMonthSales = sales * (1 + forecastpercent)
    return nextMonthSales

totalsales = 0

r = input("Do you want to compute next month's sales (yes or no)?")
while r == "yes":
    lname = input("Enter last name:")
    month = input("Enter month:")
    sales = float(input("Enter current sales:"))
    nextMonthSales = CompSales(month, sales)
    print("Last name",lname)
    print(f"Next month's sales forecast ${nextMonthSales:.2f}")

    totalsales = totalsales + nextMonthSales 
    r = input("Do you want to compute next month's sales (yes or no)?")

print(f"Sum of all forecasted sales ${totalsales:.2f}")