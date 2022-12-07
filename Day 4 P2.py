out = []
with open('Puzzle Inputs/Day 4 Input') as file:
    lines = list(file.readlines())
    for i in range(len(lines)):
        out.append(lines[i].strip("\n").split(","))
counter = 0
for i in range(len(lines)):
    line = [[], []]
    for l in range(len(out[i])):
        tmp = out[i][l].split("-")
        line[l] = list(range(int(tmp[0]), int(tmp[1])+1))
    for l in line[0]:
        if l in line[1]:
            counter += 1
            break
print(counter)
