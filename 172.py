class Solution:
    def fac(self, x):
        if x == 0:
            return 1
        return self.fac(x - 1) * x
    
    def trailingZeroes(self, n):
        start = list(str(self.fac(n))[::-1])
        for q in range(len(start)):
            if start[q] != '0':
                return q