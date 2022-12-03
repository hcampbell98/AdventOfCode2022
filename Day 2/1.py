WIN = 6
DRAW = 3
LOSE = 0

X = 1
Y = 2
Z = 3

COMBINATIONS = {
    "A X": DRAW + X,
    "A Y": WIN + Y,
    "A Z": LOSE + Z,
    "B X": LOSE + X,
    "B Y": DRAW + Y,
    "B Z": WIN + Z,
    "C X": WIN + X,
    "C Y": LOSE + Y,
    "C Z": DRAW + Z,
}

with open("input.txt") as f:
    score = 0
    for line in f:
        score += COMBINATIONS[line.strip()]

print(score)