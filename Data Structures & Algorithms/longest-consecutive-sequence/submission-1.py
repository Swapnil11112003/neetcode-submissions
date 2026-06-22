class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        longest = 0

        for num in hash:
            if (num - 1) not in hash:
                length = 1
                while (num + length) in hash:
                    length += 1
                longest = max(length, longest)

        return longest

                
    



        