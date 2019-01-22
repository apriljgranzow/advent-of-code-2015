import solution as s

def test_examples():
    examples = {
        '(())'      : 0,
        '()()'      : 0,
        '((('       : 3,
        '(()(()('   : 3,
        '))((((('   : 3,
        '())'       : -1,
        '))('       : -1,
        ')))'       : -3,
        ')())())'   : -3
    }
    for key in examples:
        assert s.part1(key) == examples[key]