
from itertools import permutations

class Solution:
    def make(self, solution):
        solution = [[q, w] for q, w in enumerate(solution)]
        output = []
        for q in range(len(solution)):
            string = ''
            for w in range(len(solution)):
                if [q, w] in solution:
                    string += 'Q'
                else:
                    string += '.'
            output.append(string)
        return output
    
    def solveNQueens(self, n):
        output = []
        q = range(n)
        for b in permutations(q):
            if all(abs(b[x] - b[y]) != abs(x - y) for x, y in permutations(b, 2)):
                output.append(self.make(b))

        return output