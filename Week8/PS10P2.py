def exam_average(score1,score2,score3):
    total = score1 + score2 + score3
    averagescore = total / 3
    return total,averagescore 

lname = str(input("Enter student's last name:"))
score1 = float(input("Enter exam score 1:"))
score2 = float(input("Enter exam score 2:"))
score3 = float(input("Enter exam score 3:"))

total,averagescore = exam_average(score1,score2,score3)
print("Last name:",lname)
print("Total points:",format(float(total), '10,.2f'))
print("Average score:",format(float(averagescore), '10,.2f'))