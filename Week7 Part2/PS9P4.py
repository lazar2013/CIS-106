def CompPrice(miles):
    if miles >= 30:
        tp = 12 
    elif miles >= 20:
        tp = 10
    elif miles >= 10:
        tp = 8
    else:
        tp = 5
    return tp 

totaltp = 0

r = input("Do you want to calculate the ticket price?")
while r == "yes":
    miles = float(input("Enter the amount of miles from downtown Chicago:"))
    tp = CompPrice(miles)
    print(f"Ticket price: ${tp:.2f}")

    totaltp = totaltp + tp
    r = input("Do you want to calculate the ticket price?")

print(f"Sum price of all tickets: ${totaltp:.2f}")
