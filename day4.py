with open("day4.txt") as f:
    data = f.readlines()

data = [line[:-1] for line in data]  # strip /n

def do_contain(line):
    first, second = line.split(',')
    b_first, e_first = map(int, first.split('-'))
    b_second, e_second = map(int, second.split('-'))

    if b_first >= b_second and e_first <= e_second or\
        b_second >= b_first and e_second <= e_first:
        return True
    return False

total = 0

for line in data:
    if do_contain(line):
        total += 1

print(total)

def do_overlap(line):
    first, second = line.split(',')
    b_first, e_first = map(int, first.split('-'))
    b_second, e_second = map(int, second.split('-'))

    if b_first <= b_second and e_first >= b_second or\
        b_second <= b_first and e_second >= b_first:
        return True
    return False

total = 0

for line in data:
    if do_overlap(line):
        total += 1

print(total)