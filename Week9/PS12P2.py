lnames = ["Adams", "Baker", "Jones", "Wayne", "Connor", "Mack", "Evans", "Nova", "Diaz", "Craig"]
scores = [95, 90, 85, 80, 75, 70, 65, 70, 75, 80]

def display(lnames, scores):
    for i in range(0,10,1):
        print(lnames[i], "scored", scores[i])

def reversedisplay(lnames, scores):
    for i in range(9,-1,-1):
        print(lnames[i], "scored", scores[i])

print("Names and scores in order:")
display(lnames, scores)

print("Names and scores in reverse order:")
reversedisplay(lnames, scores)
