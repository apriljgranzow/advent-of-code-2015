import re
from sys import maxsize

def total_area(dimensions):
    l = dimensions[0]
    w = dimensions[1]
    h = dimensions[2]
    smallest_side = maxsize
    sides = [l*w, w*h, h*l]
    for elem in sides:
        if elem < smallest_side:
            smallest_side = elem
    return sum([side*2 for side in sides])+smallest_side

def part_1(lst):
    return sum(total_area(x) for x in lst)

def perimeter(x,y):
    return (2*x)+(2*y)

def smallest_perimeter(dimensions):
    l = dimensions[0]
    w = dimensions[1]
    h = dimensions[2]
    sides = [(l,w),(w,h),(h,l)]
    return min([perimeter(x[0],x[1]) for x in sides])

def volume(dimensions):
    l = dimensions[0]
    w = dimensions[1]
    h = dimensions[2]
    return l*w*h

def part_2(lst):
    return sum([smallest_perimeter(x) + volume(x) for x in lst])

if __name__ == '__main__':
    input_format = r'(\d+)x(\d+)x(\d+)'
    grammar = re.compile(input_format)
    
    with open('input.txt') as file:
        text = file.read(); file.close()
    results = grammar.findall(text)
    inputs = [tuple(int(x) for x in y) for y in results]
    print(part_1(inputs))
    print(part_2(inputs))

