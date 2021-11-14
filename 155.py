class Solution:
    def findPeakElement(self, nums):
        for q in range(1, len(nums) - 1):
            if nums[q - 1] < nums[q] > nums[q + 1]:
                return q
        return nums.index(max(nums))