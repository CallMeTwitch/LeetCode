import numpy as np

class Solution:
    def maximumGap(self, nums):
        if len(nums) == 1:
            return 0
        return max(np.diff(sorted(nums)))