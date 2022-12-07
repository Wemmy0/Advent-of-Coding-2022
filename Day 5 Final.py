from collections import defaultdict
import re
inputs, commands = open("Puzzle Inputs/Day 5 Input").read().split("\n\n")

inputs = inputs.split("\n")
inputs.pop()
commands = commands.split("\n")
commands.pop()

stacks = []
for i in inputs:
    stacks.append(i[1::4].replace(" ", ""))
print(stacks)
for command in commands:
    num, fr, to = re.findall(r"\d+", command)
    num, fr, to = int(num), int(fr), int(to)
    print(num, fr, to)
    print(f"Moving {num} items from {fr} to {to}")
    print(stacks[to])
    for i in range(num):
        tmp = stacks[to].append(stacks[fr][len(stacks[fr])-i])
        stacks[fr].pop(len(stacks[fr]-i))
    print(stacks[to])
