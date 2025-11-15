lnames = []
scores = []

def data(lnames, scores):
    f = open("data.txt", "r")

    for i in range(0, 10, 1):
        name = f.readline()
        name = name.rstrip("\n")
        lnames.append(name)

        score = f.readline()
        score = score.rstrip("\n")
        scores.append(int(score))

    f.close()

def hilow(lnames, scores):
    high_var = 0
    low_var = 999

    high_index = 0
    low_index = 0 

    for i in range(0, 10, 1):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i

        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print("Highest score of:", high_var, "is earned by:", lnames[high_index])
    print("Lowest score of:", low_var, "is earned by:", lnames[low_index])

data(lnames, scores)
hilow(lnames, scores)