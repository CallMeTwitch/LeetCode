from itertools import permutations

class Solution:
    def totalNQueens(self, n):
        return sum([1 for b in permutations(range(n)) if all(abs(b[x] - b[y]) != abs(x - y) for x in range(n) for y in range(n) if y - x)])