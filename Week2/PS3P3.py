#input phase
friend1 = input("Enter the name of the first friend")
friend2 = input("Enter the name of the second friend")
friend3 = input("Enter the name of the third friend")
totalpay = float(input("Enter the total amount paid for all three friends"))

#process phase
share = totalpay / 3

#output phase
print("Pay for" ,friend1 ,share)
print("Pay for" ,friend2 ,share)
print("Pay for" ,friend3 ,share)

#pause so the window stays open
input("\nPress Enter to exit")