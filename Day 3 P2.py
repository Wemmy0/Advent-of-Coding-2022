import string

end = []
lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase
with open('Puzzle Inputs/Day 3 Input') as file:
    lines = file.readlines()
    count = 0
    for i in range(0, len(lines), 3):
        first = set(lines[i+0].strip("\n"))
        second = set(lines[i+1].strip("\n"))
        third = set(lines[i+2].strip("\n"))
        badge = list(first.intersection(second).intersection(third))[0]
        if badge in lower_alphabet:
            end.append(lower_alphabet.index(badge)+1)
        else:
            end.append(upper_alphabet.index(badge)+27)

print(sum(end))
