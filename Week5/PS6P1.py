#before - set count start value to 1, stop value to 25, increment value to 2
countstart = 1
countstop = 25
incvalue = 2

#in the loop - count ends at 25, add 2 each time to get just the odd numbers
while(countstart <= countstop):
    print(countstart)
    countstart = countstart + incvalue

#after loop - stop 
input("\nPress Enter to exit")