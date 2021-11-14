class Solution:
    def __init__(self):
        self.mem = [1, 1]
        
    def climbStairs(self, n):
        if n <= len(self.mem) - 1:
            return self.mem[n]
        self.mem.append(sum(self.mem[-2:]))
        return self.climbStairs(n)