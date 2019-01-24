import solution as s

def test_is_vowel():
    vowels = list('aeiou')
    non_vowels = list('qwrtypsdfghjklzxcvbnm')
    for vowel in vowels:
        assert s.is_vowel(vowel)
    for non_vowel in non_vowels:
        assert not s.is_vowel(non_vowel)

def test_at_least_three_vowels():
    tests = {
        'aei' : True,
        'xazegov' : True,
        'aeiouaeiouaeiou' : True,
        'dvszwmarrgswjxmb' : False
    }
    for case in tests:
        assert s.at_least_three_vowels(case) == tests[case]

def test_at_least_one_double_letter():
    tests = {
        'xx' : True,
        'abcdde' : True,
        'aabbccdd' : True,
        'jchzalrnumimnmhp' : False
    }
    for case in tests:
        assert s.at_least_one_double_letter(case) == tests[case]

def test_forbidden_strings():
    tests = {
        'ugknbfddgicrmopn' : False,
        'haegwjzuvuyypxyu' : True
    }
    for case in tests:
        assert s.forbidden_strings(case) == tests[case]

def test_part1():
    tests = {
        'ugknbfddgicrmopn' : True,
        'aaa' : True,
        'jchzalrnumimnmhp' : False,
        'haegwjzuvuyypxyu' : False,
        'dvszwmarrgswjxmb' : False
    }
    pass