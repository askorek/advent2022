with open("day1.txt") as f:
    data = f.readlines()

calories = [0]

for line in data:
    if line == "\n":
        calories.append(0)
    else:
        calories[-1] += int(line.split('\n')[0])

print(max(calories))
print(sum(sorted(calories)[-3:]))