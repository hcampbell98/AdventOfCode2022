WIN = 6
DRAW = 3
LOSE = 0

X = 1
Y = 2
Z = 3

COMBINATIONS = {
    "A X": LOSE + Z,
    "A Y": DRAW + X,
    "A Z": WIN + Y,
    "B X": LOSE + X,
    "B Y": DRAW + Y,
    "B Z": WIN + Z,
    "C X": LOSE + Y,
    "C Y": DRAW + Z,
    "C Z": WIN + X,
}

with open("input.txt") as f:
    score = 0
    for line in f:
        score += COMBINATIONS[line.strip()]

print(score)