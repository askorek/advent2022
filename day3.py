with open("day3.txt") as f:
    data = f.readlines()

data = [line[:-1] for line in data]  # strip /n

total = 0

for line in data:
    middle = len(line)//2
    part1 = line[:middle]
    part2 = line[middle:]

    common = set(part1).intersection(set(part2))
    common = common.pop()
    
    value = ord(common)
    if value > 90:
        value -= 96
    else:
        value -=38

    total += value
print(total)


# part 2
line_number = 0
rucksags = [0,0,0]
total = 0

for line in data:
    rucksags[line_number] = line
    line_number += 1
    if line_number > 2:
        line_number = 0
        common = set(rucksags[0]).intersection(set(rucksags[1])).intersection(set(rucksags[2]))
        common = common.pop()
        value = ord(common)
        if value > 90:
            value -= 96
        else:
            value -=38
        total += value

print(total)
