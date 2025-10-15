#Before the loop - set count to 0, set sumgross to 0
count = 0
sumgross = 0

#Ask the user if they want to run the program 
r = input("Do you want to run this program (Yes or No)")

#In the loop - 
while(r == "Yes"):
    lname = input("Enter your last name:")
    workedhours = float(input("Enter the amount of hours worked:"))
    payrate = float(input("Enter the rate of pay: $"))

    #determine if employee receives time and a half pay for hours they worked after 40
    if workedhours > 40:
        overtimehours = workedhours - 40
        grosspay = (overtimehours * payrate * 1.5) + (payrate * 40)
    else:
        grosspay = workedhours * payrate 

    print("Employee's last name:",lname)
    print("Employee's gross pay: $",format(grosspay, ".2f"))

    count = count + 1 
    sumgross = sumgross + grosspay 

    r = input("Do you want to run this program (Yes or No)")

#After the loop - display the sum of all gross pays (sumgross), number of employees counted (count), and average of all employees' grosspay (averagepay)
averagepay = sumgross / count
print("The average gross pay per employee is $",format(averagepay, ".2f"))

#Pause so the window stays open
input("\nPress Enter to exit the screen")