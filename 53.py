class Solution:
    def maxSubArray(self, nums):
        for q in range(1, len(nums)):
            if nums[q - 1] > 0:
                nums[q] += nums[q - 1]
        return max(nums)