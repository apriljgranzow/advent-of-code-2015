import solution as s

def test_part1():
    examples = {
        '>'         : 2,
        '^>v<'      : 4,
        '^v^v^v^v^v': 2
    }
    for key in examples:
        assert s.part1(key) == examples[key]
    
def test_part2():
    examples = {
        '^v'         : 3,
        '^>v<'       : 3,
        '^v^v^v^v^v' : 11
    }
    for key in examples:
        assert s.part2(key) == examples[key]