
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


with open("day9.txt") as f:
    data = f.readlines()

data = [line[:-1] for line in data]  # strip /n

for line in data:
    parse_line(line)

print(len(visited))