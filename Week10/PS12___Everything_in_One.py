def dl1 (mylist):
    n = int(input("Number of items for your list"))
    for n in range(0,n,1):
        s = int(input("Enter an integer"))
        mylist.append(s)
    return mylist
def displaylist(mylist):
    for item in mylist:
        print(item)

#main
mylist = []  #defining an empty list
mylist = dl1(mylist)
displaylist(mylist) #display each item in the list 
print(mylist)

#DL2
mylist.insert(0,99)
print(mylist)

#DL3
mylist[0] = 100
print(mylist)

#DL4
mylist2 = [500, 600, 700, 800, 900]
mylist.extend(mylist2)
print(mylist)

#DL5
mylist.remove(800)
print(mylist)

#DL6
mylist.pop(2)
print(mylist)

#DL7
gradelist = ["A", "B", "C", "A", "A", "C"]
print(gradelist)

#DL8
print("Count of A grades in the list:", gradelist.count("A"))

#DL9
print("Position of first B grade:" ,gradelist.index("B"))

#DL10
if "F" in gradelist: 
    print("F is in the list")
else:
    print("F is not in the list")

#DL11
mylist2.clear()
print("Second list should be cleared", mylist2)

#DL12
del mylist2
print("Second list has been deleted")

#DL13
playerslist = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print(playerslist)

#DL14
playerslist.sort()
print(playerslist)

#DL15
players2 = playerslist.copy()
print(players2)

#DL16
players2.reverse()
print("Players list:",playerslist)
print("Players list reversed:",players2)