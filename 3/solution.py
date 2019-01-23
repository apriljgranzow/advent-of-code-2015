
def adjust_position(x,y,direction):
    if direction == '^':
        position = (x,y+1)
    elif direction == 'v':
        position = (x,y-1)
    elif direction == '>':
        position = (x+1,y)
    elif direction == '<':
        position = (x-1,y)
    return position

def part1(string):
    # Input is one long string, Santa stops after each character
    lst = [x for x in string]
    pos = (0,0)
    visited = {pos}
    for elem in lst:
        pos = adjust_position(pos[0],pos[1],elem)
        visited.add(pos)
    return len(visited)

def part2(string):
    lst = [x for x in string]
    pos1 = (0,0)
    pos2 = (0,0)
    visited = {pos1,pos2}
    for i in range(len(lst)):
        if (i % 2 == 0):
            pos1 = adjust_position(pos1[0],pos1[1],lst[i])
            visited.add(pos1)
        else:
            pos2 = adjust_position(pos2[0],pos2[1],lst[i])
            visited.add(pos2)
    return len(visited)


if __name__ == '__main__':
    with open('input.txt') as file:
        input_ = file.read(); file.close()
    print(part1(input_))
    print(part2(input_))