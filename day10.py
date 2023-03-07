with open("day10.txt") as f:
    data = f.readlines()

data = [line[:-1] for line in data]  # strip /n

"""noop
addx 3
addx -5"""

def check_if_signal(cycle, x):
    if cycle%40 == 20 and cycle <= 220:
        signal.append(cycle*x)

x = 1
cycle = 0
signal = []
for line in data:
    #print(line)
    if line == "noop":
        cycle += 1
        check_if_signal(cycle, x)
        
    else:
        cycle += 1
        check_if_signal(cycle, x)
        cycle += 1
        check_if_signal(cycle, x)
        value_to_add = line.split(" ")[1]
        x = x + int(value_to_add)
        

print(cycle, x)
print(signal)
print(sum(signal))
