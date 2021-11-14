class Solution:
    def majorityElement(self, nums):
        out = [nums[0], 1]
        for q in set(nums):
            if nums.count(q) > out[1]:
                out = [q, nums.count(q)]
        return out[0]