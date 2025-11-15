lnames = ["Adams", "Baker", "Jones", "Wayne", "Connor", "Mack", "Evans", "Nova", "Diaz", "Craig"]

def names(lnames):
    for i in range(0,10,1):
        print(lnames[i])

def reversenames(lnames):
    for i in range(9,-1,-1):
        print(lnames[i])

print("Names in order:")
names(lnames)

print("Names in reverse order:")
reversenames(lnames)