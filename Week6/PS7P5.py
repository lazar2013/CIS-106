f = open("data1.txt", "r")

c = 0
totaltuition = 0.0

#get first part of the data

lname = str(f.readline().rstrip('\n'))

while lname !="":
    dcode = str(f.readline().rstrip('\n'))
    credits = float(f.readline())

    if dcode == "I":
        costpercredit = 250.00
    else:
        costpercredit = 500.00

    tuition = costpercredit * credits
    c = c + 1
    totaltuition = totaltuition + tuition

    print("Student:", lname)
    print("Credits taken:", credits)
    print("Tuition Owed:", tuition)
    print("  ")

    lname = str(f.readline().rstrip('\n'))

f.close()

print("Number of students", c)
print("Total Tuition Owed:", totaltuition)