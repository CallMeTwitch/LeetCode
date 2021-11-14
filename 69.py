class Solution:
    def mySqrt(self, x):
        sqrt = 0
        num = sqrt // 2 - 1
        while sqrt <= x:
            num += 1
            sqrt = num * num
        return num - 1