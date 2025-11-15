def b_average(score1,score2,score3,handicap):
    sum = score1 + score2 + score3 
    average = sum / 3
    haverage = (sum + handicap) / 3
    return average, haverage

lname = str(input("Enter last name:"))
score1 = float(input("Score 1:"))
score2 = float(input("Score 2:"))
score3 = float(input("Score 3:"))
handicap = float(input("What is your handicap?"))
average,haverage = b_average(score1,score2,score3,handicap)

print("Last name:",lname)
print("Average score:", format(float(average), '10,.2f'))
print("Average score with handicap:", format(float(haverage), '10,.2f'))
