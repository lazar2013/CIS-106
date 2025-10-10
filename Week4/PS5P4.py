#input phase 
ticketqty = int(input("Enter the number of concert tickets: "))

#process phase 
if ticketqty >= 25:
    priceperticket = 50
elif ticketqty >= 10 and ticketqty <= 24:
    priceperticket = 60
elif ticketqty >= 5 and ticketqty <= 9:
    priceperticket = 70
elif ticketqty < 5:
    priceperticket = 75

totalcost = ticketqty * priceperticket

#output phase
print("Number of tickets:",ticketqty)
print("Price per ticket:${:,.2f}".format(priceperticket))
print("Total cost:${:,.2f}".format(totalcost))

#pause so the window stays open
input("\nPress Enter to exit")
