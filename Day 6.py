with open('Puzzle Inputs/Day 6 Input') as file:
    line = file.readline().strip("\n")

def find(num):
    tmp = []
    for i in range(len(line)):
        tmp.append(line[i])
        if len(tmp) == num+1:
            tmp.pop(0)
        if len(tmp) == num:
            duplicates = [character for character in tmp if tmp.count(character) > 1]
            if len(duplicates) != 0:
                pass
            else:
                out = ""
                for i in tmp:
                    out += i
                break
    return line.index(out)+num
print(find(4))
print(find(14))