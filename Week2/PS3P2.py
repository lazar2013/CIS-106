#input phase
lname = input("Enter student's last name")
midterm = float(input("Enter midterm score"))
final = float(input("Enter final score"))

#process phase
total = midterm + final

#output phase 
print("Student: ", lname)
print("Total points earned",total)

#pause so the window stays open
input('\nPress Enter to exit')