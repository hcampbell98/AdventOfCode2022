elves = []

with open('input.txt') as f:
    elf = 0
    for line in f:
        #remove newlines
        line = line.strip()

        if line == "":
            elves.append(elf)
            elf = 0
        else:
            elf += int(line)

#print biggest elf
print(max(elves))