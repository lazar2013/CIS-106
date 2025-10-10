#input phase
principleamt = int(input("Enter a principle amount of a CD"))
yearsmaturity = int(input("Enter year to maturity of the CD"))

#process phase
if principleamt > 100000 and yearsmaturity == 5:
    interestrate = 0.06
elif principleamt >= 50000 and principleamt <= 100000 and yearsmaturity == 10:
    interestrate = 0.05
elif principleamt >= 50000 and principleamt <= 100000 and yearsmaturity == 5:
    interestrate = 0.04
else:
    interestrate = 0.02

firstyearinterest = principleamt * interestrate 

#output phase
print("Principle: ${:,.2f}".format(principleamt))
print("Interest Rate: {:.0f}%".format(interestrate * 100))
print("The interest amount for first year: ${:,.2f}".format(firstyearinterest))

#pause so window stays open 
input("\nPress Enter to exit")