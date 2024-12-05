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
        xs = [i for i, e, in enumerate(line) if e == 'A']
        print(xs)
        for x in xs:
            self.look_compass(x, line_index)
    
    def look_compass(self, x_index, y_index):
        # print((x_index, y_index))
        for d in ['ne','se','sw','nw']:
            # print((x_index, y_index))
            # print((d,self.compass[d][0],self.compass[d][1]))
            x_search = x_index + self.compass[d][0]
            y_search = y_index + self.compass[d][1]
            # print((x_search, y_search))
            if self.is_on_board(x_search, y_search):
                if self.lines[y_search][x_search] == 'M':
                    self.look_across(x_index, y_index, d)
                    return # no need to look for second M in cross if one is found
    
    def look_across(self, x_index, y_index, direction):
        print((x_index, y_index, direction))

        # search for 'S' in the other direction by subtracting the primary direction
        x_search = x_index - self.compass[direction][0]
        y_search = y_index - self.compass[direction][1]
        if not self.is_on_board(x_search, y_search): return False
        if not self.lines[y_search][x_search] == 'S': return False

        # get third corner
        mas = []
        x_search = x_index - self.compass[direction][0]
        y_search = y_index + self.compass[direction][1]
        if not self.is_on_board(x_search, y_search): return False
        mas.append(self.lines[y_search][x_search])

        # fourth corner
        x_search = x_index + self.compass[direction][0]
        y_search = y_index - self.compass[direction][1]
        if not self.is_on_board(x_search, y_search): return False
        mas.append(self.lines[y_search][x_search])

        print(mas)
        if 'M' not in mas or 'S' not in mas: return False

        print((x_index,y_index),(x_search,y_search))
        self.result += 1

    def is_on_board(self, x, y):
        # print((x,y))
        # print((0 <= x <= self.width) and (0 <= y <= self.height))
        return (0 <= x <= self.width) and (0 <= y <= self.height)

wip = Aoc(testing = False)

result = wip.do_aoc()

# length of set since all will be double counted
print(wip.result)

# wip.dampen()