class Solution:
    def canJump(self, nums):
        new = [[q, q + w + 1] for q, w in enumerate(nums)]
        current = new[0]
        while current[1] < len(new):
            next = max(new[current[0]:current[1]], key = lambda x:x[1])
            if next == current:
                return False
            current = next
        return True