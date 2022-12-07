import re
from collections import defaultdict

inputs, commands = open("Puzzle Inputs/Day 5 Input").read().split("\n\n")
inputs = inputs.split("\n")
inputs.pop()
commands = commands.split("\n")
commands.pop()

stacks_1 = defaultdict(list)
stacks_2 = defaultdict(list)

for input in reversed(inputs):
    for i, letter in enumerate(input[1::4]):
        if letter != " ":
            stacks_1[i + 1].append(letter)
            stacks_2[i + 1].append(letter)

for command in commands:
    amt, fr, to = re.findall(r"\d+", command)
    i = len(stacks_2[int(to)])
    for _ in range(int(amt)):
        move = stacks_1[int(fr)].pop()
        stacks_1[int(to)].append(move)

        move = stacks_2[int(fr)].pop()
        stacks_2[int(to)].insert(i, move)

for stack in [stacks_1, stacks_2]:
    print("".join(s.pop() for s in stack.values()))