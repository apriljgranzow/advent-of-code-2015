from itertools import groupby

def is_vowel(char):
    """Return true if char is vowel - not including y"""
    return char in set('aeiou')

def at_least_three_vowels(string):
    """Return true if string contains at least 3 vowels"""
    return len([x for x in string if is_vowel(x)]) >= 3

def at_least_one_double_letter(string):
    """Return true if at least one letter appears twice
    or more in a row"""
    letter_clusters = [list(g) for k,g in groupby(string)]
    for elem in letter_clusters:
        if len(elem) > 1:
            return True
    return False

def forbidden_strings(string):
    """Return true if string does not contain any of the 
    following substrings: ab cd pq xy"""
    return any([
        'ab' in string,
        'cd' in string,
        'pq' in string,
        'xy' in string
        ])

def passes_all(string):
    return all([
        at_least_three_vowels(string),
        at_least_one_double_letter(string),
        not forbidden_strings(string)])

def part1(lst):
    return [passes_all(string) for string in lst].count(True)

if __name__ == '__main__':
    with open('input.txt') as file:
        lines = file.readlines()
    print(part1(lines))
