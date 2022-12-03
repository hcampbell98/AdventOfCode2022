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

#we want to print the sum of the top 3 elves
elves.sort(reverse=True)
print(elves[0] + elves[1] + elves[2])