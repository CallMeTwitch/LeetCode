class Solution:
    def twoSum(self, nums, target):
        for q in range(len(nums)):
            for w in range(len(nums)):
                if q != w and nums[q] + nums[w] == target:
                    return [q, w]