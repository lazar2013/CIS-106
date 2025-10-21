f = open("data2.txt", "r")
bonus_sum = 0

lname = f.readline().rstrip('\n')
while lname !="":
    salary = float(f.readline())
    if salary >= 100000.00:
        bonus = salary * 0.20
    elif salary >= 50000.00:
        bonus = salary * 0.15
    else:
        bonus = salary * 0.10

    print()
    print("Employee Last Name:", lname)
    print("Employee Salary: $", format(float(salary),'10,.2f'))
    print("Employee Bonus Amount: $", format(float(bonus),'10,.2f'))

    bonus_sum = bonus_sum + bonus
    lname = f.readline().rstrip('\n')
f.close()

print("  ")
print("Total sum of bonuses paid out: $", format(float(bonus_sum),'10,.2f'))