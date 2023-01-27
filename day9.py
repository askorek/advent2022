
visited = set()

head_position = (0,0)
tail_position = (0,0)

def sng(value):
    return int(value/abs(value))

def update_tail():
    global head_position
    global tail_position
    # touching, no update needed
    if abs(head_position[0] - tail_position[0]) <= 1 and abs(head_position[1] - tail_position[1]) <= 1:
        return 
    # horizontal +/-    
    elif head_position[1] == tail_position[1]:
        diff = head_position[0] - tail_position[0]
        # print("horizontal")
        tail_position =  (tail_position[0] + diff//2, tail_position[1])
    # vertical +/-    
    elif head_position[0] == tail_position[0]:
        diff = head_position[1] - tail_position[1]
        # print("vertical")
        tail_position =  (tail_position[0], tail_position[1] + diff//2)
    # diagonally
    else:
        # print("diagonally")
        move_x = sng(head_position[0] - tail_position[0])
        move_y = sng(head_position[1] - tail_position[1])
        tail_position = (tail_position[0] + move_x, tail_position[1] + move_y)
    

def move_and_update(letter):
    global visited
    global head_position
    global tail_position

    if letter == 'L':
        head_position = (head_position[0] - 1, head_position[1])
    elif letter == 'R':
        head_position = (head_position[0] + 1, head_position[1])
    elif letter == 'U':
            head_position = (head_position[0], head_position[1] + 1)
    elif letter == 'D':
            head_position = (head_position[0], head_position[1] - 1)
    else:
        raise NotImplementedError()

    update_tail()
    visited.add(tail_position)

def parse_line(line):
    letter, number = line.split(" ")
    for cnt in range(int(number)):
        move_and_update(letter)

"""
with open("day9.txt") as f:
    data = f.readlines()

data = [line[:-1] for line in data]  # strip /n

for line in data:
    parse_line(line)

print(len(visited))
"""

# ----------------------------- PART 2 ------------------------


def update_tail_f(head_position, tail_position):
    # touching, no update needed
    if abs(head_position[0] - tail_position[0]) <= 1 and abs(head_position[1] - tail_position[1]) <= 1:
        return tail_position
    # horizontal +/-    
    elif head_position[1] == tail_position[1]:
        diff = head_position[0] - tail_position[0]
        # print("horizontal")
        return  (tail_position[0] + diff//2, tail_position[1])
    # vertical +/-    
    elif head_position[0] == tail_position[0]:
        diff = head_position[1] - tail_position[1]
        # print("vertical")
        return (tail_position[0], tail_position[1] + diff//2)
    # diagonally
    else:
        # print("diagonally")
        move_x = sng(head_position[0] - tail_position[0])
        move_y = sng(head_position[1] - tail_position[1])
        return (tail_position[0] + move_x, tail_position[1] + move_y)


def update_line(line):
    for i, element in enumerate(line):
        if i == 0:
            continue # do not update head 
        line[i] = update_tail_f(line[i-1], element)
    return line

def update_visited(line):
    global visited
    visited.add(line[-1])
    return visited

def move_head(line, letter):
    head_position = line[0]
    if letter == 'L':
        head_position = (head_position[0] - 1, head_position[1])
    elif letter == 'R':
        head_position = (head_position[0] + 1, head_position[1])
    elif letter == 'U':
            head_position = (head_position[0], head_position[1] + 1)
    elif letter == 'D':
            head_position = (head_position[0], head_position[1] - 1)
    else:
        raise NotImplementedError()

    return [head_position] + line[1:]

def parse_line_f(text_line, line):
    global visited
    letter, number = text_line.split(" ")
    for cnt in range(int(number)):
        line = move_head(line, letter)
        line = update_line(line)
        update_visited(line)
    return line

line = [(0,0) for el in range(10)]
visited = set()


with open("day9.txt") as f:
    data = f.readlines()

data = [line[:-1] for line in data]  # strip /n

for text_line in data:
    line = parse_line_f(text_line, line)

print(len(visited))
