from collections import Counter

def part1(string):
    """Count how many times we go up and down and return what floor we end up on"""
    counts = Counter(string)
    return counts['('] - counts[')']

def part2(string): # best solution is probably linear
    """Return the 1-indexed position of the first instruction that enters the basement (Floor -1)"""
    ground_floor = 0
    current_floor = ground_floor
    for i in range(len(string)):
        if string[i] == '(':
            current_floor += 1
        else:
            current_floor -= 1
        if current_floor == -1:
            return i+1


if __name__ == '__main__':
    with open('input.txt') as file:
        input_ = file.read()
    print(part1(input_))
    print(part2(input_))
