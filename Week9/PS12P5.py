lnames = []
avgs = []

def data(lnames, avgs):
    f = open("data.txt", "r")

    for i in range(0, 10, 1):
        name = f.readline()
        name = name.rstrip("\n")
        lnames.append(name)

        avg = f.readline()
        avg = avg.rstrip("\n")
        avgs.append(float(avg))

    f.close()

def display(lnames,avgs):
    for i in range(0, 10, 1):
        print(lnames[i], "batting average is:", avgs[i])

def searchplayer(names, avgs):
    last = input("Enter last name of player you want to look up or say quit:")
    
    while last != "quit":

        found = 0

        for i in range(0, 10, 1):
            if lnames[i] == last:
                print(lnames[i],"batting average is:", avgs[i])
                found = 1

        if found == 0:
            print("Name Not Found!")
            
        last = input("Enter last name of player you want to look up or say quit:")

data(lnames, avgs)
display(lnames, avgs)
searchplayer(lnames, avgs)
