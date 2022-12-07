end = []
with open('Puzzle Inputs/Day 1 Input') as file:
    lines = file.readlines()
    count = 0
    for i in range(len(lines)):
        if lines[i] != "\n":
            count += int(lines[i])
        else:
            end.append(count)
            count = 0
end.sort()
print(end[len(end)-1])
print(end[len(end)-1]+end[len(end)-2]+end[len(end)-3])
