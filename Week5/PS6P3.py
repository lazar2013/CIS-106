#Before the loop - set count to 0
count = 0

#ask the user if they want to run the program
r = input("Do you want to run the program (Yes or No)?")

#In the loop - 
while(r=="Yes"):
    lname = input("Enter the student's last name:")
    exam1 = float(input("Enter the score for first exam:"))
    exam2 = float(input("Enter the score for the second exam:"))

    #calculate average score
    average = (exam1 + exam2) / 2
    print("Last name:",lname)
    print("Average score of exams:",average)
    count = count + 1 
    r = input("Do you want to run the program (Yes or No)?")

#After the loop - display the count of student's who entered data
print("Total amount of students who entered data:",count)

#Pause so the screen stays open
input("\nPress Enter to exit")


