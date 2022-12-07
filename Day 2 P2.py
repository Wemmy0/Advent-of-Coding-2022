foe = []
friend = []
win = {"A": "Y", "B": "Z", "C": "X"}
draw = {"A": "X", "B": "Y", "C": "Z"}
loss = {"A": "Z", "B": "X", "C": "Y"}
points = {"X": 1, "Y": 2, "Z": 3}

with open('Puzzle Inputs/Day 2 Input') as file:
    lines = file.readlines()
    for i in lines:
        tmp = i.split(" ")
        foe.append(tmp[0])
        friend.append(tmp[1].strip("\n"))

count = 0
for i in range(len(foe)):
    match friend[i]:
        case "X":
            # Loss
            count += points[loss[foe[i]]]
        case "Y":
            # Draw
            count += points[draw[foe[i]]]
            count += 3
        case "Z":
            # Win
            count += points[win[foe[i]]]
            count += 6
print(count)
