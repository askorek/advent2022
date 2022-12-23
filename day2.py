with open("day2.txt") as f:
    data = f.readlines()

score = 0

for line in data:
    left = line[0]
    right = line[2]

    if right == 'X':
        score += 1
    elif right == 'Y':
        score += 2
    else:
        score += 3

    if (right == 'X' and left == 'A') or (right == 'Y' and left == 'B') or (right == 'Z' and left == 'C'):
        score += 3
    elif (right == 'Y' and left == 'A') or (right == 'Z' and left == 'B') or (right == 'X' and left == 'C'):
        score += 6
    
print(score)

score = 0

for line in data:
    left = line[0]
    right = line[2]

    if right == 'X':
        pass
    elif right == 'Y':
        score += 3
    else:
        score += 6

    if (right == 'Y' and left == 'A') or (right == 'X' and left == 'B') or (right == 'Z' and left == 'C'):
        score += 1
    elif (right == 'Y' and left == 'B') or (right == 'Z' and left == 'A') or (right == 'X' and left == 'C'):
        score += 2
    else:
        score += 3

print(score)    