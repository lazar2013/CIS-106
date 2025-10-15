#Before the loop - get start, stop, and increment value from user
startValue = int(input("Enter the start value of the count"))
stopValue = int(input("Enter the stop value of the count"))
incrementValue = int(input("Enter the increment amount for the count"))

#In the loop -
while(startValue <= stopValue):
    print(startValue)
    startValue = startValue + incrementValue

#After the loop - end
input("\nPress Enter to exit")