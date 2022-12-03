foe = []
friend = []
outcome = {"A": "Y", "B": "Z", "C": "X"}
points = {"X": 1, "Y": 2, "Z": 3}
translate = {"A": "X", "B": "Y", "C": "Z"}

with open('Day 2 Input') as file:
    lines = file.readlines()
    for i in lines:
        tmp = i.split(" ")
        foe.append(tmp[0])
        friend.append(tmp[1].strip("\n"))

out = 0
for i in range(len(foe)):
    out += points[friend[i]]
    if outcome[foe[i]] == friend[i]:
        out += 6
    elif translate[foe[i]] == friend[i]:
        out += 3
    else:
        out += 0
print(out)
