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

    def is_safe(self, sequence):
        for i in range(len(sequence)):
            if i == 0: continue
            if (sequence[i] - sequence[i-1]) not in [1,2,3]:
                return False
            if i == len(sequence)-1:
                return True
    
    def dampen(self, sequence):
        if self.is_safe(sequence): return True

        # check all lists with one floor removed
        for i in range(len(sequence)):
            if self.is_safe(sequence[0:i] +sequence[i+1:]): return True
        
        # No safe lists with only one floor removed
        print('unsafe')
        return False
    
    def count_safe_reports(self):
        for line in self.lines:
            sequence = [int(x) for x in line.split()]

            # make all lists ascending
            if sequence[0] > sequence[-1]:
                sequence.reverse()

            print(sequence)

            if self.dampen(sequence):
                print('safe')
                self.safe += 1
        
        return self.safe

wip = Aoc(testing = False)

safe_report_count = wip.count_safe_reports()

print(safe_report_count)

# wip.dampen()