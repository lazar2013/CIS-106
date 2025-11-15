def sales_report(sales):
    if sales > 100000.00:
        percent = 0.10
    elif sales <=100000.00:
        percent = 0.05
    commission = sales * percent 
    nextyear = sales * 1.05
    return commission,nextyear 

lname = input("Enter salesperson last name:")
sales = float(input("Enter sales amount: $"))
commission,nextyear = sales_report(sales)

print("Salesperson:",lname)
print("Commission: $",format(float(commission), '10,.2f'))
print("Next year's target: $",format(float(nextyear), '10,.2f'))