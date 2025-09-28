#input phase
ticker = input("Enter stock ticker symbol")
numshares = int(input("Enter the number of shares"))
cost = float(input("Enter the cost per share"))

#process phase 
amtinvested = numshares * cost

#output phase
print("Ticker")
print("The total amount invested in shares is" ,amtinvested)

#pause so the window stays open
input("\nPress Enter to exit")
