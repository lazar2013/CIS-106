#input phase
lname = input("Enter employee's last name: ")
salary = float(input("Enter employee's annual salary: "))
joblevel = int(input("Enter employee's job level: "))

#process phase
if joblevel >= 10:
    bonusrate = 0.25
elif joblevel >= 5 and joblevel <= 9:
    bonusrate = 0.20
else: 
    bonusrate = 0.10

bonus = salary * bonusrate

#output phase
print("Employee's last name:",lname)
print("Employee's bonus:${:,.2f}".format(bonus))

#pause so the window stays open
input("\nPress Enter to exit")