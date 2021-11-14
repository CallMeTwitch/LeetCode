class Solution:
    def factorial(self, n):
        total = 1
        while n > 1:
            total *= n
            n -= 1
        return total
    
    def uniquePaths(self, m, n):
        m -= 1
        n -= 1
        return self.factorial(m + n) // (self.factorial(m) * self.factorial(n))