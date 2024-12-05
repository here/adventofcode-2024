import os

# import re

class Aoc:

    def __init__(self, testing):
        print('howdy')
        
        self.testing = testing
        self.lines = []
        self.result = 0

        self.width = 0
        self.height = 0

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

        self.width = len(self.lines[0])-1
        self.height = len(self.lines)-1

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
            self.look_compass(x, line_index)
    
    def look_compass(self, x_index, y_index):
        # print((x_index, y_index))
        for d in self.compass:
            # print((x_index, y_index))
            # print((d,self.compass[d][0],self.compass[d][1]))
            x_search = x_index + self.compass[d][0]
            y_search = y_index + self.compass[d][1]
            # print((x_search, y_search))
            if (0 <= x_search <= self.width) and (0 <= y_search <= self.height):
                if self.lines[y_search][x_search] == 'M':
                    self.look_line(x_index, y_index, d)
    
    def look_line(self, line_index, x_index, direction):
        print((line_index, x_index, direction))
        self.result += 1

wip = Aoc(testing = True)

result = wip.do_aoc()

print(wip.result)

# wip.dampen()