class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = len(nums)//2
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                i -= i//2
            else:
                i += i//2

        return -1

        