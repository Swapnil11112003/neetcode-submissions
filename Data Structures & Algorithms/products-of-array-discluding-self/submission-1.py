class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        prod = 1
        for i in range(1,len(nums)):
            prod *= nums[i-1]
            prefix[i] = prod

        suf_prod = 1
        for i in range(len(nums) - 2, -1, -1):
            suf_prod *= nums[i+1]
            suffix[i] = suf_prod

        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]

        return res




        