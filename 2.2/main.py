import os

class Aoc:

    def __init__(self, testing):
        print('howdy')
        
        self.testing = testing
        self.lines = []

        self.safe = 0
        
        if testing:
            input = os.path.dirname(__file__) + '/test'
        else:
            input = os.path.dirname(__file__) + '/in'

        with open(input) as file:
            for line in file:
                self.lines.append(line)

        print(len(self.lines))

    def is_safe(self):
        for line in self.lines:
            sequence = [int(x) for x in line.split()]

            # make all lists ascending
            if sequence[0] > sequence[-1]:
                sequence.reverse()
            
            print(sequence)

            dampen = 1
            for i in range(len(sequence)):
                if i == 0: continue
                if (sequence[i] - sequence[i-1]) not in [1,2,3]:
                    if dampen == 0:
                        break
                    dampen -= 1
                    print(dampen)
                if i == len(sequence)-1:
                    self.safe += 1

        print(self.safe)

        return(self.safe)

wip = Aoc(testing = True)

wip.is_safe()