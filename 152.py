class Solution:
    def maxProduct(self, nums):
        neg_nums = nums[:]

        for q in range(1, len(nums)):
            nums[q], neg_nums[q] = max(nums[q - 1] * nums[q], nums[q], neg_nums[q - 1] * nums[q]), min(neg_nums[q - 1] * nums[q], neg_nums[q], nums[q - 1] * nums[q])
            print(nums[q], neg_nums[q])

        return max(nums + neg_nums)