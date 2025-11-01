#Computing batting average
def CompBatAvg(hits, bats):
    avgbat = hits / bats
    return avgbat

#Main Program
totalplayers = 0 

r = input("Do you want to do this program (yes or no)?")

while r == "yes":
    lname = input("Enter player's last name:")
    hits = float(input("Enter number of hits:"))
    bats = float(input("Enter the number of at bats:"))

    avgbat = CompBatAvg(hits, bats)
    print("Player last name:", lname)
    print("Batting Average:", avgbat)

    totalplayers = totalplayers + 1 
    r = input("Do you want to do this program (yes or no)?")

print("Total players entered:",totalplayers)

    
