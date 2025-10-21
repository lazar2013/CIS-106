f = open("p4d.txt", "r")

#initialize counters and sums to 0
c = 0.0
total_ep = 0.0

#get first data line
item = str(f.readline().rstrip('\n'))

while item !="":
    qty = float(f.readline())
    price = float(f.readline())

    ep = qty * price
    #sum and count in the loop
    total_ep = total_ep + ep
    c = c + 1 

    #display a line of data
    print("Item is:            ",item)
    print("Quantity is:        ",qty)
    print("Price is:           ",price)
    print("Extend Price is:    ",ep)
    
    #get next data
    item = str(f.readline().rstrip('\n'))

#After the loop - 
#final calculations
#display them in sum and counts
print("Total Extended Prices:  ",total_ep)
print("Number of orders:       ",c)
avg = total_ep / c
print("Average Order:          ",avg) 