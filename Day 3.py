import string

end = []
lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase
with open('Puzzle Inputs/Day 3 Input') as file:
    lines = file.readlines()
    count = 0
    for i in lines:
        compartment_1 = i[:int(len(i) / 2)]
        compartment_2 = i[int(len(i) / 2):].strip("\n")
        counter = 0
        for i in compartment_1:
            if i in compartment_2:
                if i in lower_alphabet:
                    end.append(lower_alphabet.index(i)+1)
                    break
                else:
                    end.append(upper_alphabet.index(i)+27)
                    break

print(sum(end))
