class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        max_diff = 0
        i = 0
        j = i + 1

        while j < len(nums):
            diff = nums[j] - nums[i]
            max_diff = max(diff, max_diff)
            if nums[i] > nums[j]:
                i += 1
            else: j += 1

        return max_diff
