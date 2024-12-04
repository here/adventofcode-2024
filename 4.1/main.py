import os

# import re

class Aoc:

    def __init__(self, testing):
        print('howdy')
        
        self.testing = testing
        self.lines = []
        self.result = 0

        self.compass = {
            'n' : ( 0, -1),
            'ne': ( 1, -1),
            'e' : ( 1,  0),
            'se': ( 1,  1),
            's' : ( 0,  1),
            'sw': (-1,  1),
            'w' : (-1,  0),
            'nw': (-1, -1)
        }

        if testing:
            input = os.path.dirname(__file__) + '/test'
        else:
            input = os.path.dirname(__file__) + '/in'

        with open(input) as file:
            for line in file:
                self.lines.append(line)

        print(len(self.lines))

    def do_aoc(self):
        for i, line in enumerate(self.lines):
            self.find_xmas(i, line)


    """
        find x
        look for m clockwise starting at n, ne, e, se, s, sw, w, nw
        for all m's continue for a, s
        
        alt: list all possible strings and regex
    """
    def find_xmas(self, line_index, line):
        print(line)
        xs = [i for i, e, in enumerate(line) if e == 'X']
        print(xs)
        for x in xs:
            self.find_mas(line_index, x)
    
    def find_mas(self, line_index, x_index):
        print((line_index, x_index))
        self.result += 1

wip = Aoc(testing = True)

result = wip.do_aoc()

print(wip.result)

# wip.dampen()