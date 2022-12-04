out = []
with open('Day 4 Input') as file:
    lines = list(file.readlines())
    for i in range(len(lines)):
        out.append(lines[i].strip("\n").split(","))
counter = 0
for i in range(len(lines)):
    line = [[], []]
    for l in range(len(out[i])):
        tmp = out[i][l].split("-")
        line[l] = list(range(int(tmp[0]), int(tmp[1])+1))
    if all(item in line[0] for item in line[1]):
        counter += 1
    elif all(item in line[1] for item in line[0]):
        counter += 1
print(counter)
